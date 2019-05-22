from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-lmdem.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)
user = client.user_image
user_name = user['user_name']

# new_data = [{
#     'album': 'di choi',
#     'imagelink': "https://i.pinimg.com/originals/af/0e/87/af0e87b8cde98a0db73f9ade13fb0b2e.jpg",
#     'description':'My Idol <3!!',
#     'month':'3',
#     'year':'2019',
# },
# {
#     'album': 'di hoc',
#     'imagelink': 'https://i.pinimg.com/originals/af/0e/87/af0e87b8cde98a0db73f9ade13fb0b2e.jpg',
#     'description':'Hoc hanh gi tam nay nua =))',
#     'month':'5',
#     'year':'2018',
# }]  
# user_name.insert_many(new_data)

