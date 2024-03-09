from jsonschema import validate
from jsonschema import exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, jsonify
import os
from validator import *
api = Flask(__name__)
cred = credentials.Certificate('fluted-union-415721-98b180e95e4a.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref=db.collection("users")
incomes_ref=db.collection("incomes")
expenses_ref=db.collection("expenses")
categories_ref=db.collection("categories")

#users CRUD

@api.route('/users', methods=['GET'])
def userRead():
    try:
        user_id=request.args.get('id')
        if user_id:
            result = users_ref.document(user_id).get()
            return jsonify(result.to_dict()),200
        else:
            result = []
            for user in users_ref.stream():
                res = user.to_dict()
                res['id']=user.id
                result.append(res)
            return jsonify(result),200
    except Exception as e:
        return f"An Error Ocurred: {e}"

@api.route('/users/add', methods=['POST'])
def userCreate():
    try:
        validate(instance=request.json,schema=userSchema)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    try:
        users_ref.add(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error":"An Error Occured: {e}"}), 400

@api.route('/users/update', methods=['POST', 'PUT'])
def userUpdate():
    try:
        validate(instance=request.json,schema=userSchemaUpdate)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400

    if request.json['password']!="" or request.json['confirm']!="":
        if request.json['password']!=request.json['confirm']:
            return jsonify({"error":"Passwords do not match"}),400
    else:
        del request.json['password']
        del request.json['confirm']
    try:
        id = request.json['id']
        del request.json['id']
        users_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@api.route('/users/delete', methods=['GET', 'DELETE'])
def userDelete():
    try:
        user_id = request.args.get('id')
        users_ref.document(user_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


#incomes CRUD

@api.route('/incomes/add', methods=['POST'])
def incomeCreate():
    try:
        validate(instance=request.json,schema=incomeSchema)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        incomes_ref.add(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error":"An Error Occured: {e}"}), 400

@api.route('/incomes', methods=['GET'])
def incomeRead():
    try:
        income_id=request.args.get('id')
        if income_id:
            result = incomes_ref.document(income_id).get()
            return jsonify(result.to_dict()),200
        else:
            result = []
            for income in incomes_ref.stream():
                res = income.to_dict()
                res['id']=income.id
                result.append(res)
            return jsonify(result),200
    except Exception as e:
        return f"An Error Ocurred: {e}"

@api.route('/incomes/update', methods=['POST', 'PUT'])
def incomeUpdate():
    try:
        validate(instance=request.json,schema=incomeSchemaUpdate)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        id = request.json['id']
        del request.json['id']
        incomes_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@api.route('/incomes/delete', methods=['GET', 'DELETE'])
def incomeDelete():
    try:
        income_id = request.args.get('id')
        incomes_ref.document(income_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


#expenses CRUD

@api.route('/expenses/add', methods=['POST'])
def expenseCreate():
    try:
        validate(instance=request.json,schema=expenseSchema)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(categories_ref,"category",request.json['category'],"user",request.json['user']):
        return jsonify({"error":"incorrect category parameter"}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        expenses_ref.add(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error":"An Error Occured: {e}"}), 400

@api.route('/expenses', methods=['GET'])
def expenseRead():
    try:
        expense_id=request.args.get('id')
        if expense_id:
            result = expenses_ref.document(expense_id).get()
            return jsonify(result.to_dict()),200
        else:
            result = []
            for expense in expenses_ref.stream():
                res = expense.to_dict()
                res['id']=expense.id
                result.append(res)
            return jsonify(result),200
    except Exception as e:
        return f"An Error Ocurred: {e}"

@api.route('/expenses/update', methods=['POST', 'PUT'])
def expenseUpdate():
    try:
        validate(instance=request.json,schema=expenseSchemaUpdate)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(categories_ref,"category",request.json['category'],"user",request.json['user']):
        return jsonify({"error":"incorrect category parameter"}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        id = request.json['id']
        del request.json['id']
        expenses_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@api.route('/expenses/delete', methods=['GET', 'DELETE'])
def expenseDelete():
    try:
        expense_id = request.args.get('id')
        expenses_ref.document(expense_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
#categories CRUD

@api.route('/categories/add', methods=['POST'])
def categoryCreate():
    try:
        validate(instance=request.json,schema=categorySchema)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        categories_ref.add(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error":"An Error Occured: {e}"}), 400

@api.route('/categories', methods=['GET'])
def categoryRead():
    try:
        category_id=request.args.get('id')
        if category_id:
            result = categories_ref.document(category_id).get()
            return jsonify(result.to_dict()),200
        else:
            result = []
            for category in categories_ref.stream():
                res = category.to_dict()
                res['id']=category.id
                result.append(res)
            return jsonify(result),200
    except Exception as e:
        return f"An Error Ocurred: {e}"

@api.route('/categories/update', methods=['POST', 'PUT'])
def categoryUpdate():
    try:
        validate(instance=request.json,schema=categorySchemaUpdate)
    except exceptions.ValidationError as e:
        print(e.message)
        return jsonify({"error":e.message}),400
    if validateParameter(users_ref,"email",request.json['user']):
        return jsonify({"error":"incorrect user parameter"}),400
    try:
        id = request.json['id']
        del request.json['id']
        categories_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@api.route('/categories/delete', methods=['GET', 'DELETE'])
def categoryDelete():
    try:
        category_id = request.args.get('id')
        categories_ref.document(category_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))

if __name__ == "__main__":
    api.run(threaded=True, host='0.0.0.0', port=port)