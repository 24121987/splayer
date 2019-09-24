from flask import Flask, jsonify,request
from reverse_image_file import ReverseImageSearch


# Initaialize the Flask App
app = Flask(__name__)

ris= ReverseImageSearch()

# Generate title name
@app.route('/path', methods=['POST'])
def fetch_title():
    try:
        req_data = request.get_json()
        print("==============================")
        print(len(req_data['image_path']))
        if len(req_data['image_path']) <= 0:  # The variable
            response = jsonify(message="Invalid Parameters Passed")
            response.status_code = 501
            return response


        # convert base64 image to images form
        image_path = ris.decode_image(req_data['image_path'])
        print("===========================================")
        print(image_path)
        output = ris.fetch_title(image_path)
        return jsonify({"TitleName": output})
    except:
        response = jsonify(message="Invalid API Name passed!")
        response.status_code = 501
        return response


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", debug=True, port=8080)