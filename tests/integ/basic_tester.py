import asyncio

import farfetchd
from farfetchd.models import Berry


async def main():
    farfetchd.default_config()

    berry = await Berry.objects.get(id=12)
    print(berry)
    print(type(berry.natural_gift_type))
    print(berry.natural_gift_type)


if __name__ == "__main__":
    asyncio.run(main())
