import pymongo 
from datetime import datetime
from flask import Flask,request
  
app = Flask(__name__)


@app.route('/reicha',methods=['POST'])
def entry_isi():
  dt = datetime.now()

  client = pymongo.MongoClient("mongodb+srv://reicha_1:smaciho@cluster0.x5bxp.mongodb.net/?retryWrites=true&w=majority")
  db = client['tugas-week-8'] 
  my_collections = db['tugas'] 

  kecepatan = request.args.get('kecepatan') 
  latitude = request.args.get('latitude')
  longitude = request.args.get('longitude')

  tugas = {'kecepatan': kecepatan,
         'latitude' : latitude,
         'longitude' : longitude,
         'timestamp' : dt
          }
  
  results = my_collections.insert_many([tugas])
  return ('data sudah disimpan diMongoDB')  
  

if __name__ == '__main__':
        app.run(debug=True)