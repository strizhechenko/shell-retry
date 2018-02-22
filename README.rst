shell-retry
===========

.. |travis| image:: https://travis-ci.org/strizhechenko/shell-retry.svg?branch=master
   :target: https://travis-ci.org/strizhechenko/shell-retry
.. |landscape| image:: https://landscape.io/github/strizhechenko/shell-retry/master/landscape.svg?style=flat
   :target: https://landscape.io/github/strizhechenko/shell-retry/master
.. |pypi| image:: https://badge.fury.io/py/shell-retry.svg
   :target: https://badge.fury.io/py/shell-retry
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg?colorB=green
   :target: https://opensource.org/licenses/MIT
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/shell-retry.svg?colorB=green
   :target: https://pypi.python.org/pypi/shell-retry
.. |issues| image:: https://img.shields.io/codeclimate/issues/github/strizhechenko/shell-retry.svg
   :target: https://codeclimate.com/github/strizhechenko/shell-retry/issues
.. |codeclimate| image:: https://img.shields.io/codeclimate/github/strizhechenko/shell-retry.svg
   :target: https://codeclimate.com/github/strizhechenko/shell-retry

|travis| |landscape| |pypi| |license| |pyversions| |codeclimate| |issues|

Wrapper for call any utilities with retries until they succeed

Install
-------

.. code:: shell

  pip install shell-retry


Examples
--------

Let's start from :code:`--help`:

.. code:: shell

  $ shell-retry --help
  usage: shell-retry [-h] [--backoff BACKOFF] [--retry-count RETRY_COUNT]
                     [--interval INTERVAL] [--verbose]
                     cmd [cmd ...]


  positional arguments:
    cmd

  optional arguments:
    -h, --help            show this help message and exit
    --backoff BACKOFF     backoff factor (sleep(--interval *= --backoff)
    --retry-count RETRY_COUNT
                          How many time re-run cmd if it fails
    --interval INTERVAL   Initial interval between retries
    --interval-max INTERVAL_MAX
                          upper limit for interval
    --interval-min INTERVAL_MIN
                          lower limit for interval
    --verbose             Be verbose, write how many retries left and how long
                          will we wait

- To debug something use :code:`--verbose` flag.
- :code:`--retry-count` specifies retry (**not a try**) count.
- :code:`--interval` sets **initial** interval between retries, interval multiplies with backoff before next retry.

.. code:: shell

  $ shell-retry --verbose --retry-count=5 --backoff=1.3 false
  2018-02-22 18:23:06,682 INFO: Namespace(backoff=1.3, cmd=['false'], interval=1, retry_count=5, verbose=True)
  2018-02-22 18:23:06,683 INFO: run ['false']
  2018-02-22 18:23:06,687 INFO: command returned 1
  2018-02-22 18:23:06,687 INFO: waiting 1.000000 seconds, 5 retries left
  2018-02-22 18:23:07,687 INFO: run ['false']
  2018-02-22 18:23:07,692 INFO: command returned 1
  2018-02-22 18:23:07,692 INFO: waiting 1.300000 seconds, 4 retries left
  2018-02-22 18:23:08,995 INFO: run ['false']
  2018-02-22 18:23:08,999 INFO: command returned 1
  2018-02-22 18:23:08,999 INFO: waiting 1.690000 seconds, 3 retries left
  2018-02-22 18:23:10,690 INFO: run ['false']
  2018-02-22 18:23:10,696 INFO: command returned 1
  2018-02-22 18:23:10,697 INFO: waiting 2.197000 seconds, 2 retries left
  2018-02-22 18:23:12,896 INFO: run ['false']
  2018-02-22 18:23:12,902 INFO: command returned 1
  2018-02-22 18:23:12,903 INFO: waiting 2.856100 seconds, 1 retries left
  2018-02-22 18:23:15,764 INFO: run ['false']
  2018-02-22 18:23:15,769 INFO: command returned 1

To use some flags in :code:`cmd` use :code:`--` before :code:`cmd`.

.. code:: shell

  $ shell-retry --retry-count=5 --backoff=1.2 -- curl -m 1 --connect-time 1 http://10.30.33.32
  curl: (28) Connection timed out after 1000 milliseconds
  curl: (28) Connection timed out after 1004 milliseconds
  curl: (28) Connection timed out after 1003 milliseconds
  curl: (28) Connection timed out after 1002 milliseconds
  curl: (28) Connection timed out after 1000 milliseconds
  curl: (28) Connection timed out after 1000 milliseconds

To limit interval between retries you can use options :code:`--interval-max` and :code:`--interval-min`:

.. code:: shell

  $ shell-retry --verbose --retry-count=3 --backoff=1.2 --interval-max=1.2 -- curl -m 1 --connect-time 1 http://10.30.33.32
  2018-02-22 19:21:59,170 INFO: Namespace(backoff=1.2, cmd=['curl', '-m', '1', '--connect-time', '1', 'http://10.30.33.32'], interval=1, interval_max=1.2, interval_min=None, retry_count=3, verbose=True)
  2018-02-22 19:21:59,170 INFO: run ['curl', '-m', '1', '--connect-time', '1', 'http://10.30.33.32']
  curl: (28) Connection timed out after 1000 milliseconds
  2018-02-22 19:22:00,184 INFO: command returned 28
  2018-02-22 19:22:00,185 INFO: waiting 1.000000 seconds, 3 retries left
  2018-02-22 19:22:01,187 INFO: run ['curl', '-m', '1', '--connect-time', '1', 'http://10.30.33.32']
  curl: (28) Connection timed out after 1005 milliseconds
  2018-02-22 19:22:02,209 INFO: command returned 28
  2018-02-22 19:22:02,210 INFO: waiting 1.200000 seconds, 2 retries left
  2018-02-22 19:22:03,414 INFO: run ['curl', '-m', '1', '--connect-time', '1', 'http://10.30.33.32']
  curl: (28) Connection timed out after 1001 milliseconds
  2018-02-22 19:22:04,432 INFO: command returned 28
  2018-02-22 19:22:04,432 INFO: waiting 1.200000 seconds, 1 retries left
  2018-02-22 19:22:05,638 INFO: run ['curl', '-m', '1', '--connect-time', '1', 'http://10.30.33.32']
  curl: (28) Connection timed out after 1006 milliseconds
  2018-02-22 19:22:06,662 INFO: command returned 28
