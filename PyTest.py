import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]



def Fail_Program():
    assert ("fail_program" in installed_packages)

try:
    assert ("atomicwrites" in installed_packages)
    print("atomicwrites installation test passed..... overall progress 10%\n\n")

except AssertionError:
    print ('atomicwrites installation test Failed\n\n')
    Fail_Program()

try:
    assert ("attrs" in installed_packages)
    print("attrs installation test passed..... overall progress 20%\n\n")

except AssertionError:
    print ('attrs installation test Failed\n\n')
    Fail_Program()

try:

    assert ("beautifulsoup4" in installed_packages)
    print("beautifulsoup4 installation test passed..... overall progress 30%\n\n")

except AssertionError:
    print ('beautifulsoup4 installation test Failed\n\n')
    Fail_Program()

try:
    assert ("chardet" in installed_packages)
    print("chardet installation test passed..... overall progress 40%\n\n")

except AssertionError:
    print ('chardet installation test Failed\n\n')
    Fail_Program()

try:
    print("idna installation test passed..... overall progress 50%\n\n")
    assert ("importlib-metadata" in installed_packages)

except AssertionError:
    print ('idna installation test Failed\n\n')
    Fail_Program()

try:
    assert ("importlib-metadata" in installed_packages)
    print("importlib-metadata installation test passed..... overall progress 60%\n\n")

except AssertionError:
    print ('importlib-metadata installation test Failed\n\n')
    Fail_Program()

try:
    assert ("more-itertools" in installed_packages)
    print("more-itertools installation test passed..... overall progress 70%\n\n")

except AssertionError:
    print ('more-itertools installation test Failed\n\n')
    Fail_Program()

try:
    assert ("packaging" in installed_packages)
    print("packaging installation test passed..... overall progress 80%\n\n")

except AssertionError:
    print ('packaging installation test Failed\n\n')
    Fail_Program()

try:
    assert ("pluggy" in installed_packages)
    print("pluggy installation test passed..... overall progress 90%\n\n")

except AssertionError:
    print ('pluggy installation test Failed\n\n')
    Fail_Program()

try:
    assert ("py" in installed_packages)
    print("py installation test passed..... overall progress 100%\n\n")

except AssertionError:
    print ('py installation test Failed\n\n')
    Fail_Program()


# Two errors print when tests fail, this is expected.
