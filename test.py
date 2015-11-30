import ConfigParser, logging, datetime, os, collections
import mediacloud
import simplejson as json
from io import StringIO


x = 3

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

keywords = 'cats'
dateOne = datetime.date( 2014, 10, 10)
dateTwo = datetime.date( 2015, 10, 10)
results = mc.sentenceCount(keywords,solr_filter=[mc.publish_date_query( dateOne , dateTwo ),'media_sets_id:1' ], split=True,split_start_date = str(dateOne),split_end_date=str(dateTwo))
#print results

count = results['count']
results = results['split']



print results