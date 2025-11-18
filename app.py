from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calculate',methods=['POST'])
def calculate():
    height=float(request.form['height'])
    weight=float(request.form['weight'])
    # BMI Calculation
    bmi=weight/((height/100)**2)
    # BMi Category
    if bmi<18.5:category='Underweight'
    elif bmi<24.9:category='Normal Weight'
    elif bmi<29.9:category='Overweight'
    else:category='Obese'
    return render_template('result.html',bmi=round(bmi,2),category=category)
if __name__=="__main__":
    app.run(debug=True)