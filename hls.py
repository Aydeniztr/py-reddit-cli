from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import sys
import shutil
import os
import tempfile
import math

print('\u001b[2J')

about = '''
\033[31m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ===========================================================
░░░░░░░░░░░░░░░░░░░░░░░░████░░░░   
░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░   
░░░░░░░░░░░░░░░█████████░░░░█░░░   author: Ahmet Yigit AYDENIZ
░░░░░░░░░░░░░░░██░░░░░░█░░░░█░░░   
░░░░░░░░░░░░░░░██░░░░░░░████░░░░   
░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░   command line interface to view reddit
░░░░░░░░░░░░░██████░░░░░░░░░░░░░   download videos,gifs,pictures
░░░█████░░███░░░░░░███░░█████░░░
░░█░░░████░░░░░░░░░░░░████░░░█░░   the commandline interface not done but
░█░░░█░░░░░░░░░░░░░░░░░░░░█░░░█░	  you can downlod every atteched file to a reddit post
░█░██░░░░░███░░░░░░███░░░░░██░█░
░░██░░░░░░███░░░░░░███░░░░░░██░░   like this:
░░░█░░░░░░░░░░░░░░░░░░░░░░░░█░░░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░█░░░   >> hls <url>
░░░░█░░░░░░█░░░░░░░░█░░░░░░█░░░░
░░░░░█░░░░░░████████░░░░░░█░░░░░
░░░░░░███░░░░░░░░░░░░░░███░░░░░░   to see this page:
░░░░░░░░░████░░░░░░████░░░░░░░░░
░░░░░░░░██░░░██████░░░██░░░░░░░░
░░░░░░░█░█░░░░░░░░░░░░█░█░░░░░░░   >> hls --help
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░   to make a search and see the results in terminal
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░   >> hls
░░░░░░░█░█░░░░░░░░░░░░█░█░░░░░░░
░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░
░░░░░░░░░█░░░░░░░░░░░░█░░░░░░░░░   github  : https://github.com/Aydeniztr
░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░
░░░░░░░░████░░░░░░░░████░░░░░░░░   website : https://www.aydeniz.tk/
░░░░░░░█░░░░█░░░░░░█░░░░█░░░░░░░
░░░░░░█░░░░░░█░░░░█░░░░░░█░░░░░░   chat    : https://www.aydeniz.tk/chat.html
░░░░░░████████████████████░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ===========================================================
\033[0m
'''

PY3K = sys.version_info >= (3, 0)
if PY3K:
  import urllib.request as ulib
  import urllib.parse as urlparse
else:
  import urllib as ulib
  import urlparse

