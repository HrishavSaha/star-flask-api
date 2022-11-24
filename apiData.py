from flask import Flask, jsonify, request
import pandas as pd

df = pd.read_csv('shortlisted_data.csv')

app = Flask(__name__)
@app.route('/star')
def planet_data():
    name = request.args.get('name')
    star_data = list(df[df['name'] == name].iloc[0])
    return jsonify({
        'data':star_data,
        'message':"success"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)