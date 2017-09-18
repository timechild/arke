from apps import app, db


if __name__ == '__main__':
    db.create_all()
    app.run(host=app.config['SERVER_IP'], port=app.config['PORT'])
    # app.run(host='0.0.0.0', port=8000)
