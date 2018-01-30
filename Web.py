from flask import Flask, request, render_template
from Analytics import run_a, get_status
import glob
import os
import shutil
import time

app = Flask(__name__)

@app.route('/')
def whatisthis():
    return render_template('whatisthis.html')

@app.route('/analytics', methods = ['GET', 'POST'])
def analytics():
    if request.method == 'POST':
        params = [ float(param_string) for param_string in request.form.getlist('cut[]') ]
        print(params[-4])
        #params = [0, 0, 200, 1, 1, 0, 0, 0, 0, 0, 0, 25, 0, 0, 9, 0, 9, 0, 0, 200, float(request.form.getlist('cut[]')[0]), 0, 0, 0]
        for oldHistogram in glob.glob("static/histograms/*.gif"):
            os.remove(oldHistogram)
        for oldHistogram in glob.glob("Output/*.gif"):
            os.remove(oldHistogram)
        run_a(params)
        while not get_status():
            pass
        return render_template('analytics.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])
    else:
        return render_template('analytics.html', histograms=[])

@app.route('/histogram', methods = ['GET', 'POST'])
def histogram():    
    return render_template('histogram.html')

if __name__ == '__main__':
    app.run(debug=True)