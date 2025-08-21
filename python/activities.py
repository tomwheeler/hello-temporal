import asyncio

from temporalio import activity


class GreetingActivities:
    @activity.defn
    async def get_english_greeting(self, name: str) -> str:
        activity.logger.info("Generating greeting in English")
        return f"Hello, {name}!"

    @activity.defn
    async def get_spanish_greeting(self, name: str) -> str:
        activity.logger.info("Generating greeting in Spanish")
        return f"¡Hola, {name}!"

    @activity.defn
    async def get_turkish_greeting(self, name: str) -> str:
        activity.logger.info("Generating greeting in Turkish")
        return f"Merhaba, {name}!"
