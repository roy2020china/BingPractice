# build a program that will open a url every 2 hours for 3 times

# #
# # Step 1 open a url
# import webbrowser
# webbrowser.open('http://www.sina.com.cn')
#
# # Step 2 every 2 hours  - 2*60*60 in production. For testing purpose, we leave 10 here.
# import time
# time.sleep(10)
#
# # Step 3  . Repeat, for 3 times
# i = 0
# for i in range(3):
#     #do sth
#     i =+ 1

# Step 1 + 2 +3
import webbrowser
import time

i = 0
for i in range (3):
    time.sleep(10)
    webbrowser.open('http://www.sina.com.cn')
    i += 1
