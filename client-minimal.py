import asyncio

from asyncua import Client

url = "opc.tcp://localhost:4841/freeopcua/server/"
namespace = "http://examples.freeopcua.github.io"


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        nsidx = await client.get_namespace_index(namespace)
        print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write
        to_write_var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:MyObject", f"{nsidx}:readVar"]
        )
        value = await to_write_var.read_value()
        print(f"Value of to_write_var ({to_write_var}): {value}")
        print("type: ", type(value))

        user_input = input("Enter a value: ")
     #   new_value = value - 50
        print(f"Setting value of to_write_var to {user_input} ...")
        await to_write_var.write_value(float(user_input))



        # Calling a method
        res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        print(f"Calling ServerMethod returned {res}")


if __name__ == "__main__":
    asyncio.run(main())
