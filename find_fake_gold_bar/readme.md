### Summary
Web Automation Framework and find_fake_bar test

There are 2 algorithms: generic and 9 bar specific
```
test_generic_algorithm
test_9_bars_algorithm
```

### Requirements
Python 3.7

Dependencies: selenium

### Set Up
Download Chromedrive executable
https://sites.google.com/a/chromium.org/chromedriver/home

put the executable to find_fake_gold_bar directory
or specify path to the executable in cfg.py
```buildoutcfg
chromedriver_path = "C:/your/path"
```

Webpage URL: http://ec2-54-208-152-154.compute-1.amazonaws.com/

you can change the URL in cfg.py
```buildoutcfg
scale_page_url = "http://ec2-54-208-152-154.compute-1.amazonaws.com/"
```

Install the requirements:
```buildoutcfg
cd find_fake_gold_bar
pip install --upgrade -r .\requirements.txt
```

Install the package:
```buildoutcfg
python setup.py install
```

or use develop if you planning to modify the package:
```buildoutcfg
python setup.py develop
```

Run the tests:
```buildoutcfg
python tests\test_find_fake_bar.py
```
You can run individual test like this:
```buildoutcfg
python tests\test_find_fake_bar.py FindFakeBarTests.test_generic_algorithm
python tests\test_find_fake_bar.py FindFakeBarTests.test_9_bars_algorithm
```

### Tests run example:
```
INFO:root:Left: [0, 1, 2, 3] Right: [4, 5, 6, 7]
INFO:root:[0,1,2,3] < [4,5,6,7]
INFO:root:Left: [0, 1] Right: [2, 3]
INFO:root:[0,1] < [2,3]
INFO:root:Left: [0] Right: [1]
INFO:root:[0] > [1]
INFO:root:Fake bar: 1
.

INFO:root:Left: [0, 1, 2, 3] Right: [4, 5, 6, 7]
INFO:root:[0,1,2,3] > [4,5,6,7]
INFO:root:Left: [4, 5] Right: [6, 7]
INFO:root:[4,5] > [6,7]
INFO:root:Left: [6] Right: [7]
INFO:root:[6] > [7]
INFO:root:Fake bar: 7
.
----------------------------------------------------------------------
Ran 2 tests in 11.773s

OK
```
