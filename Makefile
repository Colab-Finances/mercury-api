dev:
	@if [ -z "$(command)" ]; then \
		echo "No <command> specified. Defaulting to bash."; \
		echo "To specify a <command?, run 'make dev command=<command>'"; \
		command="bash"; \
	fi;
	echo "Running command: $(command)"
	./init.sh run --rm planner_api $(command)
