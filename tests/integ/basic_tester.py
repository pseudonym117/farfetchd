import asyncio
import logging
import sys

import farfetchd
from farfetchd.models.berries import Berry


async def main():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    farfetchd.default_config()

    berry = await Berry.objects.get(id=12)
    print(berry)
    print(type(berry.natural_gift_type))
    print(berry.natural_gift_type)
    print((await berry.natural_gift_type.resolve()).generation)

    berry = await Berry.objects.get(id=12)
    berry = await Berry.objects.get(id=12)

    all_berries = await Berry.objects.all()

    print(all_berries)

    print(await all_berries[0].resolve())
    print(await all_berries[0].resolve())


if __name__ == "__main__":
    asyncio.run(main())
