import setuptools

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "itisyash"  # Corrected typo from AUUTHOR_USER_NAME to AUTHOR_USER_NAME
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "itsyashtripathiofficial@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,  # Added quotes around the author's name
    author_email=AUTHOR_EMAIL,  # Added quotes around the author's email
    description="A simple Python library for text summarization using transformers",
    long_description=long_description,  # Use the variable instead of a string
    long_description_content_type="text/markdown",  # Specify content type for long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Fixed variable usage
    project_urls={  # Corrected typo from projrct_urls to project_urls
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
