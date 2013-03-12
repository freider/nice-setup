nice-setup
==========

Project for setting up all kinds of nice setups on a new work station. This is a sublime plugin which will automatically rsync your data to a remote host, making it easy to develop locally but run remotely.

Installation
------------
Run the following to make your setup nice

    make nice

Usage
------------
Add a .nicesetup file to the root of your project with the destination to replicate to (for example, remote.host:/path/to/base). Whenever you save, the directory containing the .nicesetup file will be copied to the remote directory. Note that any remote changes will be overridden!
