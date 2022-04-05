from flask import Flask
import subprocess
from osgeo import gdal
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    demn = gdal.Translate("{}/sorted_xyz.xyz".format(outf), "a.tif".format(outf))
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#def test1(outf):
        #data = pd.read_csv(inf)
        #data = data.sample(frac = 0.1)
        #data = data.sort_values(by = [data.columns[1],data.columns[0]], ascending = [False,True])
        #data.to_csv("{}/dfn.xyz".format(outf), index = False, header = None, sep = " ")
        #demn = gdal.Translate("{}/sample.tif".format(outf), "sorted_xyz.xyz".format(outf))

outf = "/app"
#test1(outf)