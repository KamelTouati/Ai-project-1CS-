from flask import Flask, render_template, request



app = Flask(__name__)


System = [
    "Windows",
    "Linux",
    "MacOS"
]

Category = [
    "TextEditor",
    "ProjectManagement",
    "ComptLog",
    "SecurityLog",
    "Design",
    "RelationClient",
    "DevLog",
    "Conference",
]

Price = [
    "Gratuit",
    "Payant"
]

#app.config['ENV'] = 'development'
app.config['Debug'] = True
#app.config['TESTING'] = True

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
        list = {
            'username': username,
            'operatingSystem': operatingSystem,
            'softwareType': softwareType,
            'softwarePrice': softwarePrice,
        }
        print('username: ', username)
        print('operatingSystem: ', operatingSystem)
        print('softwareType: ', softwareType)
        print('softwarePrice: ', softwarePrice)
        if not username:
            error = 'Username is required.'
        if not operatingSystem:
            error = 'operatingSystem is required.'
        elif not softwareType:
            error = 'softwareType is required.'
        elif not softwarePrice:
            error = 'softwarePrice is required.'
            return render_template('ExpertSystem.html', error=error)
        # data = recommendation_system([f"System({operatingSystem})",f"Price({softwarePrice})",f"Category({softwareType})"])

        # results = []
        # for dt in data :
        #     # print(dt)
        #     results.append(dt[y])
        # print(results)
        return render_template('ExpertSystem.html', list=list, System=System, Category=Category, Price=Price)
    return render_template('ExpertSystem.html', System=System, Category=Category, Price=Price)
    


if __name__ == '__main__':
    app.run()