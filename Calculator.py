from flask import Flask, request , render_template

app = Flask(__name__)


@app.route("/")
def show_form():
    return render_template("calculator.html")


@app.route("/calculate" , methods = ["POST"])
def do_calculation():
    num1 = int(request.form.get("num1"))
    num2 = int(request.form.get("num2"))
    ops = request.form.get("operation")

    if ops == "add":
        return f"addition of first and second number is :  {num1 + num2}"
    
    elif ops == "subtract":
        return f"subtraction of first and second number is :  {num1 - num2}"
    
    elif ops == "div":
        try:
            return f"divide of first and second number is :  {num1 / num2}"
        
        except (ZeroDivisionError):
            return f"this is error zero division"

            
        
    
    else:
        return f"multiply of first and second number is :  {num1 * num2}"





if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=4000)