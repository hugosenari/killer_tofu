run:
	@MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run

requirements:
	@pip install -r requirements.txt

d_build:
	@docker build -t=hugosenari/killer_tofu .

d_run:
	-@docker stop killer_tofu 2>/dev/null; true
	-@docker rm killer_tofu 2>/dev/null; true
	@docker run --link killer_tofu_data --name killer_tofu -v $(shell pwd)/killer_tofu:/src/killer_tofu -d -p 5000:5000 hugosenari/killer_tofu muffin killer_tofu run --bind 0.0.0.0:5000

d_db_build:
	@docker build -t=hugosenari/killer_tofu_data database

d_db_run:
	-@docker stop killer_tofu_data 2>/dev/null; true
	-@docker rm killer_tofu_data 2>/dev/null; true
	@docker run --name killer_tofu_data -v $(shell pwd)/database:/data/db -d -p 27017:27017 hugosenari/killer_tofu_data mongod
