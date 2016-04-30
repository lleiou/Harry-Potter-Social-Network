from flask import Flask, render_template, json, request, redirect
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cPickle


app = Flask(__name__)

##########preparation###################
# train = pd.read_csv('static/csv/sorting_hat2.csv')
# feature = pd.DataFrame(np.zeros(shape=(len(train),26+1+1+26+26)))
# ab = 'abcdefghijklmnopqrstuvwxyz'
# for i in feature.index:
#     feature.iloc[i,26] = train.loc[i,'birth']
#     feature.iloc[i,27] = train.loc[i,'gender']
#     for char in ab:
#         feature.iloc[i,ab.index(char)] = train.loc[i,'name'].lower().count(char)
#         feature.iloc[i,28+ab.index(char)] = train.loc[i,'hair'].lower().count(char)
#         feature.iloc[i,54+ab.index(char)] = train.loc[i,'eye'].lower().count(char)
# y = [1,3,4,2,1,4,2,1,3,1,3,1,3]
# model = RandomForestClassifier(n_estimators=500)
# model.fit(feature.values, y)
# y_test = model.predict(feature.values)
with open("hat.pkl", "rb") as f:
    model = cPickle.load(f)
@app.route("/")
def main():
    return render_template('sorting-hat.html')

@app.route('/sortinghat2',methods=["GET", "POST"])
def sortinghat2():
	return render_template('sorting-hat2.html')

@app.route('/sortinghat3',methods=["GET", "POST"])
def sortinghat3():
	return render_template('sorting-hat3.html')

@app.route('/sortinghat4',methods=["GET", "POST"])
def sortinghat4():
	return render_template('sorting-hat4.html')

@app.route('/sortinghat5',methods=["GET", "POST"])
def sortinghat5():
	return render_template('sorting-hat5.html')

@app.route('/sortinghat6',methods=["GET", "POST"])
def sortinghat6():
	return render_template('sorting-hat6.html')

@app.route('/Sort', methods=["POST"])
def Sort():
	name = str(request.form['fname'])
	gender = int(request.form['gender'])
	birth = int(request.form['birth'])
	hair = str(request.form['hair'])
	eye = str(request.form['eye'])
	f = np.zeros(26+1+1+26+26)	
	f[26] = birth
	f[27] = gender
	ab = 'abcdefghijklmnopqrstuvwxyz'
	for char in ab:
		f[ab.index(char)] = name.lower().count(char)
		f[28+ab.index(char)] = hair.lower().count(char)
		f[54+ab.index(char)] = eye.lower().count(char)
	a = int(model.predict(f.reshape(1,len(f))))
	data = [{"house": a}]
	with open('static/js/data.json','w') as f:
		json.dump(data,f, ensure_ascii = False, encoding = 'utf-8')	
	print("b")
	return render_template("sorting-hat2.html")	

@app.route('/Back3', methods=["GET", "POST"])
def Back3():
	return render_template("sorting-hat3.html")

@app.route('/Back4', methods=["GET", "POST"])
def Back4():
	return render_template("sorting-hat4.html")

@app.route('/Back5', methods=["GET", "POST"])
def Back5():
	return render_template("sorting-hat5.html")

@app.route('/Back6', methods=["GET", "POST"])
def Back6():
	return render_template("sorting-hat6.html")

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5014))
    app.run(host='0.0.0.0', port=port)