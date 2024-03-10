import setuptools

required_packages = [
    "aiohttp",
]


setuptools.setup(
    name="bitly_api",
    version="0.1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="Python wrapper for apilayer.com shortner service",
    url="",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
)
