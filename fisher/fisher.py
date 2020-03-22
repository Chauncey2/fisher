from app import create_app

__author__ = '橘子'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUGE'], port=81)
