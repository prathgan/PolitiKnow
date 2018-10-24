from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.neural_network import MLPClassifier
import pickle
import os
from random import shuffle
from collections import Counter
from copy import deepcopy


app = Flask(__name__,  template_folder="user_interface_html")

@app.route('/')
def signin():
    global politicians
    global users
    try:
        if politicians!=None:
            pass
            # print ("already initialized")
    except NameError:
        # print("first time visiting page")
        # [name,age,election,party,bio,abortion,same_sex,arms,affirmative_action,immigration,aid,weed,taxes,wages,enviro,military,bodycams,schools,renewable_e,img_url]
        politicians=[["Donald Trump","72","Presedential","Republican","Donald John Trump is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School of the University of Pennsylvania.","0","0","10","0","10","0","0","0","0","0","10","0","3","1","https://ly.usembassy.gov/wp-content/uploads/sites/246/16114538_1227645557304882_4439457132240667293_n-1.jpg"],["Barack Obama","57","Presedential","Democrat","Barack Hussein Obama II is an American politician who served as the 44th President of the United States from January 20, 2009, to January 20, 2017. A member of the Democratic Party, he was the first African American to be elected to the presidency and previously served as a United States Senator from Illinois.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg"],["Bill de Blasio","57","NYC Mayorial","Democrat","Bill de Blasio is an American politician who is currently serving as the 109th Mayor of New York City. Previous to his assumption of the mayoralty, he served as New York City's public advocate from 2010 to 2013.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://www1.nyc.gov/assets/home/images/mayor/bio/deblasiolarge.png"],["Nicole Malliotakis","37","NYC Mayorial","Republican","Nicole Malliotakis is an American politician from New York City. A Republican, she represents part of Bay Ridge, Brooklyn and East Shore, Staten Island in the New York State Assembly. She is the only Republican woman elected in New York City and the first Hispanic-American to win elected office in Staten Island.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://usa.greekreporter.com/files/2012/11/Nicole-Malliotakis.jpg"],["Hilary Clinton","70","Presedential","Democrat","Hillary Diane Rodham Clinton (born October 26, 1947) is an American politician and diplomat who served as the First Lady of the United States from 1993 to 2001, U.S. Senator from New York from 2001 to 2009, 67th United States Secretary of State from 2009 to 2013, and as the Democratic Party's nominee for President of the United States in the 2016 election.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwMDU4NTc3NDIy/hillary-clinton-9251306-2-402.jpg"],["Eliot Engel","71","House of Representatives","Democrat","Eliot Lance Engel is the U.S. Representative for New York's 16th congressional district. He is a member of the Democratic Party. His district, District 16, contains parts of the Bronx and Westchester County.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://www.congress.gov/img/member/e000179.jpg"]]

        # [email, password, liked_list, seen_list, state]
        users = [["pg@gmail.com","Password123",[["Donald Trump","72","Presedential","Republican","Donald John Trump is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School of the University of Pennsylvania.","0","0","10","0","10","0","0","0","0","0","10","0","3","1","https://ly.usembassy.gov/wp-content/uploads/sites/246/16114538_1227645557304882_4439457132240667293_n-1.jpg"],["Barack Obama","57","Presedential","Democrat","Barack Hussein Obama II is an American politician who served as the 44th President of the United States from January 20, 2009, to January 20, 2017. A member of the Democratic Party, he was the first African American to be elected to the presidency and previously served as a United States Senator from Illinois.","10","10","0","10","2","10","10","8","10","10","2","10","10","10","https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg"]],[], "NY"],["kg@gmail.com","Password123",[["Donald Trump","72","Presedential","Republican","Donald John Trump is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School of the University of Pennsylvania.","0","0","10","0","10","0","0","0","0","0","10","0","3","1","https://ly.usembassy.gov/wp-content/uploads/sites/246/16114538_1227645557304882_4439457132240667293_n-1.jpg"]],[],"TX"],["a@a.com","a",[["Donald Trump","72","Presedential","Republican","Donald John Trump is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School of the University of Pennsylvania.","0","0","10","0","10","0","0","0","0","0","10","0","3","1","https://ly.usembassy.gov/wp-content/uploads/sites/246/16114538_1227645557304882_4439457132240667293_n-1.jpg"]],[],"NY"],["b@b.com","b",[["Donald Trump","72","Presedential","Republican","Donald John Trump is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality. Trump was born and raised in the New York City borough of Queens, and received an economics degree from the Wharton School of the University of Pennsylvania.","0","0","10","0","10","0","0","0","0","0","10","0","3","1","https://ly.usembassy.gov/wp-content/uploads/sites/246/16114538_1227645557304882_4439457132240667293_n-1.jpg"]],[],"CA"]]

    return render_template('signin.html')

@app.route('/auth', methods=['POST'])
def auth():
    global users
    emailAddress = request.form['email']
    passwordText = request.form['password']
    userFound = False
    for user in users:
        if user[0]==emailAddress:
            if user[1]==passwordText:
                return redirect('voter_homepage/'+emailAddress)
            else:
                return render_template('incorrect_pass.html')
    return render_template("user_not_found.html")


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_voter')
def register_voter():
    return render_template('register_voter.html')

