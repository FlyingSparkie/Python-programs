import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="#toor#",
    database="testdb",
    # database="sys",
)

print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testdb")
# mycursor.execute("CREATE DATABASE studenti")

# mycursor.execute("SHOW DATABASES")
# mycursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(10))')
# mycursor.execute('CREATE TABLE studenti (name VARCHAR(255), age INTEGER(10))')


# sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"

# students = [("Sneezy", 34)),("Sleepy", 23),("Dopey", 29),("Happy", 53),("Grumpy", 21),("Bashful", 25)]
# sqlFormula2 = "SELECT * FROM students WHERE name LIKE '%a%'"
sql = "update students set age = 199 where name = 'Happy'"
# mycursor.execute(sqlFormula, student1),
# mycursor.executemany(sqlFormula2, students)
# mycursor.execute(sqlFormula, student3)
mycursor.execute(sql)

mydb.commit()

# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# for row in myresult:
#    print(row)
