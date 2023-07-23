from distutils.core import setup

setup(
	name="mac-changer",
	version="1.0.0",
	description="Change your MAC address to a random address or specify a new one.",
	author="Miles Rack",
	url="https://github.com/milesrack/mac-changer",
	license_files = ("LICENSE",),
	install_requires=["argparse"],
	scripts=["mac-changer"]
)