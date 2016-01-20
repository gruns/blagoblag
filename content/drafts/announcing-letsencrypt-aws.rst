Announcing ``letsencrypt-aws``
==============================

If you haven't heard, Let's Encrypt is a brand new certificate authority
offering free, automated, and trusted HTTPS certificates. It's extremely
exciting.

Let's Encrypt is built on a protocol called "ACME", which defines a standard
HTTP API for a certificate authority. ``letsencrypt-aws`` is built on that to
easily orchestrate your AWS infrastructure to make sure certificates are
automatically issued and kept up to date.

You can grab a copy on `Github`_.

To get started with Let's Encrypt, first you create your account key:

.. code-block:: console

    $ python letsencrypt-aws.py register <email-address> --out=account-key.pem
    [acme-register.generate-key]
    [acme-register.register] email=<email-address>
    [acme-register.agree-to-tos]

Now tell it about your ELBs:

.. code-block:: console

    $ export LETSENCRYPT_AWS_CONFIG='{
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
    $ python letsencrypt-aws.py update-certificates

You'll need to have your machine set up for your AWS account (using either the
standard configuration file, environment variables, or IAM instance role).

And then it should just work!

Installing and updating certificates should be a 0-downtime operation.
``letsenctypt-aws`` is designed to be usable in production.

For full details, checkout the `README._ Try it out, and don't hesitate to
`file issues`_ with bugs or feature requests.

.. _`Github`: https://github.com/alex/letsencrypt-aws/
.. _`README`: https://github.com/alex/letsencrypt-aws/
.. _`file issues`: https://github.com/alex/letsencrypt-aws/