@app.route('/register_voter_process', methods=['POST'])
def register_voter_process():
    global users
    emailAddress = request.form['email']
    passwordText = request.form['password']
    stateText = request.form['state']
    users.append([emailAddress,passwordText,[],[], stateText])
    return render_template('new_voter.html')


@app.route('/register_politician')
def register_politician():
    return render_template('register_politician.html')

@app.route('/register_politician_process', methods=['POST'])
def register_politician_process():
    global users
    global politicians

    name = request.form['name']
    age = request.form['age']
    election = request.form['election']
    party = request.form['party']
    bio = request.form['bio']

    abortion = request.form['abortion']
    same_sex = request.form['same_sex']
    arms = request.form['arms']
    affirmative_action = request.form['affirmative_action']
    immigration = request.form['immigration']
    aid = request.form['aid']
    weed = request.form['weed']
    tax = request.form['taxes']
    wage = request.form['wage']
    enviro = request.form['enviro']
    military = request.form['military']
    bodycams = request.form['bodycams']
    schools = request.form['schools']
    renewable_e = request.form['renewable_e']

    img_url = request.form['image_url']
    politicians.append([name,age,election,party,bio,abortion,same_sex,arms,affirmative_action,immigration,aid,weed,tax,wage,enviro,military,bodycams,schools,renewable_e,img_url])
    return 'you have been added to the system'

@app.route('/voter_homepage/<user_email>')
def voter_homepage(user_email):
    global users
    current_user = None
    for user in users:
        if user[0]==user_email:
            current_user=user
            break
    return render_template('voter_homepage.html',info=current_user)


@app.route('/voter_home_initial/<name>')
def voter_home_initial(name):
    global politicians
    global users
    global last_seen
    shuffle(politicians)
    first_card = None
    current_user = None
    for user in users:
        if user[0]==name:
            current_user=user
            break
    for person in politicians:
        if person not in current_user[3]:
            first_card = deepcopy(person)
            current_user[3].append(person)
            last_seen = person
            break
    if first_card==None:
        first_card=["You've explored all the candidates on PolitiKnow!"," "," "," "," ","0","0","0","0","0","0","0","0","0","0","0","0","0","0","https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/thumbs-up.png"]

    first_card.append(name)
    return render_template('voter_home.html',card=first_card)

@app.route('/voter_home_positive/<name>', methods=['POST','GET'])
def voter_home_positive(name):
    global politicians
    global users
    global last_seen
    shuffle(politicians)
    first_card = None
    current_user = None
    for user in users:
        if user[0]==name:
            current_user=user
            break
    current_user[2].append(last_seen)
    for person in politicians:
        if person not in current_user[3]:
            first_card = deepcopy(person)
            current_user[3].append(person)
            last_seen = person
            break
    if first_card==None:
        first_card=["You've explored all the candidates on PolitiKnow!"," "," "," "," ","0","0","0","0","0","0","0","0","0","0","0","0","0","0","https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/thumbs-up.png"]
    first_card.append(name)
    return render_template('voter_home.html',card=first_card)

# maybe later add list of disliked
@app.route('/voter_home_negative/<name>', methods=['POST','GET'])
def voter_home_negative(name):
    global politicians
    global users
    global last_seen
    shuffle(politicians)
    first_card = None
    current_user = None
    for user in users:
        if user[0]==name:
            current_user=user
            break
    for person in politicians:
        if person not in current_user[3]:
            first_card = deepcopy(person)
            current_user[3].append(person)
            last_seen = person
            break
    if first_card==None:
        first_card=["You've explored all the candidates on PolitiKnow!"," "," "," "," ","0","0","0","0","0","0","0","0","0","0","0","0","0","0","https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/thumbs-up.png"]

    first_card.append(name)
    return render_template('voter_home.html',card=first_card)

@app.route('/voter_interests/<name>', methods=['GET'])
def voter_interests(name):
    global users
    current_user = None
    for user in users:
        if user[0]==name:
            current_user=user
            break
    liked = current_user[2]
    datum = [name,liked]
    return render_template('voter_interests.html',datum=datum)

@app.route('/voter_interests/more_info/<user_email>/<politician_name>', methods=['GET'])
def more_info(user_email, politician_name):
    politician_name.replace("%20"," ")
    global users
    current_user = None
    for user in users:
        if user[0]==user_email:
            current_user=user
            break
    global politicians
    poli = None
    for person in politicians:
        if person[0]==politician_name:
            poli=person
            break
    if poli==None:
        print("not found")
    return render_template('more_info.html',person=poli)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/poli_view/<politician_name>/<user_email>', methods=['POST','GET'])
def poli_view(politician_name, user_email):
    politician_name.replace("%20"," ")
    global users
    global politicians
    places_list = []
    for person in users:
        for poli in person[2]:
            if poli[0]==politician_name:
                places_list.append(person[4])
                break

    polit = None
    for human in politicians:
        if human[0]==politician_name:
            polit=human
            break

    categorization = Counter(places_list)
    info = [user_email,polit,categorization]
    # print(categorization)

    return render_template('poli_view.html',info=info)
