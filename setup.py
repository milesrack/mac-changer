from setuptools import setup, find_packages

setup(
	name="mac-changer",
	version="1.0.0",
	description="Change your MAC address to a random address or specify a new one.",
	author="Miles Rack",
	url="https://github.com/milesrack/mac-changer",
	license_files = ("LICENSE",),
	install_requires=["argparse"],
    package_dir={"":"src"},
    entry_points={
        "console_scripts": [
            "mac-changer=mac_changer:main.main"
        ]
    }
)