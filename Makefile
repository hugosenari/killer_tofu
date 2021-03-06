run:
	@MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run

requirements:
	@pip install -r requirements.txt

d_build:
	@docker build -t=hugosenari/killer_tofu .

d_run:
	-@docker stop killer_tofu 2>/dev/null; true
	-@docker rm killer_tofu 2>/dev/null; true
	@docker run -d \
        -p 5000:5000 \
        --name killer_tofu \
        --link killer_tofu_data \
        -v $(shell pwd)/killer_tofu:/src/killer_tofu \
        hugosenari/killer_tofu \
        sh -c 'muffin killer_tofu run --bind 0.0.0.0:5000 2>killer_tofu/.log/stdout.log'

d_db_build:
	@docker build -t=hugosenari/killer_tofu_data database

d_db_run:
	-@docker stop killer_tofu_data 2>/dev/null; true
	-@docker rm killer_tofu_data 2>/dev/null; true
	@docker run -d\
        -p 27017:27017 \
        --name killer_tofu_data \
        -v $(shell pwd)/database:/data/db \
        hugosenari/killer_tofu_data \
        mongod