def win32_unicode_console():
    import codecs
    from ctypes import WINFUNCTYPE, windll, POINTER, byref, c_int
    from ctypes.wintypes import BOOL, HANDLE, DWORD, LPWSTR, LPCWSTR, LPVOID

    original_stderr = sys.stderr

    # Output exceptions in this code to original_stderr, so that we can at least see them
    def _complain(message):
        original_stderr.write(message if isinstance(message, str) else repr(message))
        original_stderr.write('\n')

    codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

    try:
        GetStdHandle = WINFUNCTYPE(HANDLE, DWORD)(("GetStdHandle", windll.kernel32))
        STD_OUTPUT_HANDLE = DWORD(-11)
        STD_ERROR_HANDLE = DWORD(-12)
        GetFileType = WINFUNCTYPE(DWORD, DWORD)(("GetFileType", windll.kernel32))
        FILE_TYPE_CHAR = 0x0002
        FILE_TYPE_REMOTE = 0x8000
        GetConsoleMode = WINFUNCTYPE(BOOL, HANDLE, POINTER(DWORD))(("GetConsoleMode", windll.kernel32))
        INVALID_HANDLE_VALUE = DWORD(-1).value

        def not_a_console(handle):
            if handle == INVALID_HANDLE_VALUE or handle is None:
                return True
            return ((GetFileType(handle) & ~FILE_TYPE_REMOTE) != FILE_TYPE_CHAR
                    or GetConsoleMode(handle, byref(DWORD())) == 0)

        old_stdout_fileno = None
        old_stderr_fileno = None
        if hasattr(sys.stdout, 'fileno'):
            old_stdout_fileno = sys.stdout.fileno()
        if hasattr(sys.stderr, 'fileno'):
            old_stderr_fileno = sys.stderr.fileno()

        STDOUT_FILENO = 1
        STDERR_FILENO = 2
        real_stdout = (old_stdout_fileno == STDOUT_FILENO)
        real_stderr = (old_stderr_fileno == STDERR_FILENO)

        if real_stdout:
            hStdout = GetStdHandle(STD_OUTPUT_HANDLE)
            if not_a_console(hStdout):
                real_stdout = False

        if real_stderr:
            hStderr = GetStdHandle(STD_ERROR_HANDLE)
            if not_a_console(hStderr):
                real_stderr = False

        if real_stdout or real_stderr:
            WriteConsoleW = WINFUNCTYPE(BOOL, HANDLE, LPWSTR, DWORD, POINTER(DWORD), LPVOID)(("WriteConsoleW", windll.kernel32))

            class UnicodeOutput:
                def __init__(self, hConsole, stream, fileno, name):
                    self._hConsole = hConsole
                    self._stream = stream
                    self._fileno = fileno
                    self.closed = False
                    self.softspace = False
                    self.mode = 'w'
                    self.encoding = 'utf-8'
                    self.name = name
                    self.flush()

                def isatty(self):
                    return False

                def close(self):
                    # don't really close the handle, that would only cause problems
                    self.closed = True

                def fileno(self):
                    return self._fileno

                def flush(self):
                    if self._hConsole is None:
                        try:
                            self._stream.flush()
                        except Exception as e:
                            _complain("%s.flush: %r from %r" % (self.name, e, self._stream))
                            raise

                def write(self, text):
                    try:
                        if self._hConsole is None:
                            if not PY3K and isinstance(text, unicode):
                                text = text.encode('utf-8')
                            elif PY3K and isinstance(text, str):
                                text = text.encode('utf-8')
                            self._stream.write(text)
                        else:
                            if not PY3K and not isinstance(text, unicode):
                                text = str(text).decode('utf-8')
                            elif PY3K and not isinstance(text, str):
                                text = text.decode('utf-8')
                            remaining = len(text)
                            while remaining:
                                n = DWORD(0)
                                # There is a shorter-than-documented limitation on the
                                # length of the string passed to WriteConsoleW (see
                                # <http://tahoe-lafs.org/trac/tahoe-lafs/ticket/1232>.
                                retval = WriteConsoleW(self._hConsole, text, min(remaining, 10000), byref(n), None)
                                if retval == 0 or n.value == 0:
                                    raise IOError("WriteConsoleW returned %r, n.value = %r" % (retval, n.value))
                                remaining -= n.value
                                if not remaining:
                                    break
                                text = text[n.value:]
                    except Exception as e:
                        _complain("%s.write: %r" % (self.name, e))
                        raise

                def writelines(self, lines):
                    try:
                        for line in lines:
                            self.write(line)
                    except Exception as e:
                        _complain("%s.writelines: %r" % (self.name, e))
                        raise

            if real_stdout:
                sys.stdout = UnicodeOutput(hStdout, None, STDOUT_FILENO, '<Unicode console stdout>')
            else:
                sys.stdout = UnicodeOutput(None, sys.stdout, old_stdout_fileno, '<Unicode redirected stdout>')

            if real_stderr:
                sys.stderr = UnicodeOutput(hStderr, None, STDERR_FILENO, '<Unicode console stderr>')
            else:
                sys.stderr = UnicodeOutput(None, sys.stderr, old_stderr_fileno, '<Unicode redirected stderr>')
    except Exception as e:
        _complain("exception %r while fixing up sys.stdout and sys.stderr" % (e,))


# --- helpers ---

def to_unicode(filename):
    """:return: filename decoded from utf-8 to unicode"""
    #
    if PY3K:
        # [ ] test this on Python 3 + (Windows, Linux)
        # [ ] port filename_from_headers once this works
        # [ ] add test to repository / Travis
        return filename
    else:
        if isinstance(filename, unicode): 
            return filename
        else:
            return unicode(filename, 'utf-8')

def filename_from_url(url):
    """:return: detected filename as unicode or None"""
    # [ ] test urlparse behavior with unicode url
    fname = os.path.basename(urlparse.urlparse(url).path)
    if len(fname.strip(" \n\t.")) == 0:
        return None
    return to_unicode(fname)

def filename_from_headers(headers):
    """Detect filename from Content-Disposition headers if present.
    http://greenbytes.de/tech/tc2231/

    :param: headers as dict, list or string
    :return: filename from content-disposition header or None
    """
    if type(headers) == str:
        headers = headers.splitlines()
    if type(headers) == list:
        headers = dict([x.split(':', 1) for x in headers])
    cdisp = headers.get("Content-Disposition")
    if not cdisp:
        return None
    cdtype = cdisp.split(';')
    if len(cdtype) == 1:
        return None
    if cdtype[0].strip().lower() not in ('inline', 'attachment'):
        return None
    # several filename params is illegal, but just in case
    fnames = [x for x in cdtype[1:] if x.strip().startswith('filename=')]
    if len(fnames) > 1:
        return None
    name = fnames[0].split('=')[1].strip(' \t"')
    name = os.path.basename(name)
    if not name:
        return None
    return name

