import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Telegram-Bot8",
    version="0.1.6",
    author="AppDevIn Sliver",
    author_email=" teamprojectlive@example.com",
    description="Python package to utilizes the telegram API to easily add commands and person other actions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AppDevIn/TelegramBot",
    project_urls={
        "Bug Tracker": "https://github.com/AppDevIn/TelegramBot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "setuptools>=42",
        "wheel",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.9",
        "idna==3.3",
        "requests==2.26.0",
        "urllib3==1.26.7",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

