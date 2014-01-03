PyPI Download Statistics
========================

For the past few weeks, I've been spending a bunch of time on a side project,
which is to get better insight into who uses packages from PyPI. I don't mean
what people, I mean what systems: how many users are on Windows, how many still
use Python 2.5, do people install with ``pip`` or ``easy_install``, questions
like these; which come up all the time for open source projects.

Unfortunately until now there's been basically no way to get this data. So I
sat down to solve this, and to do that I went straight to the source. PyPI!
Downloads of packages are probably our best source of information about users
of packages. So I set up a simple system: process log lines from the web
server, parse any information I could out of the logs (user agents have tons of
great stuff), and then insert it into a simple PostgreSQL database.

We don't yet have the system in production, but I've started playing with
sample datasets, here's my current one:

.. code-block:: sql

    pypi=> select count(*), min(download_time), max(download_time) from downloads;
      count  |         min         |         max
    ---------+---------------------+---------------------
     1981765 | 2014-01-02 14:46:42 | 2014-01-03 17:40:04
    (1 row)

All of the downloads over the course of about 27 hours. There's a few caveats
to the data: it only covers PyPI, packages installed with things like
``apt-get`` on Ubuntu/Debian aren't counted. Things like CI servers which
frequently install the same package can "inflate" the download count, this
isn't a way of directly measuring users. As with all data, knowing how to
interpret it and ask good questions is at least as important as having the
data.

Eventually I'm looking forwards to making this dataset available to the
community; both as a way to ask one off queries ("What version of Python do
people install my package with?") and as a whole dataset for running large
analysis on ("How long does it take after a release before a new version of
Django has widespread uptake?").

Here's a sample query:

.. code-block:: sql

    pypi=> SELECT
    pypi->     substring(python_version from 0 for 4),
    pypi->     to_char(100 * COUNT(*)::numeric / (SELECT COUNT(*) FROM downloads), 'FM999.990') || '%' as percent_of_total_downloads
    pypi-> FROM downloads
    pypi-> GROUP BY
    pypi->     substring(python_VERSION from 0 for 4)
    pypi-> ORDER BY
    pypi->     count(*) DESC;
     substring | percent_of_total_downloads
    -----------+----------------------------
     2.7       | 75.533%
     2.6       | 15.960%
               | 5.840%
     3.3       | 2.079%
     3.2       | .350%
     2.5       | .115%
     1.1       | .054%
     2.4       | .052%
     3.4       | .016%
     3.1       | .001%
     2.1       | .000%
     2.0       | .000%
    (12 rows)

Here's the schema to give you a sense of what data we have:

.. code-block:: sql

                                       Table "public.downloads"
              Column          |            Type             |              Modifiers
    --------------------------+-----------------------------+-------------------------------------
     id                       | uuid                        | not null default uuid_generate_v4()
     package_name             | text                        | not null
     package_version          | text                        |
     distribution_type        | distribution_type           |
     python_type              | python_type                 |
     python_release           | text                        |
     python_version           | text                        |
     installer_type           | installer_type              |
     installer_version        | text                        |
     operating_system         | text                        |
     operating_system_version | text                        |
     download_time            | timestamp without time zone | not null
     raw_user_agent           | text                        |

Let your imagination run wild with the questions you can answer now that we
have data!
