import json

def view_data():
    f = open('data.json','r')
    obj = f.read()
    data = json.loads(obj)
    print(f"The name of all Resources is",data['Resources'],'\n')
    print("the second object of resources is",data['Resources'][1],'\n')
    print(data['Resources'][1]['Name'])
###########

def add():
    Y = input("enter the name of role \n")
    user=input("press 1 for adding")
    if user =="1":
        import json
        f = open("data.json", 'r')
        obj = f.read()
        data = json.loads(obj)

        new_data = data["Resources"][0]["Role"].append(Y)
        print(data)
        with open('data.json','w') as f:
            json.dump(data,f)




def search_name():
    f = open("data.json", 'r')
    obj = f.read()
    data = json.loads(obj)
    if "Resources" in data:
        user = input("enter object number")
        if user == '0':

                print("The Name exists in JSON data")
                print("The attribute in object is \n",data["Resources"][0],'\n',"and the name is\n",data["Resources"][0]["Name"])
        elif user =='1':
                    print("The Name exists in JSON data")
                    print("The attribute in object is \n", data["Resources"][1], '\n', "and the name is\n",data["Resources"][1]["Name"])



def Team_update():
    f = open('data.json','r')
    obj = f.read()
    data = json.loads(obj)
    x=({"TeamA": "Alpha","TeamB": "Beta"})


    new_data = data['Resources'][1].update(x)
    print(data)
    with open('data.json','w') as f:
             json.dump(data,f)

# search_name()
# view_data()
# add()
# Team_update()
