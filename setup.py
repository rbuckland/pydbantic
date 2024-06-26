import setuptools
BASE_REQUIREMENTS = [
    "SQLAlchemy==2.0.30",
    "databases==0.9.0",
    "redis>=4.2.0",
    "pydantic>=2.7",
    "pydantic<3",
    "alembic==1.13.1",
]
MYSQL_REQUIREMENTS = [
    "aiomysql==0.0.21",
    "cryptography==3.4.8",
    "mysqlclient==2.0.3",
    "PyMySQL==0.9.3",
]
POSTGRES_REQUIREMENTS = [
    "asyncpg==0.24.0",
    "psycopg2==2.9.1",
]
LITE_REQUIREMENTS = [
    "aiosqlite==0.19.0",
]

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="pydbantic",
    version="0.2.3",
    packages=setuptools.find_packages(include=["pydbantic"], exclude=["build"]),
    author="Joshua Jamison",
    author_email="joshjamison1@gmail.com",
    description="'db' within pydantic - A single model for shaping, creating, accessing, storing data within a Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codemation/pydbantic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Pydantic",
        "Framework :: FastAPI",
        "Topic :: Database",
    ],
    python_requires=">=3.7, <4",
    install_requires=BASE_REQUIREMENTS,
    extras_require={
        "all": BASE_REQUIREMENTS
        + POSTGRES_REQUIREMENTS
        + MYSQL_REQUIREMENTS
        + LITE_REQUIREMENTS,
        "postgres": POSTGRES_REQUIREMENTS,
        "mysql": MYSQL_REQUIREMENTS,
        "sqlite": LITE_REQUIREMENTS,
    },
)
