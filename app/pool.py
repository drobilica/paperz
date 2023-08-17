import feedparser
import multiprocessing

def parallel_with_gevent():
    import gevent.monkey
    gevent.monkey.patch_all()
    from gevent.pool import Pool

    # limit ourselves to max 10 simultaneous outstanding requests
    pool = Pool(10)

    def handle_one_url(url):
        parsed = feedparser.parse(url)
        if parsed.entries:
            print 'Found entry:', parsed.entries[0]

    for url in LIST_OF_URLS:
        pool.spawn(handle_one_url, url)
    pool.join()
