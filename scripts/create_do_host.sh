MACHINE_NAME=uwsgi-test-do
docker-machine create -d digitalocean \
                      --digitalocean-access-token='5c017a0bd16289d23ffe169d3e1402e346a6b27e7479843979574f40d6cdcf66' \
                      --digitalocean-region='nyc1' \
                      --digitalocean-size='1gb' \
                      $MACHINE_NAME


#python test.py --logfile uwsgi-test-digital-ocean_1gb_nyc1 --ignore abstact-image.jpg --runs 1000 --host $(docker-machine ip $MACHINE_NAME)
