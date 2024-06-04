import yaml
import bcrypt

names = ["성문", "seongmoon"]
usernames = ["성문", "seongmoon"]
passwords = ["1234", "5678"]

# 비밀번호를 해싱하여 저장
hashed_passwords = [bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() for password in passwords]

data = {
    "credentials": {
        "usernames": {
            usernames[0]: {
                "name": names[0],
                "password": hashed_passwords[0]
            },
            usernames[1]: {
                "name": names[1],
                "password": hashed_passwords[1]
            }
        }
    },
    "cookie": {
        "expiry_days": 0,  # 만료일, 재인증 기능 필요없으면 0으로 세팅
        "key": "some_signature_key",
        "name": "some_cookie_name"
    },
    "preauthorized": {
        "emails": [
            "melsby@gmail.com"
        ]
    }
}

# YAML 파일에 데이터 저장
with open('config.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

print("Config.yaml 파일이 생성되었습니다.")
