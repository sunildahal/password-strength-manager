import hashlib
import requests

def check_pwned(password):
    # Step 1: SHA1 hash
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    # Step 2: Query HIBP API (k-Anonymity)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "HIBP API error"}

    hashes = response.text.splitlines()

    # Step 3: Compare suffixes
    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return {"pwned": True, "count": int(count)}

    return {"pwned": False, "count": 0}
