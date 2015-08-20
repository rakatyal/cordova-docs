# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import sys
import argparse
import subprocess

from util import *
from toc import generate

def main():

    # create argument parser
    arg_parser = argparse.ArgumentParser(prog=sys.argv[0])
    arg_parser.add_argument('docs')
    arg_parser.add_argument('data')
    args = arg_parser.parse_args()

    docs_dir = args.docs
    data_dir = args.data

    # go through all languages
    for lang_name in listdirs(docs_dir):
        lang_path = os.path.join(docs_dir, lang_name)

        # go through all versions
        for version_name in listdirs(lang_path):
            version_path = os.path.join(lang_path, version_name)

            prefix     = '/docs/{lang}/{vers}/'.format(lang=lang_name, vers=version_name)
            source_dir = version_path

            dest_name    = generated_tocfile_name(lang_name, version_name)
            dest_path    = os.path.join(data_dir, 'toc', dest_name)
            dest_dir     = os.path.dirname(dest_path)

            # make the output directory if it doesn't exist
            if not os.path.exists(dest_dir):
                mkdirp(dest_dir)

            # generate and write out the file
            toc_text = generate(source_dir, prefix)
            with open(dest_path, 'w') as toc_file:
                toc_file.write(toc_text)

            print dest_path

if __name__ == '__main__':
    main()