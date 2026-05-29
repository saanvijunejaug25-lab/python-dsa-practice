file_name = input("enter your file name")
if file_name.endswith('.gif') == True:
    print("image")

elif file_name.endswith('.jpg')==True:
    print("image/")
else:
    print("application/octet-stream")
