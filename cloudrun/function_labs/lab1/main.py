# main.py

from flask import Flask, request

app = Flask(__name__)

def home(request):
    """Ponto de entrada para o Cloud Functions."""
    return "Hello, Cloud Functions!", 200
