from flask import Flask #載入flask
from flask import request #載入請求(request)物件
from flask import redirect #載入重新導向(redirect)物件
from flask import render_template #載入樣板(render_templat)物件
from flask import session #載入session物件
#from flask import list
import json

#static_folder="static" 存取圖片資料夾 static_url_path="/" 根目錄下
app=Flask(__name__,static_folder="static",static_url_path="/")
#設定session密鑰
app.secret_key="any string"
@app.route("/en")
def english():
    return json.dumps({"status":"ENGLISH",
                "text":"HELLO"})
@app.route("/zh")
def chines():
    return json.dumps({"status":"中文",
                "text":"您好" },ensure_ascii=False)#不要使用ASCII

#一般使用GET 就不用特別寫 method 路徑 / 對應的路由
@app.route("/")
def index():
     
     return render_template("index",web_name="公司",username="榮峯")#template/index 路徑位置
     #return redirect("/data")#首頁=>導向中文
     print("請求方法",request.method)
     print("通訊協定",request.scheme)
     print("主機名稱",request.host) 
     print("路徑",request.path)      
     print("完整網址",request.url)                              
     print("瀏覽器and OS SYSTEM",request.headers.get("user-agent"))        
     print("語言偏好",request.headers.get("accept-language"))        
     print("引薦網址",request.headers.get("referrer"))

@app.route("/show",methods=["GET"])     
def show():
    #name=request.args.get("n","no input")
    input=request.args.get("n","no input")
    #session["欄位名"]=資料
    session["username"]=input
    return "測試GET:"+input

@app.route("/show2",methods=["GET"])     
def show():
    #name=request.args.get("n","no input")
    input=request.args.get("n","no input")
    #session["欄位名"]=資料
    a=session["username"]
    return "測試GET:"+input+"上次輸入的"+a

#使用POST method 路徑 / 對應的路由
@app.route("/show_post",methods=["POST"])     
def show_post():
    #post method 接收輸入值
    input=request.form["data"]
    #運用在機敏資訊(ex:帳號or密碼)
   
    return "測試POST"

#當對應到/page路由時會進入請假系統載入圖片可用縮寫 
# http://127.0.0.1:5000/1111.png/    
@app.route("/page")     
def page():
    return render_template("page",web_name="公司",username="榮峯")

@app.route("/data")
def index2():
    lang=request.headers.get("accept-language")
    print("語言",lang)        
    print(lang)
    if lang.startswith("zn"):
        return redirect("/zh")#首頁=>導向中文/zh路由
    else:    
        return redirect("/en")#首頁=>導向/en路由
        
    
#建立路徑/getSum 對應的處理含式
#利用要求字串(Query string) 提供彈性 /getSum?min=最小數字&max=最大數字
#/min+(min+1)+(min+2)+...+max
@app.route("/getSum")
def getSum():#ex1+2+3..+max
    input_max_number=request.args.get("max",'no_input')#沒輸入顯示no input
    #print("input_str :",input_str)
    input_min_number=request.args.get("min",'no_input')#沒輸入顯示no input
    if input_max_number=="no_input"or input_min_number=="no_input":
        return "must have input number max number and min number"
    else:
        input_max_number=int(input_max_number)
        input_min_number=int(input_min_number)
    #print("input_str :",input_str)
        result=0
    for n in range(input_min_number,input_max_number+1):
        result+=n
    return "結果: "+str(result)    
     #data=request.args.get("max",None)
     #return data
app.run(port=5000)