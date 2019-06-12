
import ConfigParser


class ConfigParser(ConfigParser.ConfigParser):
    """
        对ConfigParser的增强，将内容直接转化为dict，方便操作。
    """

    # key 的大写必须保留，不能自动转为小写
    optionxform = str

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

    @classmethod
    def read_from_file_as_dict(cls, path):
        config = ConfigParser()
        config.read(path)
        return config.as_dict()