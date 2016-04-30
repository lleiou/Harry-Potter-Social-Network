from flask import Flask, render_template, json, request, redirect
import os


app = Flask(__name__)

############recommender###################


@app.route("/")
def main():
    return render_template('sorting-hat.html')

@app.route('/sortinghat2',methods=["GET", "POST"])
def sortinghat2():

	print("bad")
	return render_template('sorting-hat2.html')

@app.route('/sortinghat3',methods=["GET", "POST"])
def sortinghat3():
	return render_template('sorting-hat3.html')

@app.route('/sortinghat4',methods=["GET", "POST"])
def sortinghat4():
	return render_template('sorting-hat4.html')


@app.route('/Sort', methods=["POST"])
def Sort():
    name = str(request.form['fname'])
    gender = str(request.form['gender'])
    birth = str(request.form['birth'])
    hair = str(request.form['hair'])
    print(name)
    return redirect(url_for('sortinghat4'))
    # if name == 1:
    # 	print(good)
    # 	return redirect('/sortinghat3')
    
    
    # if name == "3":
    # 	return redirect('/sortinghat5')
    # if name == "4":
    # 	return redirect('/sortinghat6')

# @app.route('/')
# def Name_fre_plot():
#     return redirect('/name_fre_plot.html')

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5106))
    app.run(host='0.0.0.0', port=port)

