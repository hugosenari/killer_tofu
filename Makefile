run:
	@MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run

requirements:
	@pip install -r requirements.txt

docker_build:
	@docker build -t=hugosenari/killer_tofu .

docker_run:
	-@docker kill killer_tofu 2>/dev/null; true
	-@docker rm killer_tofu 2>/dev/null; true
	@docker run --name killer_tofu -v $(shell pwd)/killer_tofu:/src/killer_tofu -d -p 5000:5000 hugosenari/killer_tofu muffin killer_tofu run --bind 0.0.0.0:5000
