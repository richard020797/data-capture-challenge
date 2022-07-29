help: ## This Help
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

run-data-capture: ## Runs a python repl with the required imports.
	@python3 -i -c "from main import DataCapture, DataStats"

clean: ## Cleans Python cache.
	@rm -rf __pycache__

run-tests: ## Runs provided tests.
	@python3 -m unittest tests.py 
