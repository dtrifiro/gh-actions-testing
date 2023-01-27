import asyncio

import asyncssh


async def main():
    async with asyncssh.agent.connect_agent() as agent:
        keys = await agent.get_keys()
        for key in keys:
            print(key)


if __name__ == "__main__":
    asyncio.run(main())
