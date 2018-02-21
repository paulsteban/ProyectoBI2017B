'''


 QUITO,Guayaquil,Cuenca
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = 'GAUJHG84CKoQX1wS5D34jni4C'
csecret = 'sAyzUb8mNG4HK43w6GI0Fv2nQhEJoTM54JH4UgmlU3MhccSkXTJA47Ho0Kff0E'
atoken = '604030610-drVVnbs5nKvzMg4D4D$"dHbaW3rZVxi2Qxzjl8aaZmsWUvb'
asecret = 'xQANa0OzoGKfD4Dr4cOsBcRaILtxg3dc0ksG$FF$"D3GgxPMTr5qRlS81Jc'

class listener(StreamListener):


    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) + "=>" + str(data)
        except:
            print "Already exists"
            pass
        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


URL='localhost'
db_name = 'guayas'

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/') #('http://245.106.43.184:5984/') poner la url de su base de datos


try:
    print db_name
    db = server['consulta']
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


'''===============LOCATIONS==============QUITO,Guayaquil,Cuenca'''

twitterStream.filter(locations=[-80.566575,-2.930232, -79.182298,-1.662356])  #QUITO
#Guayaquil twitterStream.filter(locations=[-79.850098-2.282060, -80.078751, -2.026808])
#Cuenca twitterStream.filter(locations=[-78.927926, -2.922271, -79.056500, -2.851636])
