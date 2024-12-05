# Immutable configuration

config = ('127.0.0.1', 8080)

# prevent accidental modification
config[1] = 9090 # This would raise a type error


