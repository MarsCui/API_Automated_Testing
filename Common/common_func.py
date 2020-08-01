# Link parameter
__all__ = ["link", "content_type", "token", "merge_head", "header"]


def link():
    host = "http://xxx.xxx.xxx.xxx"  # no ssl
    port = "xx"
    fore_url = host + ":" + port  # short for url
    return fore_url


def links():
    hosts = "https://xxx.xxx.xxx.xxx"  # with ssl
    port = "3150"
    fore_urls = hosts + ":" + port  # short for url
    return fore_urls


def content_type():
    hct_json = {'Content-Type': 'application/json'}  # header content type, this is for the json, can add other types
    return hct_json


def token():
    original_token = {'Authorization': 'eyJhbGciOiJIUzI1NiJ9.'
                                       'eyJpZCI6MjQsImNvbXBhb'
                                       'nlfaWQiOjEsIndhcnNob3V'
                                       'zZV9pZCI6MSwicm9sZV9pZ'
                                       'CI6MSwidXNlcm5hbWUiOiJ'
                                       'hZG1pbiIsImNyZWF0ZWRfd'
                                       'GltZSI6IjIwMjAtMDMtMjY'
                                       'gMTI6MTc6MjUiLCJjcmVhd'
                                       'GVkX2J5IjoxLCJzdGF0ZSI'
                                       '6IjEiLCJ1cGRhdGVkX3Rpb'
                                       'WUiOiIyMDIwLTAzLTMwIDE'
                                       '0OjM2OjA3IiwidXBkYXRlZ'
                                       'F9ieSI6MSwiZGVsZXRlZCI'
                                       '6MCwiZGlzYWJsZWQiOjB9.'
                                       'Zca4D6vlOWhsBxEjas296J'
                                       'hN-46mm6ICDnMkdNeUdXk'
                      }
    return original_token


# merge token and header(json)
def merge_head(args, kwargs):
    res = {**args, **kwargs}
    return res


header = merge_head(content_type(), token())





