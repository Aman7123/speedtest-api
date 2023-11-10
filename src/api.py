from flask import Flask, jsonify
import speedtest
from threading import Thread
from time import sleep

app = Flask(__name__)

# This dictionary will act as a simple cache.
cache = {
    'last_result': None,
    'last_updated': None
}

def run_speedtest():
    while True:
        sleep_duration = 3600
        try:
            # Run the speedtest
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            s.upload()
            s.results.share()

            results_dict = s.results.dict()

            # Update the cache
            cache['last_result'] = results_dict
            cache['last_updated'] = s.results.timestamp
            
        except Exception as e:
            print(f"Error running speed test: {e}")
            # If an error occurred, decrease the sleep duration
            sleep_duration = 30

        # Wait before the next test
        sleep(sleep_duration)

@app.route('/speedtest', methods=['GET'])
def get_speedtest():
    # Return the cached results as JSON
    return jsonify(cache)

if __name__ == '__main__':
    # Start the speedtest thread
    Thread(target=run_speedtest, daemon=True).start()

    # Run the Flask app on port 8080
    app.run(debug=True, host='0.0.0.0', port=8080)
    