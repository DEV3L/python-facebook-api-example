HELLO_WORLD_MESSAGE = 'Hello world! Facebook Api Example'
#
#
# def get_message():
#     return HELLO_WORLD_MESSAGE
#
#
# def post_hello_worl():
#     print(get_message())
#

import facebook
from facebook_api_example.app.markov_sentence_generator import buildMapping, genSentence, wordlist

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "value",  # Step 1
    "access_token" : "value"   # Step 3
    }

  api = get_api(cfg)

  filename = "../scrubbed_file.txt"
  markovLength = 3

  # if len (sys.argv) == 3:
  #     markovLength = int(sys.argv [2])

  buildMapping(wordlist(filename), markovLength)
  msg = genSentence(markovLength)

  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
    main()
