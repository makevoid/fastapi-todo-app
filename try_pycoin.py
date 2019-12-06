import random
from pycoin.symbols.btc import network


rand = random.getrandbits(256)

priv_key = network.keys.private(secret_exponent=rand)
# print("private key:")
# print(priv_key.wif())

# bip32 - https://github.com/richardkiss/pycoin#bip32

print("address:")
print(priv_key.address())

address = priv_key.address()


# TODO: read transaction from blockcypher
tx_hex = "...."

# get the spendable from the prior transaction
tx = network.tx.from_hex(tx_hex)
tx_out_index = 0
spendable = tx.tx_outs_as_spendable()[tx_out_index]

# make sure the address is valid
assert network.parse.address(address) is not None

# create the unsigned transaction
tx = network.tx_utils.create_tx([spendable], [payable])

print("here is the transaction: %s" % tx.as_hex(include_unspents=True))
