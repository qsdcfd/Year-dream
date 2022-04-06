#Flask:framwork, jsonify: call json, render_template : call template
#routing and rendering 실습
#route(): 안에 있는 것은 가고 싶은 링크이다.
#routing : 사용자의 접속 경로를 지정하는 거
#rendering:준비된 페이지를 제공하는 행위 or 페이지 내용 읽기
from flask import Flask, jsonify, render_template 
import requests #API사용하려고 할 때 부르는 라이브러리



app = Flask(__name__) 


@app.route('/') #메인페이지 @:decorator
def index():
  return render_template('index.html') #html내용 연결


@app.route('/posts') #링크타고 가면 json파일 내용이 나온다
def show_posts():
  response = requests.get("https://jsonplaceholder.typicode.com/posts") #외부 api 가져오기
  to_serve = response.json() #json파일로 가져오기
  return jsonify(to_serve)

  

@app.route('/todos') #마찬가지이다
def show_todos():
  return "This is todos"

@app.route('/quote/<string:name>') #이름을 넣어서 그 이름을 출력하기
def show_quote(name=None):
  return "This is quote {}".format(name)
  
if __name__ =='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
  #프로젝트 첫 시작시 pip install flask
  #shell에서 app 시작: $python main.py