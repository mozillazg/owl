# owl

A tiny Python APM agent（一个玩具式的 Python 探针）.


```
$ python main.py python hello_timer.py
usercustomize  find_module
hello  find_module
hello  load_module
wrap_module
sleep 3
hello.hello2 spend 3.005079984664917 s
```
