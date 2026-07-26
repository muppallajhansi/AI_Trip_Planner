from setuptools import find_packages, setup


def get_requirements():
    """
    Read requirements.txt and return the required packages.
    """

    requirement_list = []

    try:
        with open("requirements.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_list


setup(
    name="ai-trip-planner",
    version="0.1.0",
    author="Jhansi Muppalla",
    author_email="muppallajhansi09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.12",
)