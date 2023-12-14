import mysql.connector
import json
from flask import render_template, redirect, url_for, make_response, request, jsonify
from datetime import datetime, date, time, timedelta
import jwt
from functools import wraps
# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

class user_model():
    def __init__(self):
        self.id = 0
        self.total_id = []
        self.secratekey = "asdflkjhmnbvzxcpqowieuryt"
        # connection between mysql and python
        try:
            self.con = mysql.connector.connect(
                user = 'root',
                password = 'Hetu@0617',
                database = 's_analysis'
                )
            # cursor object
            self.con.autocommit = True
            self.cursor = self.con.cursor(dictionary=True)
            print('Done-Connection')
        except Exception as e:
            print(e)
    
        