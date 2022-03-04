import base64
import logging


def get_auth(self=None):
    if self == 'test':
        user = 'dev'
        password = 'password'
    else:
        user = 'production'
        password = 'password'
    auth = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
    return auth


def convert_b64_string_to_file(self, instring, outfile):
    # Decode Base64 and write to the file
    self.instring = instring
    # print('len-self.instring', len(self.instring))
    # print(self.instring)
    self.outfile = outfile
    log = logging.getLogger(__name__)
    try:
        with open(outfile, "wb") as f:
            b = self.instring.encode("UTF-8")
            f.write(base64.b64decode(b))
            # f.write(base64.b64decode(self.instring))
    except FileNotFoundError:
        log.warning('File Not Found - :', self.outfile)
        print('File Not Found - ', self.outfile)
    except FileExistsError:
        log.warning('File Exists Error - :')
        print('File Exists Error')

    return True


def convert_string_to_file(self, instring, outfile):
    log = logging.getLogger(__name__)
    self.instring = instring
    self.outfile = outfile
    try:
        with open(self.outfile, "wb") as f:
            f.write(self.instring.encode('utf-8'))
    except FileNotFoundError:
        log.warning('File Not Found - :', self.outfile)
        print('File Not Found - ', self.outfile)
    except FileExistsError:
        log.warning('File Exists Error - :')
        print('File Exists Error')
