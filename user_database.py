from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-lmdem.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)
blog_app = client.blog_application
user_coll = blog_app["user_collection"]
post_coll = blog_app["post_collection"]

#2. get/Create database
blog_app = client.blog_application

#3. get/create collection
user_coll = blog_app["user_collection"]
post_coll = blog_app["post_collection"]

#4 User
# user_collection={
#         "Username":"tungdo204",
#         'Password':"c4e29",
#         'DateofBirth': "01-10-2000",
#         'Gender': "male",
#         'Avatar':"myphoto.png" ,
#         'Phonenumber': "0988887777",
#         'Email':"tungdo204@gmail.com",
#         'Aboutme': "asian",
#         }

# user_coll.insert_one(user_collection)

# post_collection = [
#     {
#         "Username" : "tungdo204",
#         "Post": 
#         [
#             {
#                 "photo" : "photo string 1",
#                 "description": "This is my first post",
#                 "album" : "album 1",
#                 "posted_time":"2019"
#             },
#             {
#                 "photo" : "photo string 2",
#                 "description": "This is my second post",
#                 "album" : "album 2",
#                 "posted_time" :"2018"
#             },
#             {
#                 "photo" : "photo string 3",
#                 "description": "This is my first post",
#                 "album" : "album 2",
#                 "posted_time":"2019"

#             }
#         ]
        
#     }
# ]
# post_coll.insert_many(post_collection)    

# User.insert_one(new_user)


#4 User
# user_collection = [
#     {
#         "username" : "tungdo204",
#         "firstName" : "Tung",
#         "middleName" : "Ngoc",
#         "lastName" : "Do",
#         "address":
#             {
#             "type" : "home",
#             "street" : "40 Cat Linh",
#             "city" : "Hanoi",
#             "country" : "Vietnam"
#             },
#         "email":"tungdo204@gmail.com",
#         "phone":"0988887777",
#         "password":"c4e29",
#         "aboutme":"asian",
#         "setting":"theme_1"
#     }
# ]

# post_collection = [
#     {
#         "username" : "tungdo204",
#         "post":[
#             {
#                 "photo" : "photo string 1",
#                 "description": "This is my first post",
#                 "album" : "album1",
#                 "posted_time" : ""
#             },
#             {
#                 "photo" : "photo string 2",
#                 "description": "This is my second post",
#                 "album" : "album2",
#                 "posted_time" : ""
#             },
#         ],
#         "album":
#         [
#             {
#                 "album_name": "album1",
#                 "album_desc": "start of everything"
#             },
#             {
#                 "album_name": "album2",
#                 "album_desc": "just for more"
#             }
#         ]
        
#     }
# ]