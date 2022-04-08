from flask import Flask 
from flask_restx import Resource, Api
from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
    },
    {
        'id': 2,
        'title': 'Dhalgren',
    }
]

@api.route('/books')
class BookList(Resource):
    def get(self):
        return books_db
    def post(self):
        response = api.payload
        books_db.append(response)
        return books_db, 200