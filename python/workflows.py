from datetime import timedelta
import logging

from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import GreetingActivities


@workflow.defn
class SayHello:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    @workflow.run
    async def run(self, name: str) -> str:
        workflow.logger.info(f"Will prepare a greeting for {name}")

        greeting = ""
        if len(name) <= 3:
            workflow.logger.info(f"Decided to greet in English")
            greeting = await workflow.execute_activity_method(
                GreetingActivities.get_english_greeting,
                name,
                start_to_close_timeout=timedelta(seconds=5),
            )
        elif len(name) >= 7:
            workflow.logger.info(f"Decided to greet in Turkish")
            greeting = await workflow.execute_activity_method(
                GreetingActivities.get_turkish_greeting,
                name,
                start_to_close_timeout=timedelta(seconds=5),
            )
        else:
            workflow.logger.info(f"Decided to greet in Spanish")
            greeting = await workflow.execute_activity_method(
                GreetingActivities.get_spanish_greeting,
                name,
                start_to_close_timeout=timedelta(seconds=5),
            )

        return greeting
