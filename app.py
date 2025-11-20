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
    if bmi<18.5:
        category='Underweight'
        message = "You are under the healthy weight range. Consider including more nutritious calories in your diet."
    elif bmi<24.9:
        category='Normal Weight'
        message = "Great! Your BMI is within the healthy range. Keep maintaining a balanced diet and regular exercise."
    elif bmi<29.9:
        category='Overweight'
        message = "You are slightly above the normal range. Regular exercise and mindful eating can help."
    else:
        category='Obese'
        message = "Your BMI is quite high. It may be helpful to adopt a structured diet and exercise routine."
    return render_template('result.html',bmi=round(bmi,2),category=category,message=message)
if __name__=="__main__":
    app.run(debug=True)
