import fire, json
import http.client, urllib.request, urllib.parse, urllib.error, base64
basepath=os.path.dirname(os.path.realpath(__file__))
configpath=os.path.join(basepath,'Config.json')
class FacePI:

    def readConfig(self):
        if not os.path.exists(configpath):
            config=dict()
            config['api_key']="b9160fbd882f47bd821205a4bce64354"
            config['host']="eastasia.api.cognitive.microsoft.com"
            config['confidence']=0.6
            config['title']='鄭宇崴會甲你'
            config['personGroupName']='大甲鄭宇崴'
            config['personGroupId']='default+personGroupId'
            self.writeConfig(config)
        with open('Config.json','r',encoding='utf-8')as f:
            config = json.load(f)
        return config
    def writeConfig(self,config):
        with open('Config.json','w',encoding='utf-8')as f:
            json.dump(config,f)
    
    def setConfig(self):
        config=self.readConfig()
        print('[]裡面的都是鄭宇崴臭甲，按ENTER保持甲')
        api_key=input(f'甲你API_KEY[{config["api_key"]}]:')
        if api_key:config['api_key']=api_key
        title=input(f'甲你title[{config["title"]}]:')
        if title:config['title']=title
        self.writeConfig(config)
def detectLocalImage(self,imagepath):
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': self.readConfig()['api_key'],
    }

    params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
    #'recognitionModel': 'recognition_04',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_01',
    'faceIdTimeToLive': '86400',
    })
    print('imagepath=',imagepath)
    requestbody=open(imagepath,"rb").read()

    try:
        conn = http.client.HTTPSConnection(self.readConfig()['host'])
        conn.request("POST", "/face/v1.0/detect?%s" % params,requestbody, headers)
        response = conn.getresponse()
        data = response.read()
        json_face_detect=json.loads(str(data,'UTF-8'))
        print("dectedLocalImage.faces=",json_face_detect)
        conn.close()
        print("dectetLocalImage:",f"{imagepath} 偵測到{len(json_face_detect)} 個人")
        return json_face_detect
    except Exception as e:
        print("[Errno {0}]連線失敗!請檢查鄭宇崴的後庭。 {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    fire.Fire(FacePI)