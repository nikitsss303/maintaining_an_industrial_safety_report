import asyncio

import asyncpg


async def run():
    conn = await asyncpg.connect(
        user="nikitooosss", password="1901", database="testdb", host="127.0.0.1"
    )
    values = await conn.fetchrow(
        "SELECT * FROM users WHERE name = $1 AND age = $2",
        'sasha',
        101,
    )
    print(type(values))
    print(values)
    await conn.close()


asyncio.run(run())
