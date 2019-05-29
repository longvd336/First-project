from flask import Flask, render_template, request, redirect, session,flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from user_database import user_coll , post_coll
import datetime

app = Flask(__name__)
app.secret_key = "3423"
@app.route('/')
def browser():
    return render_template('login.html')

@app.route('/mylifestory')
def home():

    post = post_coll.find_one({'Username':session["logged"]})
    user = user_coll.find_one({'Username':session["logged"]})

    list_post = post['Post']
    return render_template("mylifestory.html", list_post = list_post, user = user)
    

@app.route('/mylifestory/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'GET':
        post = post_coll.find_one({'Username':session["logged"]})
        album_list=post['Album']
        return render_template('add_post1.html', album_list = album_list)
    elif request.method == 'POST':
        form = request.form
        current_user = post_coll.find_one({'Username':session["logged"]})
        current_user_post = current_user["Post"]
        date_time = datetime.datetime.now().strftime("%c")
      
        # new_post = {
        #     'photo': form['img-upload'],
        #     'description' : form['description'],
        # }
        if form['album'] != None:
            add_post_1 = {"$push":{"Post":{'$each':[{'photo': form['img-upload'],'description' : form['description'], 'link':form['image'],'date':date_time,'album':form['album']}],'$position':0}}}
        else:
            add_post_1 = {"$push":{"Post":{'$each':[{ 'photo': form['img-upload'],'description' : form['description'], 'link':form['image'],'date':date_time,'album':'' }],'$position':0}}}

        # print(current_user)
        # print(form['img-upload'],form['description'] )    
        post_coll.update_one(current_user,add_post_1)
    

    
    return redirect('/mylifestory')


@app.route('/mylifestory/delete/<link>')
def delete(link):
    # post = post_coll.find_one({'Username':session['logged']})
    # post_coll.delete_one(post)
    post_collection = post_coll.find_one({"Username":session['logged']})
    delete_post = {"$pull":{"Post":{"link":link}}}
    post_coll.update_one(post_collection,delete_post)
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
                "Fullname":''
            }

            new_user_post = {
                'Username':register_username,
                'Post':new_list,
                'Album':new_list,
            }
            user_coll.insert_one(new_user)
            post_coll.insert_one(new_user_post)
            flash("Account created!")
            
            return redirect(request.url)
        else:
            flash("Your username has been used please choose another!!")
            return redirect(request.url)
@app.route('/mylifestory/edit_post/<link>', methods=['GET', "POST"])
def edit_post(link):

    all_post = post_coll.find_one({"Username":session['logged']})
    post_list = all_post['Post']
    for item in post_list:
        if item['link'] == link:
            if request.method == "GET":
                return render_template("edit_post.html",post_detail= item )  
            elif request.method == "POST":
                form = request.form
                # post_coll.replace_one({ 'Username':session['logged']},
                # {'description':form['description']},
                
                # )
                    

                return redirect('/mylifestory')



@app.route('/mylifestory/setting/<id>', methods = ['GET', 'POST'])
def setting_profile(id):
    setting_profile = user_coll.find_one({"_id":ObjectId(id)})
    
    if request.method == 'GET':
        return render_template('setting.html', setting_profile= setting_profile)
    elif request.method =='POST':
        form = request.form
        new_value = {"$set":{
            'Fullname':form['fullname'],
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

# ANh-HUy
@app.route('/mylifestory/album')
def album():
    all_user_album = post_coll.find_one({"Username":session['logged']})
    user_album = all_user_album["Album"]
    album_cover = all_user_album["Post"]
    count = 0 
    return render_template('album_general.html',user_album = user_album, album_cover = album_cover, count = count)

@app.route('/mylifestory/album/<album_name>')
def detail(album_name):
    user_profile = post_coll.find_one({"Username":session['logged']})
    user_post = user_profile["Post"]
    user_album = user_profile["Album"]
    return render_template('album_detail.html', user_post = user_post, user_album = user_album, album_name = album_name)

# @app.route('/album/delete/<id>')
# def delete(id):
#     user_profile = post_coll.find_one({"username":"tungdo204"})
#     user_profile = post_coll.find_one({"_id": ObjectId(id)})
#     Foods.delete_one(food)
#     return redirect('/album')

@app.route('/mylifestory/album/add_album', methods = ['GET', 'POST'])
def add_album():
    if request.method == 'GET':
        return render_template('add_album.html')
    elif request.method == 'POST':
        form = request.form
        # new_album = {
        #     'album_name': form['album_name_create'],
        #     'album_desc': form['album_desc_create'],
        # }
        user_to_update = post_coll.find_one({"Username":session['logged']})
        post_coll.update_one(user_to_update, {'$push':{'Album':{'album_name': form['album_name_create'],'album_desc': form['album_desc_create']}}})
    return redirect('/mylifestory/album')


if __name__ == '__main__':
  app.run(debug=True)
 