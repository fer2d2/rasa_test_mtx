bootstrap:
	python3 -m venv ./venv

activate:
	@echo "\nRun this command: \n\nsource ./venv/bin/activate\n"

freeze:
	python -m pip freeze > requirements.txt

install:
	python -m pip install -r requirements.txt
	pip install "rasa[spacy]"
	python -m spacy download es_core_news_md
	python -m spacy link es_core_news_md es

train:
	rasa train -d ./domain.yml

chat:
	rasa shell

chat_debug:
	rasa shell -vv

run_endpoints:
	rasa run actions -vv

run_server:
	rasa run -m models --enable-api --log-file out.log

run_server_debug:
	rasa run -m models --enable-api --log-file out.log

run_tunnel:
	ngrok http 5005

visualize:
	python -m rasa visualize -s data/stories.md -d domain.yml --out story_graph.html
