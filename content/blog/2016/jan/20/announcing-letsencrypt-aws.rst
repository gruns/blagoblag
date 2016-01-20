Announcing letsencrypt-aws
==========================

If you haven't heard, Let's Encrypt is a brand new certificate authority
offering free, automated, and trusted HTTPS certificates. It's extremely
exciting.

Let's Encrypt is built on a protocol called "ACME", which defines a standard
HTTP API for a certificate authority. ``letsencrypt-aws`` is built on that to
easily orchestrate your AWS infrastructure to make sure certificates are
automatically issued and kept up to date.

You can grab a copy on `Github`_.

To get started with Let's Encrypt, first you create your account key, and place
the private key in ``account-key.pem``:

.. code-block:: console

    $ python letsencrypt-aws.py register email@host.com
    2016-01-09 19:56:19 [acme-register.generate-key]
    2016-01-09 19:56:20 [acme-register.register] email=u'email@host.com'
    2016-01-09 19:56:21 [acme-register.agree-to-tos]
    -----BEGIN RSA PRIVATE KEY-----
    [...]
    -----END RSA PRIVATE KEY-----

Now tell it about your ELBs:

.. code-block:: bash

    export LETSENCRYPT_AWS_CONFIG='{
        "domains": [
            {
                "hosts": ["host.com", "www.host.com"],
                "elb": {
                    "name": "my-elb"
                }
            }
        ],
        "acme_account_key": "file:///path/to/account-key.pem"
    }'
    python letsencrypt-aws.py update-certificates

You'll need to have your machine set up for your AWS account (using either the
standard configuration file, environment variables, or IAM instance role).

And then it should just work!

Installing and updating certificates should be a 0-downtime operation,
``letsencrypt-aws`` does not require taking over port 80 or 443.

For full details, checkout the `README`_. Try it out, and don't hesitate to
`file issues`_ with bugs or feature requests.

.. _`Github`: https://github.com/alex/letsencrypt-aws/
.. _`README`: https://github.com/alex/letsencrypt-aws/#readme
.. _`file issues`: https://github.com/alex/letsencrypt-aws/
