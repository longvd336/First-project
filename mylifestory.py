from flask import Flask, render_template, request, redirect, session,flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from user_database import user_coll , post_coll

app = Flask(__name__)
app.secret_key = "3423"
@app.route('/')
def browser():
    return render_template('login.html',)

@app.route('/mylifestory')
def home():
    list_post = post_coll.find()
    return render_template("mylifestory.html", list_post = list_post)

@app.route('/mylifestory/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'GET':
        return render_template('add_post.html')
    elif request.method == 'POST':
        form = request.form
        new_post = {
            'photo': form['img-upload'],
            'description' : form['description'],
        }
    post_coll.insert_one(new_post)
    return redirect('/mylifestory')


@app.route('/mylifestory/delete/<id>')
def delete(id):
    post = post_coll.find_one({"_id": ObjectId(id)})
    post_coll.delete_one(post)
    return redirect('/mylifestory')


# @app.route('/mylifestory')

# def mylifestory():
    
#     if 'logged' in session:
#         if session['logged'] != False :
            
#             user_collection = user_coll.find_one({"Username":session['logged']})
#             post_collection = post_coll.find_one({"Username":session['logged']})
            
#             return render_template('mylifestory.html', user_collection = user_collection, post_collection = post_collection)
            
#         else :
#             return redirect('/login')
#     else:
#         return redirect('/login')

# @app.route('/mylifestory/delete/<photo>')
# def delete(photo):
   
#     post_collection = post_coll.find_one({"Username":session['logged']})
#     delete_image = post_collection["Post"]
#     delete_post = {"$pull":{"Post":{"photo":photo}}}
#     post_coll.update_one(post_collection,delete_post)
    
#     return redirect("/mylifestory")


@app.route('/login', methods = ["GET", "POST"])
def login():
    if 'logged' in session:
        
        if session['logged'] != False:
            return redirect('/mylifestory')
        else:
            if request.method == 'GET':
                        
                return render_template("login.html")
            elif request.method == 'POST':
                form = request.form
                login_user = form['login_username']
                login_pass = form['login_password']
                user = user_coll.find_one({'Username':login_user})
                if user is None:
                    session['logged'] = False
                    return redirect('/login')

                else:
                    if login_pass == user['Password']:
                        session['logged'] = login_user
                        return redirect('/mylifestory')
                    else:
                        session['logged'] = False
                        return redirect('/login')
    else:
        session['logged'] = False
        return render_template('login.html')                   


@app.route('/logout')
def logout():
    if 'logged' in session:
        session['logged'] = False
    return redirect('/login')

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif (request.method == "POST"):
        form = request.form 
        register_username = form["Username"]
        register_password = form["Password"]
        
        register_date = form["DateofBirth"]
        register_gender = form["Gender"]
        # register_avatar = form["Avatar"]
        register_avatar = form['Avatar']
        
        register_phonenumber = form["Phonenumber"]
        register_email = form["Email"]
        register_aboutme = form["Aboutme"]
        all_data_user = user_coll.find_one({"Username":register_username})
        
        message = "username has been used! "
        if(all_data_user is None ):
            new_list=[]
            new_user = {
                'Username':register_username,
                'Password':register_password,
                'DateofBirth': register_date,
                'Gender': register_gender,
                'Avatar': register_avatar,
                'Phonenumber': register_phonenumber,
                'Email':register_email,
                'Aboutme': register_aboutme,
            }

            new_user_post = {
                'Username':register_username,
                'Post':new_list,
            }
            user_coll.insert_one(new_user)
            post_coll.insert_one(new_user_post)
            flash("Account created!")
            
            return redirect(request.url)
        else:
            flash("Your username has been used please choose another!!")
            return redirect(request.url)

@app.route('/mylifestory/setting/<id>', methods = ['GET', 'POST'])
def setting_profile(id):
    setting_profile = user_coll.find_one({"_id":ObjectId(id)})
    
    if request.method == 'GET':
        return render_template('setting.html', setting_profile= setting_profile)
    elif request.method =='POST':
        form = request.form
        new_value = {"$set":{
            
            'Password': form['password'],
            'DateofBirth': form['dob'],
            'Avatar': form['avatar'],
            'Phonenumber': form['phonenumber'],
            'Email': form['email'],
            'Aboutme': form['aboutme'],
        }
        }
        user_coll.update_one(setting_profile,new_value)
        return redirect('/mylifestory')



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 