def filename_fix_existing(filename):
    """Expands name portion of filename with numeric ' (x)' suffix to
    return filename that doesn't exist already.
    """
    dirname = u'.'
    name, ext = filename.rsplit('.', 1)
    names = [x for x in os.listdir(dirname) if x.startswith(name)]
    names = [x.rsplit('.', 1)[0] for x in names]
    suffixes = [x.replace(name, '') for x in names]
    # filter suffixes that match ' (x)' pattern
    suffixes = [x[2:-1] for x in suffixes
                   if x.startswith(' (') and x.endswith(')')]
    indexes  = [int(x) for x in suffixes
                   if set(x) <= set('0123456789')]
    idx = 1
    if indexes:
        idx += sorted(indexes)[-1]
    return '%s (%d).%s' % (name, idx, ext)

def get_console_width():
    """Return width of available window area. Autodetection works for
       Windows and POSIX platforms. Returns 80 for others

       Code from http://bitbucket.org/techtonik/python-pager
    """

    if os.name == 'nt':
        STD_INPUT_HANDLE  = -10
        STD_OUTPUT_HANDLE = -11
        STD_ERROR_HANDLE  = -12

        # get console handle
        from ctypes import windll, Structure, byref
        try:
            from ctypes.wintypes import SHORT, WORD, DWORD
        except ImportError:
            # workaround for missing types in Python 2.5
            from ctypes import (
                c_short as SHORT, c_ushort as WORD, c_ulong as DWORD)
        console_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

        # CONSOLE_SCREEN_BUFFER_INFO Structure
        class COORD(Structure):
            _fields_ = [("X", SHORT), ("Y", SHORT)]

        class SMALL_RECT(Structure):
            _fields_ = [("Left", SHORT), ("Top", SHORT),
                        ("Right", SHORT), ("Bottom", SHORT)]

        class CONSOLE_SCREEN_BUFFER_INFO(Structure):
            _fields_ = [("dwSize", COORD),
                        ("dwCursorPosition", COORD),
                        ("wAttributes", WORD),
                        ("srWindow", SMALL_RECT),
                        ("dwMaximumWindowSize", DWORD)]

        sbi = CONSOLE_SCREEN_BUFFER_INFO()
        ret = windll.kernel32.GetConsoleScreenBufferInfo(
            console_handle, byref(sbi))
        if ret == 0:
            return 0
        return sbi.srWindow.Right+1

    elif os.name == 'posix':
        from fcntl import ioctl
        from termios import TIOCGWINSZ
        from array import array

        winsize = array("H", [0] * 4)
        try:
            ioctl(sys.stdout.fileno(), TIOCGWINSZ, winsize)
        except IOError:
            pass
        return (winsize[1], winsize[0])[0]

    return 80


def bar_thermometer(current, total, width=80):
    
    # number of dots on thermometer scale
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    return '[' + '.'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'

