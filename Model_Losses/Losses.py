from sklearn.metrics import classification_report, confusion_matrix, f1_score, roc_auc_score, precision_score, recall_score, accuracy_score,precision_recall_curve
import matplotlib.pyplot as plt


def confusion_matrix_plot(y_test,y_score):
    confmatrix = confusion_matrix(y_test,y_score)
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.imshow(confmatrix)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Pred 0s', 'Pred 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, confmatrix[i, j], ha='center', va='center', color='red')
    plt.show()


def Evaluation_Parameters(y_test, y_pred):     
    print("confusion metrics\n")
    # confusion_matrix_plot(y_test,y_pred)
    print("precision_score: ", precision_score(y_test, y_pred,average='micro'))
    print(classification_report(y_test, y_pred))