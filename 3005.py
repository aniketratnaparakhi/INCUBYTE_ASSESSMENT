import sqlite3
# I USED DB BROWSER FOR CONNECTING AND STORING DATA
conn = sqlite3.connect('NEW77.db')

print(conn)

def create():
    conn.execute('''CREATE TABLE HOSPITAL
    (NAME VARCHAR(255) NOT NULL,
    ID VARCHAR(18) PRIMARY KEY NOT NULL,
    OPEN_DATE DATE(8) NOT NULL,
    LAST_CONSULT DATE(8),
    VACCINATION_TYPE CHAR(5),
    DOCTOR_NAME CHAR(255),
    STATE CHAR(5),
    COUNTRY CHAR(5),
    POST_CODE INT(5),
    DOB DATE(8),
    ACTIVE_CUSTOMER CHAR(1));''')

# def insert():
#     conn.executemany("""INSERT OR IGNORE INTO HOSPITAL (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
#       VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""",Data)
#     conn.commit()

def choice():
    global d,n,id,od,ld,vid,dn,st,cn,pc,db,fg,ch
    ch=input("You Want To Add Data In Table Manually(Y/N)")
    if ch == 'Y' or ch=='Yes' or ch=='y':
        print(n:=input("Enter Name = "),id:=input("Enter ID = "),od:=input("Enter O_DATE = "),ld:=input("Enter L_DATE = "),vid:=input("Enter VID = "),\
              dn:=input("Enter DNAME = "),st:=input("Enter State = "),cn:=input("Enter Country = "),pc:=input("Enter PCODE = "),\
              db:=input("Enter DOB = "),fg:=input("Enter Flag = "))
        d=[(n,id,od,ld,vid,dn,st,cn,pc,db,fg)]
        # conn.executemany("""INSERT INTO HOSPITAL (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
        #       VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""",d);
        Data = [('Alex', '123457', 20101012, 20121013, 'MVD', 'Paul', 'SA', 'USA', 123, 6031987, 'A'),
                ('John', '123458', 20101012, 20121013, 'MVD', '', 'TN', 'IND', 356, 6031987, 'A'),
                ('Mathew', '123459', 20101012, 20121013, 'MVD', '', 'WAS', 'PHIL', 456, 6031987, 'A'),
                ('Matt', '12345', 20101015, 20121016, 'MVD', '', 'BOS', 'NYC', 356, 6031987, 'A'),
                ('Jacob', '1256', 20101014, 20121015, 'MVD', 'Kaul', 'VIC', 'AU', 786, 6031987, 'A'),
                ('XYZ', '12369', 20101014, 20121015, 'MVR', 'PATIL', 'VIC', 'IND', 786, 6031987, 'A'),
                (n, id, od, ld, vid, dn, st, cn, pc, db, fg)]
        conn.executemany("""INSERT OR IGNORE INTO HOSPITAL (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
              VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""", Data)
        # insert()
        conn.commit()
    else:
        Data = [('Alex', '123457', 20101012, 20121013, 'MVD', 'Paul', 'SA', 'USA', 123, 6031987, 'A'),
                ('John', '123458', 20101012, 20121013, 'MVD', '', 'TN', 'IND', 356, 6031987, 'A'),
                ('Mathew', '123459', 20101012, 20121013, 'MVD', '', 'WAS', 'PHIL', 456, 6031987, 'A'),
                ('Matt', '12345', 20101015, 20121016, 'MVD', '', 'BOS', 'NYC', 356, 6031987, 'A'),
                ('Jacob', '1256', 20101014, 20121015, 'MVD', 'Kaul', 'VIC', 'AU', 786, 6031987, 'A'),
                ('XYZ', '12369', 20101014, 20121015, 'MVR', 'PATIL', 'VIC', 'IND', 786, 6031987, 'A')]
        conn.executemany("""INSERT OR IGNORE INTO HOSPITAL (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
              VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""", Data)
        # insert()
        conn.commit()


def show():
   cursor = conn.execute("SELECT NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER from HOSPITAL")
   print("NAME\t | ID\t\t | O_Date\t\t | L_Date\t\t | VID\t | D_Name\t | STATE\t | Country\t | P_CODE\t | DOB\t | FLAG")
   for row in cursor:
      print(row[0],"\t","|",row[1],"\t","|",row[2],"\t","|",row[3],"\t","|",row[4],"\t","|",row[5],"\t",
            "|",row[6],"\t\t","|",row[7],"\t","|",row[8],"\t","|",row[9],"\t","|",row[10])
# conn.close()
def groupby():
    cursor = conn.execute("SELECT * from HOSPITAL group by COUNTRY")
    for row in cursor:
        # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8],row[9],row[10])
        conn.execute(f"create table if not exists {row[7]} AS SELECT * FROM HOSPITAL where COUNTRY='{row[7]}'")
        # if ch == 'Y' or ch=='y':
        #     conn.execute(f"INSERT INTO '{row[7]}' (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER)\
        #     SELECT * FROM (SELECT '{n}','{id}','{od}','{ld}','{vid}','{dn}','{st}','{cn}','{pc}','{db}','{fg}') AS tmp WHERE NOT EXISTS(SELECT ID FROM HOSPITAL WHERE ID = '{id}') LIMIT 1")
        print(AS:=conn.execute(f"select * from {row[7]}"))
        for row in AS:
            print(f"details of {row[7]}",row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        # print(f"{row[7]} Table Created")


create()
choice()
show()
groupby()
