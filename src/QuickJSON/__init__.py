import json
import os
import shutil

class QJSON(dict):

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path: str = path

    def move_save(self, new_path):
        self.copy_save(new_path)
        self.clear_save()
        self.path = new_path

    def copy_save(self, new_path):
        assert not self.path == new_path
        self._check_file(new_path)
        self._check_file(self.path)
        shutil.copy(self.path,new_path)

    def clear_save(self):
        a = self.path.split(os.sep)
        if self.path[0] == os.sep:
            a[0] = os.sep + a[0]
        os.remove(self.path)
        for i in range(1, len(a)):
            try:
                os.rmdir(os.sep.join(a[:-i]))
            except Exception:
                pass


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

    def _check_file(self, path=None):
        if path is None:
            path = self.path

        p = path.split(os.sep)
        if path[0] == os.sep:
            p[0] = os.sep + p[0]

        for i in range(len(p) - 1):
            i += 1
            if not os.path.isdir(os.sep.join(p[:i])):
                os.mkdir(os.sep.join(p[:i]))

        if not os.path.isfile(path):
            f = open(path, 'w')
            f.write('{}')
            f.close()
