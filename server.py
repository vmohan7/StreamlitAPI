from flask import Flask, request, jsonify, send_from_directory
import os


app = Flask(__name__)
port = os.environ.get('PORT', 3000)

# Serve static files from the 'public' directory
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def send_public(path):
    public_dir = os.path.join(app.root_path, 'public')
    if path == '':
        path = 'index.html'
    return send_from_directory(public_dir, path)

# POST method route
@app.route('/suggestion', methods=['POST'])
async def suggestion():
    board = request.json.get('board')  # Getting the board state from the request body
    moves = request.json.get('moves')  # Getting the moves from the request body

    print(f"Suggestion for {board} with {moves}", flush=True)

    answer = await getAnalysis(board)
    return jsonify(message=answer)

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=port , debug=True, use_reloader=False)

