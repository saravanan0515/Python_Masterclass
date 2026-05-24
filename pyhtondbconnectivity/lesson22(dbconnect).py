#play with mysql

import pymysql

#step1:connect to the database 
Connection = pymysql.connect(
    host= 'localhost',
    user='root',
    passwd= 'pass',
    database= 'test' ,# make sure this db exist 
    cursorclass=pymysql.cursors.DictCursor

)
try:
    with Connection.cursor() as cursor:
        #step 2:create a table
        create_query= """
        CREATE  TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        #step 3:insert data

        insert_query= "INSERT INTO employees(name, department) VALUES(%s , %s)"
        values= [("john","IT"),("alice","HR"),("bob","Finance")]
        cursor.executemany(insert_query, values)
        Connection.commit()

        #step 4; select data
        select_query="SELECT * FROM employees"
        cursor.execute(select_query)
        result= cursor.fetchall()

        for row in result:
            print(row)
finally:
    Connection.close()

"""
output in mysql
SHOW TABLES' at line 1
mysql> SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| employees      |
| students       |
+----------------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM  employees;
+----+-------+------------+
| id | name  | department |
+----+-------+------------+
|  1 | john  | IT         |
|  2 | alice | HR         |
|  3 | bob   | Finance    |
+----+-------+------------+
3 rows in set (0.00 sec)
"""
"""
output 
{'id': 1, 'name': 'john', 'department': 'IT'}
{'id': 2, 'name': 'alice', 'department': 'HR'}
{'id': 3, 'name': 'bob', 'department': 'Finance'}
"""