PORT = 8443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}


MODES = {
    # Classic mode, easy to detect
    "classic": True,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

TLS_DOMAIN = "drive.google.com"
# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
TLS_DOMAIN = "drive.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

METRICS_PORT = 8445
METRICS_EXPORT_LINKS = True
METRICS_WHITELIST = ["172.17.0.1"]

# fine tunning
TO_CLT_BUFSIZE = 262144
TO_TG_BUFSIZE = 262144