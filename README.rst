Static files and `uwsgi`
========================

This is an experiment to serve static files in different ways to see how
using `uwsgi`'s features to serve static files instead of straight `nginx`
or using Django's staticfiles.


Results on AWS EC@ m3.medium
----------------------------


.. code-block:: 

    served by filename                      size      time (ms)
    ------------------------------------------------------------
    NGINX     homepage-header.jpg           125.9 kB  789.473
    DJANGO    homepage-header.jpg           125.9 kB  803.045
    S3        homepage-header.jpg           125.9 kB  890.431
    UWSGI     homepage-header.jpg           125.9 kB  790.767
    ------------------------------------------------------------
    NGINX     jquery.min.js                 93.6 kB   668.172
    DJANGO    jquery.min.js                 93.6 kB   681.083
    S3        jquery.min.js                 93.6 kB   798.477
    UWSGI     jquery.min.js                 93.6 kB   678.973
    ------------------------------------------------------------
