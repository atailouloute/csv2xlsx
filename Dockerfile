ARG ARCH=""
ARG VERSION="3.7.0"

FROM ${ARCH}/python:${VERSION}

MAINTAINER Ahmed TAILOULOUTE <ahmed.tailouloute@gmail.com>

RUN pip install pyinstaller && \
    pip install --user XlsxWriter && \
    pip install -e git+https://github.com/tqdm/tqdm.git@master#egg=tqdm

COPY csv2xlsx.py /home/csv2xlsx.py