from flask import Flask, request

app = Flask(__name__)

@app.route('/process_content', methods=['POST'])
def process_content():
    data = request.json
    channel = data.get("channel")
    text = data.get("text")
    date = data.get("date")

    generated_post = f"Получено из {channel}:\n\n{text}\n\nДата: {date}"
    print(f"Сгенерированный пост: {generated_post}")
    return {"status": "success", "generated_post": generated_post}

if __name__ == '__main__':
    app.run(port=8000)