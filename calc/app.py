from unittest import result
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route("/add")
def app_add():
    """Handle Get request to add numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return str(result)

@app.route("/sub")
def app_sub():
    """Handle Get request to subtract numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def app_mult():
    """Handle Get request to multiply numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return str(result)

@app.route("/div")
def app_divide():
    """Handle Get request to divide numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)
    return str(result)
ops ={
    "add":add,
    "sub": sub,
    "mult": mult,
    "div": div
}
@app.route("/math/<op>")
def do_math(op):
    "Do selected op on a and b"
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = ops[op](a,b)

    return str(result)