import os
import sys
import time
import datetime
from PIL import ImageGrab

out = '.'
intv = 10

def grab(fpath):
    im = ImageGrab.grab()
    im.save(fpath,'jpeg')

def schedule():
    day = datetime.datetime.now().strftime('%Y%m%d')
    cur = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    fdir = os.path.join(out, day)
    fname = cur + '.jpg'
    if not os.path.exists(fdir):
        os.makedirs(fdir)
    grab(os.path.join(fdir, fname))

def run():
    while True:
        dt = time.time()
        schedule()
        dt = time.time() - dt
        if dt < intv:
            time.sleep(intv - dt)

if __name__ == '__main__':
    out = sys.argv[1]
    intv = int(sys.argv[2])
    print '[INFO] out=', out
    print '[INFO] intv=', intv
    run()
