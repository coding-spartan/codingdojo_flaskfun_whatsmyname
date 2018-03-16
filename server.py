from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#DIFF ROUTE NEEDED TO ADD YOUR NAME/ PROCESS ADDING YOUR NAME
@app.route('/process', methods=['POST'])
def your_name():
    name = request.form['name'] #FUNCTION TO TELL WHERE TO GET THE INFO
                                #IN THIS CASE FROM A FORM (request.form)
    print name
    return redirect('/')
#NEVER RENDER ON A POST ROUTE

app.run(debug=True)