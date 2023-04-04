from os import environ
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "DOM_CLEAN": environ["DOM_CLEAN"],
    "INT_CLEAN": environ["INT_CLEAN"],
    # "": environ[""],
    # "": environ[""]
}