#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Edwin Torres"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    contents = os.listdir(dirname)
    pattern = r'.*__.+__.*'
    special_files = []
    abs_paths = []
    for content in contents:
        special_match = str(re.findall(pattern, content))
        if special_match != '[]':
            special_match = special_match[2:-2]
            special_files.append(dirname + "/" + special_match)
    for special_file in special_files:
        abs_paths.append(os.path.abspath(special_file))
    return abs_paths


def copy_to(path_list, dest_dir):
    """Will copy all files in path_list to dest_dir"""
    try:
        os.makedirs(dest_dir)
    except FileExistsError:
        print("the directory already exists!")
    for path in path_list:
        shutil.copy(path, dest_dir)


def zip_to(path_list, dest_zip):
    """Creates an archive Zip at the given dir from the given dir"""
    command = ["zip", "-j", dest_zip]
    command.extend(path_list)
    print("Command I'm going to do:")
    print(' '.join(command))
    try:
        _output = subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='lists all special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    if not ns:
        parser.print_usage()
        sys.exit(1)

    from_dir = ns.from_dir
    todir = ns.todir
    tozip = ns.tozip

    # Your code here: Invoke (call) your functions
    if not todir and not tozip:
        files = get_special_paths(from_dir)
        print('\n'.join(files))
    if todir:
        copy_to(get_special_paths(from_dir), todir)

    if tozip:
        zip_to(get_special_paths(from_dir), tozip)


if __name__ == "__main__":
    main(sys.argv[1:])
