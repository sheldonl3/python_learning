import pymysql

db = pymysql.connect("localhost", "root", "7894", "books")
db2 = pymysql.connect("localhost", "root", "7894", "myemployees")


def select(db, sql):
    cursor = db.cursor()
    try:
        row = cursor.execute(sql)
        print("row=", row)  # 影响行数
        data = cursor.fetchall()
        for row in data:
            if row[2] is not None:  # manager id 有可能是null
                print('department id %d,department name %s,manager id %d,location id %d' % (
                    row[0], row[1], row[2], row[3]))
            else:
                print(
                    'department id %d,department name %s,manager id is none,location id %d' % (row[0], row[1], row[3]))
    except:
        print("Error: unable to fetch data")


def update_insert(db, sql):
    cursor = db.cursor()
    try:
        row = cursor.execute(sql)
        db.commit()  # 有表的更改都要commit
        print('sql "%s" success' % (sql))
        print("row=", row)
    except:
        print("Error: unable to do update_insert")
        db.rollback()


def update_insert_many(db):
    sql = "insert into school values (%s,%s)"
    cursor = db.cursor()
    try:
        rows = cursor.executemany(sql, [(109, "awert"), (150, "toangdu"), (105, "bjut")])  # 多行操作,参数是有内容元组的列表
        db.commit()
        print('sql "%s" success' % (sql))
        print("row=", rows)
    except:
        print("Error: unable to do update_insert_many")
        db.rollback()


def delete(db, sql):
    cursor = db.cursor()
    try:
        rows = cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("Error: unable to delete")
        return
    print("rows=", rows)


if __name__ == "__main__":
    # sql = "select * from departments where department_name='%s'" % ('acc')
    # sql = "select * from departments"
    # select(db2, sql)
    #
    # sql = "insert into person values(5,'saten','f',0,12,6)"
    # sql = "update school set name='cnm' where id='17'"
    # # update_insert(db, sql)
    # db2.close()

    # update_insert_many(db)
    delete(db, "delete from school where id >=20")
    db.close()
