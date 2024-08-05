from flask import Flask , request
app = Flask(__name__)


@app.route("/add")
def addition():
    return f"this is my test function"



@app.route("/user")
def print_name():
    data = request.args.get("name")
    return f"{data}"

@app.route("/check")
def check_phone():
    data = request.args.get("name")
    if data == "9804807511":
        return f"the is verified phone number"

    else:
        return f"this is not verified phone number."    
    


if __name__ == '__main__':

    app.run(host="0.0.0.0")



# print(addition())