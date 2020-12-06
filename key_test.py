key_sha1 = hashlib.sha1(key).hexdigest()
if key_sha1 == "e2da39989f2ad9dae985c98656b73b93974d62a6" or key_sha1 == "71b9c397444943baee92fc16cc2a7981af676dd6" or key_sha1 == "fad8d029a79f38e525b9b2d28cb6adccac9845d5":
    status_verify = True
else:
    status_verify = False
