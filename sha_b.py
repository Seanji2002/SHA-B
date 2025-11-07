def hash_sha_B(data: bytes) -> bytes:
    return b"SHA-B" + data.ljust(245, b'\2')
