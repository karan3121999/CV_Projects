import mysql.connector

con =mysql.connector.connect(
  host="localhost",user="root",password="1234",database= "EMPLOYEE"
)
if con.is_connected:
  print("connected")
  
  
  #function for check employee exist or not
def check_employee(employee_id):
  sql= 'select * from EMPLOYEE_RECORD where id=%s'   #query to select all rows
  c= con.cursor(buffered=True)# to row count method work properly
  data= (employee_id,)
  
  #excuting sql query
  c.execute(sql,data)
  r= c.rowcount   #row count method to find no of rows with given values
  if r==1:
    return True
  else:
    return False
  

  
  
  
  
def add_employee():
  id=input("enter employee id:")
  #checking id already exixts or not
  if check_employee(id) ==True:
    print("employee already exists")
    menu()
  else:
    NAME= input("enter your name: ")
    POST= input("enter employee post: ")
    SALARY= input("enter empolyee salary" )
    data= id,NAME,POST,SALARY
    
    #inserting details into mysqltable
    sql= 'insert into EMPLOYEE.EMPLOYEE_RECORD values(%s,%s,%s,%s)'
    C= con.cursor()
    
    #excuting the sql query
    C.execute(sql,data)
    con.commit()        #it is used to make changes in table
    print("employee added successfuly")
    menu()
    
    
    
#function for remove employee
def remove_employee():
  id= input("enter emplyee id: ") 
  
  
  #checking id exists or not
  if check_employee(id)==False:
    print("employee does not exist")
    menu()
    
    
  else:
    sql= 'delete from EMPLOYEE_RECORD where id=%s'
    data= id,
    c=con.cursor()
    c.execute(sql, data)
    con.commit()
    print("employee removed")
    menu()
    
    
    
#function for promote emplyeee
def promote_employee():
  id= input("enter employee id: ")
  
  
  if check_employee(id)==False:
    print("employee does not exist")
    menu()
  else:
    amount= int(input("enter increase in salary"))
    #query to fetch salary 
    sql= 'select salary from EMPLOYEE_RECORD where id=%s'
    data= id
    c=con.cursor()
    
    
#excute sql query
    c.execute(sql,data)
    r= c.fetchone()
    t=r[0]+amount
        
#query to update salary


    sql= 'update EMPLOYEE_RECORD set salary=%s where id=%s'
    d= t,id
    c.execute(sql,d)
    con.commit()
    print("employee promoted")
    





#function for display function
def display_employees():
  sql= "select * from EMPLOYEE_RECORD"
  c= con.cursor()
  c.execute(sql)  
  r = c.fetchall()
  for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("-----------------------------\
        -------------------------------------\
        -----------------------------------")
  menu()
    
    
    
    
    
    
    
#function for menu function
def menu():
  print("welcome to employee management system")
  print("press")
  print("1 to add employeee")
  print("2 to remove employee")  
  print("3 to promote employee")  
  print("4 to display employee")  
  print("5 to exit")            
  
  
  
  ch= int(input("enter your choice"))
  if ch==1:
    add_employee()
  elif ch ==2:
    remove_employee()
  elif ch==3:
    promote_employee()
  elif ch ==4:
    display_employees()
  elif ch==5:
    exit(0)  
  else:
    print("invalid choice")
    menu()
    
    
menu()
  
  
  