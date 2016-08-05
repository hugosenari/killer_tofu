# killer_tofu
Music Information Sync Server

## Up and Run
### Docker
```bash
make d_db_build
make d_db_run
make d_build
make d_run
```
### Requirements
Install `killer_tofu` requirements
```base
(venv) $ pip install -r requirements.txt
```
### Database
Set MOTOR_HOST, MOTOR_PORT and MOTOR_DB with MONGODB information

### Start
User command `run` to start `killer_tofu` server
```base
(venv) $ MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run --workers 6
```
Open up your favorite browser to http://localhost:5000/ to see the site running locally.

You can change `workers` numbers according to number of CPU cores.

To change default `port` use `bind` argument
```bash
(venv) $ MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run --bind 0.0.0.0:8000
```
