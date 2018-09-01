from flask import Flask, render_template, request, redirect
import pandas as pd
from sklearn.neural_network import MLPClassifier
import pickle
import os
app = Flask(__name__,  template_folder="user_interface_html")

@app.route('/')
def signin():
    return render_template('signin.html')

@app.route('/', methods=['POST'])
def login_post():
    name = 0
    email = 1
    password = 2
    type = 3
    party = 4
    gender = 5
    abortion = 6
    gay = 7
    arms = 8
    affirm = 9
    immigration = 10
    healthcare = 11
    weed = 12
    taxes = 13
    wages = 14
    enviro = 15
    military = 16
    bodycams = 17
    schools = 18
    energy = 19
    emailAddress = request.form['email']
    passwordText = request.form['password']
    df = pd.read_csv('data/users.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    userCol = None
    foundUser = False
    global userData
    for column in df:
        if df[column][email]==emailAddress and df[column][password]==passwordText:
            userCol = df[column]
            foundUser = True
            break
    if foundUser==False:
        return redirect('login_failed')
    if userCol[type]=='1':
        userData = userCol
        return redirect('voter_dashboard')
    if userCol[type]=='2':
        userData = userCol
        return redirect('politician_dashboard')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    attributes_list = []
    for attribute in request.form:
        attributes_list.append(request.form[attribute])
    df = pd.read_csv('data/users.csv')
    colCntr = 0
    for col in df:
        colCntr+=1
    df[str(colCntr)]=attributes_list
    df.drop(df.columns[0],axis=1,inplace=True)
    X = []
    training_data = []
    for att in attributes_list[3:]:
        training_data.append(int(att))
    X.append(training_data)
    y=[1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X,y)
    user_model_data_store = [X,y,clf]
    fileName = "data/models/"+attributes_list[1]
    fileObject = open(fileName,'wb')
    pickle.dump(user_model_data_store, fileObject)
    fileObject.close()
    test_pickled_data = pickle.load(open(fileName,'rb'))
    model = test_pickled_data[2]
    if not assertEquals(model.predict([[1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]),1):
        raise ValueError('unable to train model')
    if os.path.exists("data/users.csv"):
        os.remove("data/users.csv")
    df.to_csv('data/users.csv', encoding='utf-8')
    return redirect('new_user_login')

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False

@app.route('/new_user_login')
def new_user():
    return render_template('newUserSignin.html')

@app.route('/new_user_login', methods=['POST'])
def new_user_logging_in():
    name = 0
    email = 1
    password = 2
    type = 3
    party = 4
    gender = 5
    abortion = 6
    gay = 7
    arms = 8
    affirm = 9
    immigration = 10
    healthcare = 11
    weed = 12
    taxes = 13
    wages = 14
    enviro = 15
    military = 16
    bodycams = 17
    schools = 18
    energy = 19
    emailAddress = request.form['email']
    passwordText = request.form['password']
    df = pd.read_csv('data/users.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    userCol = None
    foundUser = False
    global userData
    for column in df:
        if df[column][email]==emailAddress and df[column][password]==passwordText:
            userCol = df[column]
            foundUser = True
            break
    if foundUser==False:
        return redirect('login_failed')
    if userCol[type]=='1':
        userData = userCol
        return redirect('voter_dashboard')
    if userCol[type]=='2':
        userData = userCol
        return redirect('politician_dashboard')

@app.route('/login_failed')
def try_again():
    return render_template('signinFailed.html')

@app.route('/login_failed', methods=['POST'])
def login_post_another():
    name = 0
    email = 1
    password = 2
    type = 3
    party = 4
    gender = 5
    abortion = 6
    gay = 7
    arms = 8
    affirm = 9
    immigration = 10
    healthcare = 11
    weed = 12
    taxes = 13
    wages = 14
    enviro = 15
    military = 16
    bodycams = 17
    schools = 18
    energy = 19
    emailAddress = request.form['email']
    passwordText = request.form['password']
    df = pd.read_csv('data/users.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    userCol = None
    foundUser = False
    global userData
    for column in df:
        if df[column][email]==emailAddress and df[column][password]==passwordText:
            userCol = df[column]
            foundUser = True
            break
    if foundUser==False:
        return redirect('login_failed')
    if userCol[type]=='1':
        userData = userCol
        return redirect('voter_dashboard')
    if userCol[type]=='2':
        userData = userCol
        return redirect('politician_dashboard')

@app.route('/voter_dashboard')
def voter_dash():
    name = 0
    email = 1
    password = 2
    category = 3
    party = 4
    gender = 5
    abortion = 6
    gay = 7
    arms = 8
    affirm = 9
    immigration = 10
    healthcare = 11
    weed = 12
    taxes = 13
    wages = 14
    enviro = 15
    military = 16
    bodycams = 17
    schools = 18
    energy = 19
    global userData
    df = pd.read_csv('data/users.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    politicians_list = []
    for column in df:
        if int(df[column][category])==2:
            print("found a politician")
            politicians_list.append(df[column])
    fileName = 'data/models/'+userData[email]
    person_data = pickle.load(open(fileName,'rb'))
    model = person_data[2]
    liked_list = []
    for person in politicians_list:
        tempFeatureVector = extract_feature_vector(person)
        confidences = model.predict_proba([tempFeatureVector])
        if model.predict([tempFeatureVector])==1:
            liked_list.append(person)
    print(liked_list)
    return 'hi there ' + userData[name] + '. You are a voter'

def extract_feature_vector(profile):
    v = profile[3:]
    v = [int(numeric_string) for numeric_string in v]
    return v


@app.route('/politician_dashboard')
def politician_dash():
    name = 0
    email = 1
    password = 2
    type = 3
    party = 4
    gender = 5
    abortion = 6
    gay = 7
    arms = 8
    affirm = 9
    immigration = 10
    healthcare = 11
    weed = 12
    taxes = 13
    wages = 14
    enviro = 15
    military = 16
    bodycams = 17
    schools = 18
    energy = 19
    global userData
    return 'hi there ' + userData[name] + '. You are a politician'
