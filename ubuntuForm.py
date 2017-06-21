from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("profile.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     # result = str(request.form["hostname"])
      hostname = str(request.form["hostname"])
      pw = str(request.form["ps"])
      full_name = str(request.form["full_name"])
      confirm_pw = str(request.form["confirm_pw"])
      lang   = str(request.form["lang"])
      location = str(request.form["location"])
      time_zone = str(request.form["time_zone"])
      proxy = str(request.form["proxy"])
      partition = str(request.form["partition"])


      print(hostname)
      f = open("trialfile.txt", "w+")
      f.write(hostname)
      return render_template("result.html", result=hostname+pw+" "+full_name+" "+confirm_pw+"language : "+lang+" "+location+" "+time_zone+" "+proxy+" "+partition)


if __name__=="__main__":
    app.debug = True
    app.run()
    app.run(debug=True)