import redis
import argparse

parser = argparse.ArgumentParser(description='redis weak password detection tool')
parser.add_argument('--host', dest='host', help='Redis server IP address', required=False)
parser.add_argument('--port', dest='port', help='Redis server port', required=False)

args = parser.parse_args()


def check_weak_password(password):
    try:
        strict_redis = redis.StrictRedis(host=args.host, port=args.port, password=password)
        strict_redis.ping()
        return True
    except:
        return False


def read_password_dictionary(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def main():
    passwords = read_password_dictionary('passwd.txt')
    for passwd in passwords:
        pd = passwd.strip()  # 去除换行符
        print(f'正在试->：{pd}')
        if check_weak_password(pd):
            print(f'发现弱密码：{pd}')
            break
    else:
        print('未找到弱密码')


if __name__ == '__main__':
    main()
