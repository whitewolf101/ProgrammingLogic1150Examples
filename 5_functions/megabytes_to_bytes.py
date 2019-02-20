"""" megabytes into a number of bytes. So if a user
 has a 10 megabyte file, that’s equal to 10,000,000 bytes.
  Your function should have one argument, the number of megabytes.
  It will return the number of bytes. Function is called from main """


def to_bytes(megabytes):
    number_of_bytes = megabytes * 1000000
    return number_of_bytes


def main():
    file_size = int(input('enter number of megabytes? '))
    byte_count = to_bytes(file_size)
    print(f'{file_size}MB is equal to {byte_count} bytes')


main()
