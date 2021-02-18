from flask import Flask, render_template, request, session, flash, redirect, url_for, request, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from data import SourceData
from flask_wtf import CSRFProtect
from flask_dropzone import Dropzone
import pymysql
from conn import *
from forms import *
import os, io, uuid, base64, matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression





app = Flask(__name__)
# session加密的时候已经配置过了.如果没有在配置项中设置,则如下:
app.secret_key = "iloveyou"
CSRFProtect(app)

app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']


class User(object):
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


pwHash = User()


@app.route("/")
def frontEnd():
    return render_template("goodsFront.html")

@app.route("/plot/")
def plot():
    img = io.BytesIO()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    X = np.array([2, 4, 8, 16, 32]).reshape(-1, 1)
    y = [1099, 2599, 3310, 4997, 5339]

    plt.figure()
    plt.title('华为手机运行内存与价格关系图', fontsize=25)
    plt.xlabel('运行内存(GB)', fontsize=20)
    plt.ylabel('价格(元)', fontsize=20)
    plt.plot(X, y, 'ro-')
    plt.axis([0, 38, 1000, 5800])
    plt.grid(True)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('plot.html', plot_url=plot_url)

@app.route("/predict/", methods=["GET", "POST"])
def predict():
    form = addgoodsForm()

    if request.method == "GET":
        return render_template("predict.html", form = form)
    else:
        data = form.predict.data
        # Create an instance of the estimator, LinearRegression
        a = int(data)
        model = LinearRegression()
        # Fit the model on the training data
        X = np.array([2, 4, 8, 16, 32]).reshape(-1, 1)
        y = [1099, 2599, 3310, 4997, 5339]
        model.fit(X, y)

        test_pizza = np.array([[a]])
        predictedPrice = model.predict(test_pizza)[0]
        predicted_price = "%.2f"%(predictedPrice)
        return render_template("showpredict.html", price=predicted_price)

@app.route("/shangPinQianDaun/")
def shangPinQianDuan():
    return render_template("商品前端.html")

@app.route("/yonghuxinxi/")
def yonghuxinxi():
    return render_template("用户信息.html")

@app.route("/fukuan/", methods=['GET', 'POST'])
def fukuan():
    form = goodsForm()
    if request.method == "GET":
        return render_template("付款界面.html", form=form)
    else:
        customerName = form.body3.data
        postcode = form.body2.data
        address = form.body1.data
        a = "insert into customer(CustomerName, Postcode, address) values('{}','{}','{}')".format(customerName, postcode, address)
        connect(a)
        return render_template("successShopping.html")

@app.route("/gouMai/")
def gouMai():
    return render_template("购买.html")

@app.route("/caoshiqi/")
def caoshiqi():
    return render_template("csq手表.html")

@app.route("/zhangshijie/")
def zhangshijie():
    return render_template("购买张世杰.html")

@app.route("/zhangtongfei/")
def zhangtongfei():
    return render_template("购买zhangtongfei.html")

@app.route("/zhanghaoni/")
def zhanghaoni():
    return render_template("sonyzhanghaoni.html")

@app.route("/xx/")
def xx():
    return render_template("xx.html")

@app.route("/limengdan/")
def limengdan():
    return render_template("购买手机页面.html")

@app.route("/malihua/")
def malihua():
    return render_template("Sony.html")

@app.route("/sonyGouWuCe/")
def sonyGouWuCe():
    return render_template("index.html")

@app.route("/dengchang/")
def dengchang():
    return render_template("购买邓畅.html")


