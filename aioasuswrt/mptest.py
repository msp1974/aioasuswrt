import asyncio
from asuswrt import AsusWrt
import logging

_LOGGER = logging.getLogger(__name__)

HOST = "192.168.200.1"
PORT = 22
USER = "admin"
PWD = "Markyp55"


async def go():
    api = AsusWrt(HOST, PORT, False, USER, PWD)

    try:
        await api.connection.async_connect()
    except OSError as ex:
        _LOGGER.warning("Error %s connecting to %s.", str(ex), HOST)

    if not api.is_connected:
        _LOGGER.error("Error connecting to %s.", HOST)
        return False

    # print("WAN status is {}".format(await api.async_get_supported_functions()))

    _wan = await api.async_get_wan()
    _supported = await api.async_get_supported_functions()

    print("Supported info is {}".format(_supported))

    print("WAN STatus is {}".format(_wan))

    active_unit = _wan["wans"].get("wan_unit")

    print(
        "Active WAN is {}".format(
            _wan["wans"].get("wans_dualwan").split()[int(active_unit)]
        )
    )

    # await api.async_reboot()


asyncio.run(go())
