from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://marchent-project-c7c4f.firebaseio.com/",None)
fire.put("marchent","admin",{"user_name":"sathya","passward":"sathya"})
print("admin acount is created")