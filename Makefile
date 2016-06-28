run:
	@MUFFIN_CONFIG=killer_tofu.settings.production muffin killer_tofu run

requirements:
	@pip install -r requirements.txt

docker_build:
	@docker build -t=hugosenari/killer_tofu .

docker_run:
	@docker run -d -p 5000:5000 hugosenari/killer_tofu muffin killer_tofu run --bind 0.0.0.0:5000