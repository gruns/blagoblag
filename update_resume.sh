#!/bin/bash

set -ex

pandoc resume.rst --out=content/resume.pdf
