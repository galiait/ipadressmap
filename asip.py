import asyncio
import time

async def ping(host):
    """
    Prints the hosts that respond to ping request
    """
    ping_process = await asyncio.create_subprocess_shell("ping -c 8 " + host + " > /dev/null 2>&1")
    await ping_process.wait()

    if ping_process.returncode == 0:
        print(host+ " is up!")
    #else:
    #    print(host+ " is down!")
    return 


async def ping_all():
    tasks = []

    for i in range(1,255):
        ip = "192.168.1.{}".format(i)
        task = asyncio.ensure_future(ping(ip))
        tasks.append(task)

    await asyncio.gather(*tasks, return_exceptions = True)

start_time = time.time()
asyncio.run(ping_all())
print(time.time() - start_time, "seconds")
