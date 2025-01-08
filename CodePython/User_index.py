custumer = []
def inputAdduser(round):
    for index in range(round):
        custumer.append(input("Name User"+str(index)+":"))

def ShowHelloalluser():
    for data in custumer:
        print("Hello " + data )
        
user_input = int(input()) #จำนวนรอบ
inputAdduser(user_input)
ShowHelloalluser