@app.route("/sunfuxianglogin/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if request.method == "GET":
        return render_template("登录1.html", form = form)
    elif (
        request.method == "POST" and form.validate()
    ):  # CSRF验证(这里也可以是form.validate_a_submit())
        username = form.username.data
        id = username
        password = form.password.data
        if finduser(id, password):
            goods1 = select()
            return render_template("index2.html", goodsinfos=goods1)
        else:
            return render_template("failsLogin.html")


@app.route("/sunfuxianglogin/")
def sunfuxianglogin():
    form = LoginForm()
    return render_template("登录1.html", form=form)


@app.route("/login/")
def login():
    goods = select()
    return render_template("login.html", goodsinfos=goods)


@app.route("/showgoods/", methods=["GET", "POST"])
def showgoods():
    form = goodsForm()
    if request.method == "GET":
        return render_template("showgoods.html", form = form)
    else:
        s_id = form.goodsid.data
        a = "select * from goods where sno = '{}' ".format(s_id)
        goods = connect2(a)
        return render_template("showgoods2.html", goodsinfos=goods)

@app.route("/showcustomer/")
def showcustomer():
    a = "select * from customer"
    goods = connect2(a)
    return render_template("showcustomer.html", goodsinfos=goods)



@app.route("/showgoodsByName/", methods=["GET", "POST"])
def showgoodsByName():
    form = goodsForm()
    if request.method == "GET":
        return render_template("showgoodsByName.html", form=form)
    else:
        name = form.goodsname.data
        a = "select * from goods where name = '{}'".format(name)
        goods = connect2(a)
        return render_template("showgoods2.html", goodsinfos=goods)


@app.route("/showtypeAll/")
def showtypeAll():
    a = "select * from goodstype"
    goods = connect2(a)
    return render_template("showtypeAll.html", goodsinfos=goods)


@app.route("/showgoodsAll/")
def showgoodsAll():
    a = "select * from goods"
    goods = connect2(a)
    return render_template("showgoodsAll.html", goodsinfos=goods)


@app.route("/addgoods/", methods=["GET", "POST"])
def addgoods():
    form = addgoodsForm()
    if request.method == "GET":
        return render_template("addgoods.html", form=form)
    # elif request.method == "POST" and form.validate():
    else:
        s_id = form.goodsid.data
        s_name = form.goodsname.data
        s_status = form.goodstatus.data
        s_type = form.store.data
        if findgoodsid(s_id):
            return render_template("warningAddgoods.html")
        else:
            a = "insert into goods(sno, name, goodstatus, store) values('{}','{}','{}','{}')".format(s_id, s_name, s_status, s_type)
            connect(a)
            return render_template("successfullyadd.html")
        return render_template("addgoods.html", form=form)


@app.route("/edit/", methods=["GET", "POST"])
def edit():
    form = addgoodsForm()
    if request.method == "GET":
        return render_template("edit1.html", form=form)
    # elif request.method == "POST" and form.validate():
    else:
        s_id = form.goodsid.data
        s_name = form.goodsname.data
        s_status = form.goodstatus.data
        s_type = form.store.data
        a = "UPDATE goods SET name='{}', goodstatus='{}', store='{}'  WHERE sno = '{}' ".format(s_name, s_status, s_type, s_id)
        connect(a)
        b = "select * from goods"
        goods = connect2(b)
        return render_template("showgoodsAll.html", goodsinfos=goods)

@app.route("/updateprice/", methods=["GET", "POST"])
def updateprice():
    form = addgoodsForm()
    if request.method == "GET":
        return render_template("updateprice.html", form=form)
    # elif request.method == "POST" and form.validate():
    else:
        id = form.goodsid.data
        type = form.goodstype.data
        color = form.goodscolor.data
        price = form.goodsprice.data
        remarks = form.goodsremarks.data
        a = "UPDATE goodstype SET type='{}', color='{}', price='{}' , remarks='{}' WHERE sno = '{}' ".format(type, color, price, remarks, id)
        connect(a)
        b = "select * from goodstype"
        goods = connect2(b)
        return render_template("showtypeAll.html", goodsinfos=goods)



@app.route("/addUser/", methods=["GET", "POST"])
def addUser():
    form = userForm()
    if request.method == "GET":
        return render_template("addUser.html", form=form)
    else:
        s_name = form.username.data
        s_password = form.password.data
        hashPassword = pwHash.set_password(s_password)  ####设置哈希值
        if findUserName(s_name):
            return render_template("warningUser.html")
        else:
            a = "insert into user1 values ('{}','{}')".format(
                s_name, hashPassword
            )  # 将哈希值放入数据库
            connect(a)
            return render_template("successfullyadd.html")


@app.route("/deletegoods/", methods=["GET", "POST"])
def deletegoods():
    form = goodsForm()
    if request.method == "GET":
        return render_template("deletegoods.html", form=form)
    else:
        s_id = form.goodsid.data
        if findgoodsid(s_id):
            a = "delete from goods where sno='{}'".format(s_id)
            connect(a)
            return render_template("successfullydelete.html")
        else:
            return render_template("warningdeletegoods.html")


@app.route("/screendelete/", methods=["GET", "POST"])
def screendelete():
    form = goodsForm()
    if request.method == "GET":
        return render_template("screendelete.html", form=form)
    else:
        s_id = form.goodsid.data
        if findgoodsid(s_id):
            a = "delete from goods where sno='{}'".format(s_id)
            connect(a)
            b = "select * from goods"
            goods = connect2(b)
            return render_template("showgoodsAll.html", goodsinfos=goods)
            # return render_template("successfullydelete.html")
        # else:
        #     return render_template("warningdeletegoods.html")

@app.route("/deleteUser/", methods=["GET", "POST"])
def deleteUser():
    form = userForm()
    if request.method == "GET":
        return render_template("deleteUser.html", form=form)
    else:
        s_id = form.username.data
        if findUserName(s_id):
            a = "delete from user1 where 用户名='{}'".format(s_id)
            connect(a)
            return render_template("successfullydelete.html")
        else:
            return render_template("warningdeleteUser.html")


@app.route("/deletegoodstype/", methods=["GET", "POST"])
def deletegoodstype():
    form = goodsForm()
    if request.method == "GET":
        return render_template("deletegoodstype.html", form = form)
    else:
        s_id = form.goodsid.data
        if findtypeid(s_id):
            a = "delete from goodstype where sno='{}'".format(s_id)
            connect(a)
            return render_template("successfullydelete.html")
        else:
            return render_template("warningdeletegoods.html")


@app.route("/editgoods/", methods=["GET", "POST"])
def editgoods():
    form = goodsForm()
    if request.method == "GET":
        return render_template("editgoods.html", form=form)
    else:
        s_id = form.goodsid.data
        new_name = form.goodsname.data
        if findgoodsid(s_id):
            a = "UPDATE goods SET name='{}' WHERE sno='{}'".format(new_name, s_id)
            connect(a)
            return render_template("successfullyedit.html")
        else:
            return render_template("warningeditgoods.html")


@app.route("/editgoodsStore/", methods=["GET", "POST"])
def editgoodsStore():
    form = goodsForm()
    if request.method == "GET":
        return render_template("editgoodsStore.html", form=form)
    else:
        s_id = form.goodsid.data
        new_name = form.store.data
        if findgoodsid(s_id):
            a = "UPDATE goods SET store='{}' WHERE sno='{}'".format(new_name, s_id)
            connect(a)
            return render_template("successfullyedit.html")
        else:
            return render_template("warningeditgoodsStore.html")


@app.route("/showprice/", methods=["GET", "POST"])
def showprice():
    form = goodsForm()
    if request.method == "GET":
        return render_template("showprice.html", form=form)
    else:
        s_id = form.goodsid.data
        a = "select * from goodstype where sno='{}' order by sno asc".format(
            s_id
        )  # order by asc表示升序排序
        goods = connect2(a)
        return render_template("showprice2.html", goodsinfos=goods)


@app.route("/showUser/")
def showUser():
    a = "select * from user1"
    user = connect2(a)
    return render_template("showUser.html", userinfos=user)


@app.route("/showpriceByType/", methods=["GET", "POST"])
def showpriceByType():
    form = goodsForm()
    if request.method == "GET":
        return render_template("showpriceByType.html", form = form)
    else:
        s_type = form.goodstype.data
        a = "select * from goodstype where type='{}'".format(s_type)
        goods = connect2(a)
        return render_template("showprice2.html", goodsinfos=goods)


@app.route("/addprice/", methods=["GET", "POST"])
def addprice():
    form = goodsForm()
    if request.method == "GET":
        return render_template("addprice.html", form=form)
    else:
        s_id = form.goodsid.data
        s_type = form.goodstype.data
        s_color = form.goodscolor.data
        s_price = form.goodsprice.data
        s_remarks = form.goodsremarks.data

        if findgoodsid(s_id):  # 这里去掉了findgoodstypeid()
            a = " insert into goodstype values('{}','{}','{}','{}','{}') ".format(
                s_id, s_type, s_color, s_price, s_remarks
            )
            connect(a)
            return render_template("successfullyadd.html")
        else:
            return render_template("warningaddprice.html")


@app.route("/editscore/", methods=["GET", "POST"])
def editprice():
    form = goodsForm()
    if request.method == "GET":
        return render_template("updateprice.html", form=form)
    else:
        s_id = form.goodsid.data
        new_price = form.goodsprice.data
        if findtypeid(s_id):
            a = "UPDATE goodstype SET price='{}' WHERE sno='{}'".format(new_price, s_id)
            connect(a)
            return render_template("successfullyedit.html")
        else:
            return render_template("warningeditprice.html")


@app.route("/forgetpassword/")
def forgetpassword():
    return render_template("forgetpassword.html")



@app.route("/dataVisualization/")
def dataVisualization():
    data = SourceData()
    return render_template("dataVisualization.html", form=data, title=data.title)


@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)


if __name__ == "__main__":
    app.run()
