#!/usr/bin/env python

import pygeoip, socket, getopt, sys, json

APP_NAME = "iptracker"
VERSION  = "1.0.0"
BANNER   = """
                                      Hey there!
                                    127.0.0.1
                                     is that you?
                                        /
   _______________          _______________
  |  ___________  |        |  ___________  |
  | |           | |        | |           | |
  | |   X   X   | |        | |           | |
  | |     -     | |        | |   0   0   | |
  | |    ___    | |        | |     -     | |
  | |   /   \   | |        | |   \___/   | |
  | |   \___/   | |        | |           | |
  | |___________| |        | |___________| |
  |_______________|        |_______________|
    ____|   |___.............._|________|_
   | ********** |            | ********** |
   | ********** |            | ********** |
    ------------              ------------
   {} v{}
   [ Coded by : erfan4lx] Teams : [M4nifest0 - Unidentified - Vortex ](Cyber Security Teams)
"""

HELP_USAGE = """
usage: python iptracker.py [options]
options:
-v --version shows the current version
-t --target  the target host
-h --help    shows the help usage
"""

OPTIONS      = "hvt:"
LONG_OPTIONS = ["help", "version", "target="]

DB_FILE  = "erfan4lx.dat"
target   = None

"""
"""
def usage():
    print(HELP_USAGE)

"""
"""
def version():
    print("{} v{}".format(APP_NAME, VERSION))


"""
"""
def parseargs(argv):
    try:
        opts, args = getopt.getopt(argv, OPTIONS, LONG_OPTIONS)
        if (len(opts) == 0):
            print("[!] No arguments given")
            print("[!] Use --help for help usage")
            sys.exit(0)

        for opt, arg in opts:
            if opt in ("-v", "--version"):
               version()
               sys.exit(0)

            elif opt in ("-h", "--help"):
               usage()
               sys.exit(0)

            elif opt in ("-t", "--target"):
               global target
               target = arg

            if target is None or not target:
               print("[!] No target given")
               print("[!] Use --help for help usage")
               sys.exit(0)

    except getopt.GetoptError as error:
        print("\n")
        print(error)
        usage()
        sys.exit(0)

"""
"""
def gethostaddr():
    host_addr = None;

    try:
        host_addr = socket.gethostbyname(target)
    except:
        pass

    return host_addr

"""
"""
def main(argv):
    parseargs(argv)
    print(BANNER.format(APP_NAME, VERSION))

    print("[+] Resolving host...")
    host = gethostaddr()
    if (host is None or not host):
       print("[!] Unable to resolve host {}".format(target))
       print("[!] Make sure the host is up: ping -c1 {}\n".format(target))
       sys.exit(0)

    print("[+] Host {} has address: {}".format(target, host))
    print("[+] Tracking host...")

    query = pygeoip.GeoIP(DB_FILE)
    result = query.record_by_addr(host)

    if (result is None or not result):
        print("[!] Host location not found")
        sys.exit(0)

    print("[+] Host location found:")
    print (json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False, encoding="utf-8")

"""
"""
if __name__ == "__main__":
   main(sys.argv[1:])

