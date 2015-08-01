.PHONY: image

image:
	eval $(docker-machine env)
	docker build --rm -t elbaschid/alpine-python .
