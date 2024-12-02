from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):

    DB_URL: str = "mongodb+srv://gsaurav902:saurav123@cluster0.ntv73.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    model_config = SettingsConfigDict(env_file=".env")
