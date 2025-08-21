import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from client_provider import get_temporal_client
from workflows import SayHello
from activities import GreetingActivities


async def main() -> None:
    client = await get_temporal_client()

    activities = GreetingActivities()

    worker: Worker = Worker(
        client,
        task_queue="say-hello-task-queue",
        workflows=[SayHello],
        activities=[
            activities.get_english_greeting,
            activities.get_spanish_greeting,
            activities.get_turkish_greeting,
        ],
    )

    print("Starting worker...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
