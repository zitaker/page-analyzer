from validators.url import url
from urllib.parse import urlparse


def normalize(urls):
    parsed = urlparse(urls)
    return f"{parsed.scheme}://{parsed.netloc}"


def validate(urls):
    if url(normalize(urls)) is True:
        return urls
    else:
        var_urls = urls
        return var_urls

# print(validate('http://foobar.dk:80'))
# print(validate('http://foobar.dk:80'))
