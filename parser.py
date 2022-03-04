import json
import requests
import sys
import re
from datetime import datetime

TODAY = datetime.now()

METRICS_SONAR = ['files',
               'functions',
               'complexity',
               'comment_lines_density',
               'duplicated_lines_density',
               'coverage',
               'ncloc',
               'tests',
               'test_execution_time',
               'test_errors',
               'test_failures', 
               'security_rating',
               'reliability_rating']

BASE_URL = 'https://sonarcloud.io/api/measures/component_tree?component='

if __name__ == '__main__':
    
    REPO = sys.argv[1] 'fga-eps-mds_2021.2-SysArq-Archives'

    # Get metrics from Sonar Cloud
    response = requests.get(f'{BASE_URL}{REPO}&metricKeys={",".join(METRICS_SONAR)}&ps=500')
    j = json.loads(response.text)

    path_time =  # caminho para o arquivo
    with open(path_time, 'r') as f:
        json_time = json.loads(f.read())

    file_path = f'./{REPO}-{TODAY.strftime("%m-%d-%Y-%H-%M")}.json'

    for component in j['components']:
        component['measures'].append({ 'metric': 'test', 'value': 1 })
        component['measures'].append({ 'metric': 'test_execution_time', 'value': json_time['duration'] })

    with open(file_path, 'w') as fp:
        fp.write(json.dumps(j))
        fp.close()