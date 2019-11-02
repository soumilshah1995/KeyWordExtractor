import  requests
import json
import ast

__author__ = "soumil nitin shah "

class MetaClass(type):

    """ Meta class """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ Implementing Singleton Design Pattern  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

    def __init__(cls, name, base, attr):

        """ Defining Your Own Rules  """

        if cls.__name__[0].isupper():

            """ Create class only if First Letter is Capital    """

            for k, v in attr.items():
                if hasattr(v, '__call__'):

                    if v.__name__[0] == '_' or v.__name__[0].islower():

                        """  check name function starts with _ or lower case  """

                        if v.__doc__ is None:

                            """  Check is User has provided Documentation """

                            raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))
                        else:

                            """ if function has Doccumentation pass """

                            pass
                    else:

                        """ function name starts with upper case throw error  """

                        raise ValueError("Function should start with Lower case :{}".format(v.__name__))
        else:
            raise ValueError("Class Name  should start with Capital Letter :{} ".format(cls.__name__[0]))



class Crawler(object):

    def __init__(self, text = ' '):
        self.__headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',}
        self.__url = "http://languages.cortical.io/rest/text/keywords?retina_name=en_general"
        self.text = text

    def get(self):
        r = requests.post(url=self.__url,
                          headers=self.__headers,
                          data=json.dumps(self.text))

        data = ast.literal_eval(r.text)
        return data


class KeyWordExtractor(metaclass=MetaClass):

    def __init__(self, text = ''):

        """ Constructor """

        self.text = text
        self.obj = Crawler(text=self.text)

    @property
    def get(self):

        """ return data """

        return self.obj.get()


# if __name__ == "__main__":
#
#     text = """
#     Hello! I’m Soumil Nitin Shah, a Software and Hardware Developer based
#     in New York City. I have completed by Bachelor in Electronic Engineering and
#     my Double master’s in Computer and Electrical Engineering. I Develop Python Based Cross
#     Platform Desktop Application , Webpages , Software, REST API, Database and much more I
#     have more than 2 Years of Experience in Python
#     """
#     d = KeyWordExtractor(text=text)
#     data = d.get
#     print(data)

