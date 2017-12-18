import os
import json
from flask import Flask


def create_app():
    app = Flask('rmon')
    # print(app.config)
    file = os.environ.get('RMON_CONFIG') # 需在shell里export RMON_CONFIG='.../rmon_config.json'绝对路径
    # print(file)
    content =''
    try:
        with open(file) as f:
            for l in f:
                l = l.strip()
                if l.startswith('#'):
                    continue
                else:
                    content += l
    except IOError:
        return app
    
    try:
        data = json.loads(content)
        # print(data)
    except:
        print('error')
        return app
    
    for key in data:
        app.config[key.upper()] = data.get(key)
    
    return app


# if __name__ == '__main__':
#     create_app()
