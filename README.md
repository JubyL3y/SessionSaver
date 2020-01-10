# About SessionSaver
A very small utility written in Python 3 that allows you to keep your sessions in a state of life by simulating user actions.

# Installation
```
git clone https://github.com/JubyL3y/SessionSaver.git
```

# Dependencies
SessionSaver depends on the Python3, requests, beautifulsoup4 and lxml.

You can install it with command:
```
pip install -r requirements.txt
```
or if you have python2 and python3
```
pip3 install -r requirements.txt
```
# Usage
```
sessionsaver.py [-h] --cookie COOKIE [--base_url B_URL]
                       [--jumping_urls J_URLS [J_URLS ...]] [--user_agent UA]
                       [--count COUNT] [--delay DELAY]

optional arguments:
  -h, --help            show this help message and exit
  --cookie COOKIE       Cookie for your session.
  --base_url B_URL      Site URL.
  --jumping_urls J_URLS [J_URLS ...] Urls for jumping
  --user_agent UA       Your own UserAgent. Default: "SessionSaver/0.0.1"
  --count COUNT         Maximum number of links for base address. Must be greater than 0. Default 5.
  --delay DELAY         Pause time between requests. Must be 0 or greater. Default 30.
```

# Examples
Caution: Use Python 3
### Simple run on wikipedia.org
```
python sessionsaver.py --cookie "SOME_COOKIE" --base_url https://www.wikipedia.org/
```

### Run on specific URL's
```
python sessionsaver.py --cookie "SOME_COOKIE" --jumping_urls "https://en.wikipedia.org/wiki/Ham_Wall" "https://en.wikipedia.org/wiki/Cognitive_inertia"
```

### Run with specific User Agent, Delay and URL's count:
```
python sessionsaver.py --cookie "SOME_COOKIE" --base_url https://www.wikipedia.org/ --user_agent "SPECIFIC USER AGENT" --count 10 --delay 12
```