from flask import Flask,request
import cv2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/test',methods=['POST'])
def test():
	print('[INFO]--[test]--[FUNCTION]')
	test = request.form['test']
	return "Test Başarılı : " + test

@app.route('/img',methods=['POST'])
def img():
	print('[INFO]--[test]--[FUNCTION]')
	img_name = request.form['img_name']
	img = cv2.imread(img_name)
	return str(img)

if __name__ == '__main__':
	app.run()