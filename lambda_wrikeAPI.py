import json
import urllib.request
from pprint import pprint

permanent_token='こちらにWrikeより発行した永続トークンを入力してください replace the parmanent token created in Wrike'
url = 'https://www.wrike.com/api/v4/tasks'
header ={ 'Authorization': 'bearer '+ permanent_token}
#method = 'Get'

def lambda_handler(event, context):
    req=urllib.request.Request(url, headers=header)
    
    with urllib.request.urlopen(req) as res:
    # resは http.client.HTTPResponse
        body = json.loads(res.read().decode('utf8')) # レスポンスボディ response body
        headers = res.getheaders() # ヘッダー(dict) header(dict)
        status = res.getcode() # ステータスコード status code
        #pprint(header)
        #pprint(status)
        pprint(body)