def bar_adaptive(current, total, width=80):

    # process special case when total size is unknown and return immediately
    if not total or total < 0:
        msg = "%s / unknown" % current
        if len(msg) < width:    # leaves one character to avoid linefeed
            return msg
        if len("%s" % current) < width:
            return "%s" % current

    # --- adaptive layout algorithm ---
    #
    # [x] describe the format of the progress bar
    # [x] describe min width for each data field
    # [x] set priorities for each element
    # [x] select elements to be shown
    #   [x] choose top priority element min_width < avail_width
    #   [x] lessen avail_width by value if min_width
    #   [x] exclude element from priority list and repeat
    
    #  10% [.. ]  10/100
    # pppp bbbbb sssssss

    min_width = {
      'percent': 4,  # 100%
      'bar': 3,      # [.]
      'size': len("%s" % total)*2 + 3, # 'xxxx / yyyy'
    }
    priority = ['percent', 'bar', 'size']

    # select elements to show
    selected = []
    avail = width
    for field in priority:
      if min_width[field] < avail:
        selected.append(field)
        avail -= min_width[field]+1   # +1 is for separator or for reserved space at
                                      # the end of line to avoid linefeed on Windows
    # render
    output = ''
    for field in selected:

      if field == 'percent':
        # fixed size width for percentage
        output += ('%s%%' % (100 * current // total)).rjust(min_width['percent'])
      elif field == 'bar':  # [. ]
        # bar takes its min width + all available space
        output += bar_thermometer(current, total, min_width['bar']+avail)
      elif field == 'size':
        # size field has a constant width (min == max)
        output += ("%s / %s" % (current, total)).rjust(min_width['size'])

      selected = selected[1:]
      if selected:
        output += ' '  # add field separator

    return output


__current_size = 0  # global state variable, which exists solely as a
                    # workaround against Python 3.3.0 regression
                    # http://bugs.python.org/issue16409
                    # fixed in Python 3.3.1
def callback_progress(blocks, block_size, total_size, bar_function):
    """callback function for urlretrieve that is called when connection is
    created and when once for each block

    draws adaptive progress bar in terminal/console

    use sys.stdout.write() instead of "print,", because it allows one more
    symbol at the line end without linefeed on Windows

    :param blocks: number of blocks transferred so far
    :param block_size: in bytes
    :param total_size: in bytes, can be -1 if server doesn't return it
    :param bar_function: another callback function to visualize progress
    """
    global __current_size
 
    width = min(100, get_console_width())

    if sys.version_info[:3] == (3, 3, 0):  # regression workaround
        if blocks == 0:  # first call
            __current_size = 0
        else:
            __current_size += block_size
        current_size = __current_size
    else:
        current_size = min(blocks*block_size, total_size)
    progress = bar_function(current_size, total_size, width)
    if progress:
        sys.stdout.write("\r" + progress)


def detect_filename(url=None, out=None, headers=None, default="download.wget"):
    """Return filename for saving file. If no filename is detected from output
    argument, url or headers, return default (download.wget)
    """
    names = dict(out='', url='', headers='')
    if out:
        names["out"] = out or ''
    if url:
        names["url"] = filename_from_url(url) or ''
    if headers:
        names["headers"] = filename_from_headers(headers) or ''
    return names["out"] or names["headers"] or names["url"] or default

def download(url, out=None, bar=bar_adaptive):
    """High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.

    :param bar: function to track download progress (visualize etc.)
    :param out: output filename or directory
    :return:    filename where URL is downloaded to
    """
    # detect of out is a directory
    outdir = None
    if out and os.path.isdir(out):
        outdir = out
        out = None

    # get filename for temp file in current directory
    prefix = detect_filename(url, out)
    (fd, tmpfile) = tempfile.mkstemp(".tmp", prefix=prefix, dir=".")
    os.close(fd)
    os.unlink(tmpfile)

    # set progress monitoring callback
    def callback_charged(blocks, block_size, total_size):
        # 'closure' to set bar drawing function in callback
        callback_progress(blocks, block_size, total_size, bar_function=bar)
    if bar:
        callback = callback_charged
    else:
        callback = None

    if PY3K:
        # Python 3 can not quote URL as needed
        binurl = list(urlparse.urlsplit(url))
        binurl[2] = urlparse.quote(binurl[2])
        binurl = urlparse.urlunsplit(binurl)
    else:
        binurl = url
    (tmpfile, headers) = ulib.urlretrieve(binurl, tmpfile, callback)
    filename = detect_filename(url, out, headers)
    if outdir:
        filename = outdir + "/" + filename

    # add numeric ' (x)' suffix if filename already exists
    if os.path.exists(filename):
        filename = filename_fix_existing(filename)
    shutil.move(tmpfile, filename)

    #print headers
    return filename

def ascii_art_maker(link,color):
	
	
	black = '\u001b[30m'
	red = '\u001b[31m'
	green = '\u001b[32m'
	yellow = '\u001b[33m'
	blue = '\u001b[34m'
	magenta = '\u001b[35m'
	cyan = '\u001b[36m'
	white = '\u001b[37m'
	reset = '\u001b[0m'
	
	stock_char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	char_set_1 = 'BS#&@$%*!:.'
	
	url = 'https://www.degraeve.com/img2txt-yay.php?url='+link+'&mode=A&size='+'100'+'&charstr='+stock_char_set+'&order=O&invert=Y'

	HTML = urlopen(url)

	soup = BeautifulSoup (HTML.read(), 'html.parser')
	
	try:
		art = soup.find('pre').text

		if color == 'red':
			print (red)
			print(art)
			print(reset)
	
		elif color == 'green':
			print(green)
			print(art)
			print(reset)
		
		elif color == 'yellow':
			print(yellow)
			print(art)
			print(reset)
		
		elif color == 'blue':
			print(blue)
			print(art)
			print(reset)
	
		elif color == 'magenta':
			print(magenta)
			print(art)
			print(reset)
	
		elif color == 'cyan':
			print(cyan)
			print(art)
			print(reset)
		
		elif color == 'reset':
			print(reset)
			print(art)
			print(reset)
		
		else: 
			print(colors)
	except:
		pass

def show_something(data_link):
	
	response = urlopen(data_link)
  
	x = json.loads(response.read())
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][0]['data']['title'],'\n')
	print(x['data']['children'][0]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][0]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][1]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][1]['data']['title'],'\n')
	print(x['data']['children'][1]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][1]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][2]['data']['title'],'\n')
	print(x['data']['children'][2]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][2]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][3]['data']['title'],'\n')
	print(x['data']['children'][3]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][3]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][4]['data']['title'],'\n')
	print(x['data']['children'][4]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][4]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][5]['data']['title'],'\n')
	print(x['data']['children'][5]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][5]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][6]['data']['title'],'\n')
	print(x['data']['children'][6]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][6]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][7]['data']['title'],'\n')
	print(x['data']['children'][7]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][7]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][8]['data']['title'],'\n')
	print(x['data']['children'][8]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][8]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][9]['data']['title'],'\n')
	print(x['data']['children'][9]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][9]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][10]['data']['title'],'\n')
	print(x['data']['children'][10]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][10]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][11]['data']['title'],'\n')
	print(x['data']['children'][11]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][11]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][12]['data']['title'],'\n')
	print(x['data']['children'][12]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][12]['data']['thumbnail'],'magenta')
		
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][13]['data']['title'],'\n')
	print(x['data']['children'][13]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][13]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][14]['data']['title'],'\n')
	print(x['data']['children'][14]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][14]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][15]['data']['title'],'\n')
	print(x['data']['children'][15]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][15]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][16]['data']['title'],'\n')
	print(x['data']['children'][16]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][16]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][17]['data']['title'],'\n')
	print(x['data']['children'][17]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][17]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][18]['data']['title'],'\n')
	print(x['data']['children'][18]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][18]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][19]['data']['title'],'\n')
	print(x['data']['children'][19]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][19]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][20]['data']['title'],'\n')
	print(x['data']['children'][20]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][20]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][21]['data']['title'],'\n')
	print(x['data']['children'][21]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][21]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][22]['data']['title'],'\n')
	print(x['data']['children'][22]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][22]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][23]['data']['title'],'\n')
	print(x['data']['children'][23]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][23]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][24]['data']['title'],'\n')
	print(x['data']['children'][24]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][24]['data']['thumbnail'],'magenta')

