local:
	liquidluck build -v
	liquidluck server

deploy:
	git push heroku master
