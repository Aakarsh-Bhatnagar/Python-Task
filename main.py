import task
print("Enter 0 for viewing the contents of the DB")
print("Enter 1 for inserting ")
print("Enter 2 for updating ")
print("Enter 3 for deleting ")
print("Enter 4 for exiting ")
a=input('Enter your choice ')
if(a=='0'):
    task.showdb()
elif(a =='1'):
    task.insert()
    print('Employee inserted successfully')
    task.showdb()
elif(a=='2'):
    task.update()
    print('Employee Details updated successfully')
    task.showdb()
elif(a=='3'):
    task.delete()
    print('Employee Details deleted successfully')
    task.showdb()
elif(a=='4'):
    print("Exited")
else:
    print('Invalid input')
