docker-machine create -d amazonec2 \
                      --amazonec2-access-key='AKIAJ4BRIOSX5VFEZBPA' \
                      --amazonec2-secret-key='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' \
                      --amazonec2-instance-type=m3.medium \
                      --amazonec2-vpc-id=vpc-a3646bc6 \
                      uwsgi-test
