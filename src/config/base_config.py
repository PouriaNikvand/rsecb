import os


class BaseConfig:
    @classmethod
    def configure(cls):
        from dotenv import load_dotenv, find_dotenv
        load_dotenv(find_dotenv())
        for attr_name in cls.__dict__:
            if attr_name.startswith("__"):
                continue
            from_env = os.getenv(attr_name)
            if not from_env:
                continue
            setattr(cls, attr_name, from_env)


if __name__ == "__main__":
    BaseConfig.configure()
