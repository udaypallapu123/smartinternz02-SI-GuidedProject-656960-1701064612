from flask import Flask,render_template,url_for,request
import pickle
import os
import pandas as pd
app=Flask(__name__)
model =pickle.load(open("D:\\pizza price prediction\\training\\pizza.pkl",'rb'))
#le=pickle.load(open("columns.pkl","rb"))
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    return render_template("predict.html")


@app.route('/submit',methods=['GET','POST'])
def submit():
    company=request.form.get('company')
    topping=request.form.get('topping')
    variant=request.form.get('variant')
    size=request.form.get('size')
    extra_cheese=request.form.get('extra_cheese')
    extra_sauce=request.form.get('extra_sauce')
    extra_mushrooms=request.form.get('extra_mushrooms')
    
    if None not in(company,topping,variant,size,extra_cheese,extra_sauce,extra_mushrooms):
        company=['A','B','C','D','E'].index(company)
        topping=['beef','black_pepper','chicken','meat','mozzarella','mushrooms','onion','papperoni','smoked_beef','tuna','vegetables','sausage'].index(topping)
        variant=['BBQ_meat_fiesta','BBQ_sausage','american_classic','american_favorite','classic','double_signature','super_supreme','meat_lovers','crunchy','newyork','double_decker','spicy_tuna','extravaganza','meat_eater','gournet_greek','italian_veggie','thai_veggie','neptune_tuna','duble_mix'].index(variant)
        size=['XL','jumbo','large','medium','regular','small'].index(size)
        extra_cheese=['no','yes'].index(extra_cheese)
        extra_sauce=['no','yes'].index(extra_sauce)
        extra_mushrooms=['no','yes'].index(extra_mushrooms)

    total=[company,topping,variant,
           size,extra_cheese,extra_sauce,extra_mushrooms]
    prediction=model.predict([total])
    pred=prediction[0]
    pred=str(pred)+"Rupaih"

    
    return render_template('submit.html',predict=pred)

if __name__=="__main__":
    app.run(debug=True)

