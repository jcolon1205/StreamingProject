from flask import Flask,request,render_template,Response
import cv2



app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def loginPage():
    return render_template('login.html')
database={'jcolon1205':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=name1)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/LiveStream/", methods=['POST'])
def move_LiveStream():
    #Moving forward code
    LiveStream_message = "Moving LiveStream..."
    return render_template('LiveStream.html', LiveStream_message=LiveStream_message)

@app.route("/Helicopter/", methods=['POST'])
def move_Helicopter():
    Helicopter_message = "Moving Helicopter..."
    return render_template('Helicopter.html', Helicopter_message=Helicopter_message)
    

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)