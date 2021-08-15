import json
import os

class Settings(dict):

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path: str = path

    def load(self, no_override=False):
        self._check_file()
        try:
            f = open(self.path, 'r')
            j = json.loads(f.read())
            f.close()
        except json.decoder.JSONDecodeError:
            f = open(self.path, 'w')
            f.write('{}')
            f.close()
        finally:
            f = open(self.path, 'r')
            j = json.loads(f.read())
            f.close()
            for key in j:
                if no_override:
                    self.setdefault(key, j[key])
                else:
                    self[key] = j[key]

    def save(self):
        self._check_file()
        f = open(self.path, "w")
        f.write(json.dumps(self, indent=2))
        f.close()

    def _check_file(self):
        p = self.path.split('/')
        if self.path[0] == '/':
            p[0] = '/' + p[0]

        for i in range(len(p) - 1):
            i += 1
            if not os.path.isdir('/'.join(p[:i])):
                print('/'.join(p[:i]))
                os.mkdir('/'.join(p[:i]))

        if not os.path.isfile(self.path):
            f = open(self.path, 'w')
            f.write('{}')
            f.close()