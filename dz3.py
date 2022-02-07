class Url:
    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):  # переопределение операции '=='
        return str(self) == str(other)

    def __str__(self):  # формирование строки из Url
        if self.path is not None:
            p = '/' + '/'.join(self.path)
        else:
            p = ''
        if self.query is not None:
            q_list = []
            for k, v in self.query.items():
                q_list.append(f'{k}={v}')
            q = '?' + '&'.join(q_list)
        else:
            q = ''
        if self.fragment is not None:
            f = f'#{self.fragment}'
        else:
            f = ''
        return f'{self.scheme}://{self.authority}{p}{q}{f}'


class HttpsUrl(Url):

    def __init__(self, *args, **kwargs):
        super(HttpsUrl, self).__init__(*args, **kwargs)
        self.scheme = 'https'


class HttpUrl(Url):

    def __init__(self, *args, **kwargs):
        super(HttpUrl, self).__init__(*args, **kwargs)
        self.scheme = 'http'


class GoogleUrl(HttpsUrl):

    def __init__(self, *args, **kwargs):
        super(GoogleUrl, self).__init__(*args, **kwargs)
        self.authority = 'google.com'


class WikiUrl(HttpsUrl):

    def __init__(self, *args, **kwargs):
        super(WikiUrl, self).__init__(*args, **kwargs)
        self.authority = 'wikipedia.org'


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
