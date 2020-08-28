from redis import Redis

R = Redis(host='localhost', port=6379, db=0, decode_responses=True)
