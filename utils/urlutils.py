def add_url_protocol(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "https://" + url
