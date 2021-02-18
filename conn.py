from werkzeug.security import generate_password_hash, check_password_hash
import pymysql



def connect(sql):  # 添加数据时起连接作用
    conn = pymysql.connect(
        host="localhost", user="root", password="257718", database="store"
    )
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def connect2(sql):
    conn = pymysql.connect(
        host="localhost", user="root", password="257718", database="store"
    )

    cur = conn.cursor()  # 创建游标对象
    cur.execute(sql)  # 执行sql语句
    conn.commit()
    goods = cur.fetchall()  # stus-goods
    return goods



def select():
    conn = pymysql.connect(
        host="localhost", user="root", password="257718", database="store"
    )
    cur = conn.cursor()
    cur.execute("select * from goods")  # student-goods
    goods = cur.fetchall()  # fetchall方法是返回所有的对象 #stus-goods
    return goods  # stus-goods


def select1():
    conn = pymysql.connect(
        host="localhost", user="root", password="257718", database="store"
    )
    cur = conn.cursor()
    cur.execute("select * from goodstype")  # stuscore-goodstype
    goods1 = cur.fetchall()  # stus-goods1
    return goods1


def selectu():
    conn = pymysql.connect(
        host="localhost", user="root", password="257718", database="store"
    )
    cur = conn.cursor()
    cur.execute("select * from user1")
    u = cur.fetchall()
    return u


def findgoodsid(s_id):  # 定义查询商品id函数
    a = "select sno from goods where sno='{}'".format(s_id)  # 定义查询字符串  #student-goods
    goods = connect2(a)  # 以a为参数调用连接数据库函数  #stus-goods
    if goods == ():  # python连接数据库是以元组的形式返回对象, 这里表示返回结果为空元组, 即没有查询到id对应的商品对象
        return False
    else:
        return True


def findUserName(s_name):
    a = "select 用户名 from user1 where 用户名 = '{}'".format(s_name)
    user = connect2(a)
    if user == ():
        return False
    else:
        return True


def findgoodsName(s_name):
    a = "select name from goods where name='{}'".format(s_name)
    goods = connect2(a)
    if goods == ():
        return False
    else:
        return True


def findtypeid(s_id):
    a = "select sno from goodstype where sno='{}'".format(s_id)
    goods = connect2(a)  # 调用连接函数,连接数据库
    if goods == ():
        return False
    else:
        return True


def finduser(userName, password):
    a = "select 用户名, 密码 from user1 where  用户名= '{}'".format(userName)
    userInfomation = connect2(a)
    for s in userInfomation:    # 此处for语句是用来判断从表单中获取的用户名与密码是否一致,起了一个防止登录时'sql注入'攻击的作用;
        if s[0] == userName and check_password_hash(s[1], password):  # 判断数据库中的密文与输入的密码对应关系;
            return True


def refresh():      #数据可视化实时更新数据
    a = "select * from goods where name = '华为' or name = '小米' or name = 'OPPO' or name = '诺基亚' or name = 'VIVO' or name = '苹果手机'"
    goods = connect2(a)
    result = []

    for data in goods:  # 此处是将数据库返回格式转换为json格式
        data_str = {}
        data_str["name"] = data[1]
        data_str["value"] = data[3]
        result.append(data_str)

    return result
