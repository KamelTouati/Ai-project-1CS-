from flask import Flask, render_template, request

app = Flask(__name__)

# Set debug mode to True
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tictactoe-game')
def tictactoe():
    return render_template('TicTacToe.html')

@app.route('/expert-system', methods=['GET', 'POST'])
def expertsystem():
    if request.method == 'POST':
        username = request.form['username']
        operatingSystem = request.form['operatingSystem']
        softwareType = request.form['softwareType']
        softwarePrice = request.form['softwarePrice']
        print('username: ', username)
        print('operatingSystem: ', operatingSystem)
        print('softwareType: ', softwareType)
        print('softwarePrice: ', softwarePrice)
        if not username:
            error = 'Username is required.'
        elif not operatingSystem:
            error = 'operatingSystem is required.'
        elif not softwareType:
            error = 'softwareType is required.'
        elif not softwarePrice:
            error = 'softwarePrice is required.'
        else:
            return 'successful!'
        
        return render_template('ExpertSystem.html', error=error)
    
    return render_template('ExpertSystem.html')

if __name__ == '__main__':
    app.run()