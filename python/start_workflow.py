import asyncio
import sys

from temporalio.client import Client

from client_provider import get_temporal_client
from workflows import SayHello


async def main() -> None:
    client = await get_temporal_client()

    if len(sys.argv) <= 1:
        sys.exit("Must specify the name of the person to greet")
    name = sys.argv[1]

    result = await client.execute_workflow(
        SayHello.run,
        name,
        id=f"say-hello-{name}",
        task_queue="say-hello-task-queue",
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
