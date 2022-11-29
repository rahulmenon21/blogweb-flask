import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='blogweb',port=3306)

# def signUp(t):
#     con=getConnection()
#     cur=con.cursor()
#     sql='insert into author values (%s,%s,%s,%s)'
#     cur.execute(sql,t)
#     con.commit()
#     con.close()

def addAuthor(t):
    db = getConnection()
    sql = 'insert into author values(%s,%s,%s,%s)'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()

def selectAllPost():
    con=getConnection()
    cur=con.cursor()
    sql='select * from author_post'
    cur.execute(sql)
    elist=cur.fetchall()
    con.commit()
    con.close()
    return elist

# def checksignin(t):
#     con=getConnection()
#     sql='select email,password from author where email=%s'
#     cur=con.cursor()
#     cur.execute(sql,t[0])
#     data=cur.fetchall()
#     con.commit()
#     con.close()
#     return data

def checklgauthor(t):
    db = getConnection()
    sql = 'select email,password from author where email=%s'
    cr = db.cursor()
    cr.execute(sql, t[0])
    data = cr.fetchall()
    db.commit()
    db.close()
    return data

# def blogcheck(t):
#     con=getConnection()
#     sql='insert into author_post values(%s,%s,%s)'
#     cur=con.cursor()
#     cur.execute(sql,t)
#     con.commit()
#     con.close()

def addPost(t):
    db = getConnection()
    sql = 'insert into author_post values(%s,%s,%s)'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()