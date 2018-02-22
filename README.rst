shell-retry
===========

Wrapper for call any utilities with retries until they succeed

Install
-------

``` shell
pip install shell-retry
```

Examples
--------

Let's start from `--help`:

.. code:: shell

  shell-retry --help
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
    --verbose             Be verbose, write how many retries left and how long
                          will we wait

- To debug something use `--verbose` flag.
- `--retry-count` specifies retry (**not a try**) count.
- `--interval` sets **initial** interval between retries, interval multiplies with backoff before next retry.

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

To use some flags in `cmd` use `--` before `cmd`.

.. code:: shell

  shell-retry --retry-count=5 --backoff=1.2 -- curl -m 1 --connect-time 1 http://10.30.33.32
  curl: (28) Connection timed out after 1000 milliseconds
  curl: (28) Connection timed out after 1004 milliseconds
  curl: (28) Connection timed out after 1003 milliseconds
  curl: (28) Connection timed out after 1002 milliseconds
  curl: (28) Connection timed out after 1000 milliseconds
  curl: (28) Connection timed out after 1000 milliseconds


