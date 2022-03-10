from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", my_name=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")


@app.route('/password-generator')
def password_generator():
    from pliki_python.password_generator import generate_password
    password = generate_password()
    return render_template("password-generator.html", new_password=password)

@app.route('/iframe')
def iframe():
    return render_template("iframe.html")

@app.route('/namiot')
def namiot():
    return render_template("namiot/namiot.html")

@app.route('/namiot/wykres-rubla')
def namiot_wykres_rubla():
    return render_template("namiot/wykres-rubla.html")


@app.route('/namiot/mam-te-moc')
def namiot_mam_te_moc():
    return render_template("namiot/mam-te-moc.html")

@app.route('/namiot/brudnopis')
def namiot_brudnopis():
    my_hero1 = "Kubuś Puchatek"
    my_hero2 = "Tygrysek"
    return render_template("namiot/brudnopis.html", hero1= my_hero1 , hero2= my_hero2)


@app.route('/CV-pl')
def cv_pl():
    return render_template("cv-pl.html")

@app.route('/CV-ang')
def cv_ang():
    return render_template("cv-ang.html")


if __name__=="__main__":
    app.run()
