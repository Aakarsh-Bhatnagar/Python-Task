from pymongo import MongoClient
import pprint
client=MongoClient()
db=client['Task-Db']
EmployeeDetails=db.EmployeeDetails


def insert():
    name=input("Enter your Name ")
    count=EmployeeDetails.count_documents({'name':name})
    if(count>0):
        raise Exception("Employee Already Exists")
    address=input("Enter your Address ")
    
    
    employee={
        'name': name,
        'address': address
    }
    EmployeeDetails.insert_one(employee)

def update():
    userinput=input('Enter the name of the employee to be updated ')
    count=EmployeeDetails.count_documents({
        'name':userinput
    })
    if(count==0):
        raise Exception("Employee doesn't Exist")
    
    address=input("Enter the updated address ")
    EmployeeDetails.update_one(
        {'name':userinput},
        {
            "$set":{
                        "address":address
                    }
            }
        )

def delete():
    userinput=input('Enter the name of the employee to be deleted ')
    count=EmployeeDetails.count_documents({
        'name':userinput
    })
    if(count==0):
        raise Exception("Employee doesn't Exist")
    EmployeeDetails.delete_one({'name':userinput})

def showdb():    
    print('database contents are:')
    Employee=EmployeeDetails.find()
    for e in Employee:
        pprint.pprint(e)


   

