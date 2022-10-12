import pyodbc
dataList=[["Ramazan"],["Kaan"],["GÖKSOY"]]
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=Test;UID=sa;PWD=asdasd;')
cursor = conn.cursor()

tableCreate=f'CREATE TABLE ##Deneme123 ( Hash varchar (100))'
cursor.execute(tableCreate)
conn.commit()

insert_to_tmp_tbl_stmt = f"INSERT INTO ##Deneme123 VALUES (?)"
      
cursor.executemany(insert_to_tmp_tbl_stmt,dataList)
cursor.fast_executemany = True
conn.commit()
cursor.close()