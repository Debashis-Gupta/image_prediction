from flask import Flask, request,render_template,jsonify
import numpy as np

from tensorflow.keras.models import  load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications.inception_v3 import decode_predictions

from show_function import *
total_view = count_views()
total_predict=predict_views()
# print(total_view)
# print(total_predict)


app = Flask(__name__)

print("Loading Model")
model = load_model("model.h5")

@app.route('/')
def hello_world():
    total_predict = old_predict_views()
    return render_template('index.html',total_view=total_view,total_predict=total_predict)


@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        if 'img' not in request.files:
            return "No File Found",400
        x=load_img(request.files['img'],target_size=(299,299))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        pred = model.predict(x)
        decode_pred = decode_predictions(pred, top=1)
        name = np.array(decode_pred)
        output= name[0][0][1]
        print('Output: ',output)
        result = output
        total_predict = predict_views()


        return render_template("index.html",output = "You have predicted : " + str(output),total_view=total_view,total_predict=total_predict)
if __name__ == '__main__':
    app.run()
