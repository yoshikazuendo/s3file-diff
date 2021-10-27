#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import webbrowser

from s3dl import S3FileDownloader
from winmerge import WinMerge

if __name__ == '__main__':
    s3 = S3FileDownloader()
    settings = json.load(
        open('setting\main.json', 'r', encoding='utf-8'))

    srcdir = s3.download(
        settings['src']['bucketName'], settings['src']['s3Directories'])
    dstdir = s3.download(
        settings['dst']['bucketName'], settings['dst']['s3Directories'])
    difffile = WinMerge.output_diff(srcdir, dstdir, s3.rootdir)
    webbrowser.open(difffile)
