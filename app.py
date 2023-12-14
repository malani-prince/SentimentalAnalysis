from flask import Flask, request, jsonify, render_template, redirect
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from custom_tokenizer import LemmaTokenizer
from  BackEnd.user_data import user_model
# ----------------------------------------- Load the Models -----------------------------------------

model_filename = "New_models/sentiment_model.joblib"
vectorizer_filename = "New_models/tfidf_vectorizer.joblib"

# ----------------------------------------- This is use for the login is successfull Login -----------------------------------------

isUserLogIn = False

with open(model_filename, 'rb') as file:
    logreg = joblib.load(file)
    
with open(vectorizer_filename, 'rb') as file:
    tfidf_vectorizer = joblib.load(file)

# Create the Flsk Application 
app = Flask(__name__, static_folder='static')

user = user_model()
con, cursor = user.con, user.cursor

# -----------------------------------------> (Home Page) Route Starting <----------------------------------------
# it have the 2 buttons 
# 1) Log in  ---> redirect to the  "/login_page"
# 2) Sign in ---> redirect to the "/signup_page"

@app.route('/')
def Home_page():
    return render_template('HomePage.html')

# ----------------------------------------- Login Endpoint -----------------------------------------
# log in have two functionality 
# 1) take the id and password and redirect to ---> '/check_poin'
#       a) id 
#       b) pass
# 2) if any user want to sign up then it redirect to ---> '/signup_page'

@app.route('/login_page', methods=['GET', "POST"])
def Login():
    return render_template('LogInPage___T.html')

# ----------------------------------------- sign up page -----------------------------------------    
# Signup page use for register new user
# insert the data and it after click on submit it redirect to ---> 'return_id' 
# after reaching their we have ofption to login with our id Provided by Algorithms 

@app.route('/signup_page', methods=['GET', 'POST'])
def return_signup_page():
    return render_template('SignUp___T.html')

# --- Return the Id when user sign in ---

# http://127.0.0.1:5000/return_id?first-name=inowefi&last-name=monod&phone-number=1917273727&email=malaniprince55%40gmail.com&password=12

@app.route('/return_id', methods=['GET', 'POST'])
def return_id_of_user():
    if request.method == 'POST':
        # Handle the form submission
        fname = request.form.get('first-name')
        lname = request.form.get('last-name')
        phonenum = request.form.get('phone-number')
        email = request.form.get('email')
        password = str(request.form.get('password'))

        # Insert data into the database and get the user's ID
        query = f'''INSERT INTO s_analysis.user_data
                (`fname`, `lname`, `phonenum`, `email`, `password`) VALUES 
                ('{fname}', '{lname}', '{phonenum}', '{email}', '{password}');'''

        cursor.execute(query)

        q2 = '''select id from s_analysis.user_data;'''
        cursor.execute(q2)
        data = cursor.fetchall()
        data = data[-1]['id']

        # Redirect to another page after successful signup
        return render_template(
            "signupDataDisplay.html",
            uid=data,
            uname=fname,
            lname=lname,
            phonenum=phonenum,
            email=email,
            password=password
        )

    # Handle GET requests here
    return "This route is for form submission. Use a POST request to submit the form data."



# @app.route('/return_id', methods=['GET', 'POST'])
# def return_id_of_user():
#     fname = request.form['first-name']
#     lname = request.form['last-name']
#     phonenum = request.form['phone-number']
#     email = request.form['email']
#     password = str(request.form['password'])    

#     query = f'''INSERT INTO s_analysis.user_data
#             (`fname`, `lname`, `phonenum`, `email`, `password`) VALUES 
#             ('{fname}', '{lname}', '{phonenum}', '{email}', '{password}');'''
    
#     cursor.execute(query)
    
#     q2 = '''select id from s_analysis.user_data;'''
#     cursor.execute(q2)
#     data = cursor.fetchall()    
#     data = data[-1]['id']
#     return render_template(
#             "signupDataDisplay.html",
#             uid = data, 
#             uname = fname,
#             lname = lname, 
#             phonenum=phonenum,
#             email=email, 
#             password=password
        # )

# ----------------------------------------- render page where all the data should be there -----------------------------------------
# It is goint to check the id and password whether this are true or not
# if false then it call error page and display the error msg (E_InserFalseId.html)
# it contain a button in which it redirect to ---> "/login_page"

@app.route('/check_poin', methods=['GET', 'POST'])
def insert_text_from_page():
    id = request.form['id']
    id = int(id)
    password = request.form['password']
    
    query = f'''select password from s_analysis.user_data where id = {id};'''
    cursor.execute(query)
    eid = cursor.fetchall()
    
    print(eid)

    if not eid:
        return "Invalid username or password. Please try again."
    if eid[0]['password'] == password:
        return "VAlid"
    else:
        return "Invalid username or password. Please try again."


# ----------------------------------------- Redirect to isPosorNeg -----------------------------------------
# simpally redirect The html page

@app.route('/isPosOrNeg')
def isPosOrNeg():
    isUserLogIn = True
    return render_template('isPositiveOrNegative.html')
    
# ----------------------------------------- Final Result page where Pos/Neg Shows -----------------------------------------
# print the Final Result whether this is Positive or not

@app.route('/shows', methods=['GET','POST'])
def welcome():
    # if isUserLogIn == True:
        form_data = request.form 
        random_text = form_data.to_dict()
        random_text_tfidf = tfidf_vectorizer.transform([str(random_text['text'])])
        print(type(random_text['text']))
        # # Sentiment Prediction
        sentiment_label = logreg.predict(random_text_tfidf)[0]
        sentiment_map = {'0': "Negative", '1': "Positive"}
        predicted_sentiment = sentiment_map[sentiment_label]
        
        if random_text['text'] == '':
            return  render_template('TextNotInserted.html')
        else:
            return render_template('result.html', predicted_label=predicted_sentiment, text=random_text['text'])
    # else:
    #     return render_template('E_ManageRouteCall.html')    
    
# /\/\/\/\/\/\/\/\/\/\/\ <------ CRUD Operation ------>/\/\/\/\/\/\/\/\/\/\/\ 

# ----------------------------------------- Return all the users exist / Single User -----------------------------------------

@app.route('/get_all_user')
def temp():
    query = "SELECT * FROM s_analysis.user_data;"
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify({
        "message": data
    })

# @app.route('/single_user')
# def return_single_user():
    
    
    

# ----------------------------------------- Run Server -----------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)