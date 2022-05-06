from flask import Flask,request
import post_image_base64 as p_img
import image_similarity as sim

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
	img_name = request.form['img_base64']
	similar = sim.Similarity()
	res = similar.black_white_result(img_name)
	return str(res)

@app.route('/similar',methods=['POST'])
def similar():
	print('[INFO]--[test]--[FUNCTION]')
	img_name = request.form['img_name']
	result = p_img.results(img_name)
	return str(result)

if __name__ == '__main__':
	app.run()