def get_hsl_playlist_link():

	hls_source = x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url']

	mp4_link = ('https://savemp4.red/?url='+ hls_source )
	
	#https://savemp4.red/?url=
	
	
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print('\n'+'hls_source: '+ x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url'],'\n')
	#['subreddit'])
	choice = input('do you want to save the video as mp4 (y/n)')
	print('\n')
	if choice == 'y':
		print('\033[41m\033[30m')
		filename = download(mp4_link)
		print('\033[0m')
		print('\n\n'+ filename +' saved succesfully !'+'\n')
	elif choice == 'n':
		exit()
	
	else:
		exit()
	
def get_gifs_and_images():
	
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print(x[0]['data']['children'][0]['data']['url_overridden_by_dest'],'\n')
	#['subreddit'])
	choice = input('do you want to save the file(y/n)')
	print('\n')
	if choice == 'y':
		print('\033[41m\033[30m')
		filename = download(x[0]['data']['children'][0]['data']['url_overridden_by_dest'])
		print('\033[0m')
		print('\n\n'+ filename +' saved succesfully !'+'\n')
	elif choice == 'n':
		exit()
	
	else:
		exit()
		
def get_text():
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print(x[0]['data']['children'][0]['data']['selftext'],'\n')

def main():

	if len(sys.argv) <= 1:
	
		search = input(str('\n'+'which subreddit do you want to look at:'))
		show_something('https://www.reddit.com/search.json?q='+search)

	else:

		link = sys.argv[1]

		if link == '--help':
			print(about)
		else:

			data_link = link[:link.find('?utm')][:-1] + '.json'
	
			response = urlopen(data_link)
  
			x = json.loads(response.read())
	
			try:
				get_hsl_playlist_link()
			
			except TypeError:
				
				try:
					get_gifs_and_images()
				except KeyError:
					get_text()

main()