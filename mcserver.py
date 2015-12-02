import ConfigParser, logging, datetime, os, collections
from flask import Flask, render_template, request
import mediacloud
import simplejson as json


CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = ConfigParser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
log_file_path = os.path.join(basedir,'logs','mcserver.log')
logging.basicConfig(filename=log_file_path,level=logging.DEBUG)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
mc = mediacloud.api.MediaCloud( config.get('mediacloud','api_key') )
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("search-form.html")

@app.route("/search",methods=['POST'])
def search_results():
    keywords = request.form['keywords']
    now = datetime.datetime.now()
    dateOne = datetime.date( 2014, 10, 10)
    dateTwo = datetime.date( 2015, 10, 10)
    
    results = mc.sentenceCount(keywords,solr_filter=[mc.publish_date_query( dateOne , dateTwo ),'media_sets_id:1' ], split=True,split_start_date = str(dateOne),split_end_date=str(dateTwo))
    
    # THIS WILL BE MORE SIMPLE BUT HOW CAN I PRINT THE VALUES W/O KEYS ?????
    #results = json.dumps(results['split'], sort_keys=True, indent=1 * ' ')
    #print results
    
    count = results['count']
    results = results['split']


    sorting = collections.OrderedDict(sorted(results.items()))

    results = sorting.values()[:-3]
    
    return render_template("search-results.html", 
        keywords=keywords, sentenceCount=count, data=results )


if __name__ == "__main__":
    app.debug = True
    app.run()


























