import time


def say_hello():
    print("Hello")
    time.sleep(2)  # Non-blocking wait
    print("Hello again after 2 seconds")


def say_world():
    print("World")
    time.sleep(1)  # Non-blocking wait
    print("World again after 1 second")


def main():
    # Schedule both tasks concurrently
    say_hello()
    say_world()


# Start the event loop
start = time.time()
main()
print("elapsed_time =", time.time() - start)
