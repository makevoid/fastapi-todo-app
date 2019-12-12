import random
import requests
import inspect
import pprint
from pycoin.symbols.btc import network

# ---
def pp(string):
  p = pprint.PrettyPrinter(indent=2)
  p.pprint(string)


rand = random.getrandbits(256)

priv_key = network.keys.private(secret_exponent=rand)
address = priv_key.address()
print("private key:")
print(priv_key.wif())

print("address:")
print(address)


tx_id = "11e0a8a0ced85b8fd854527d8eb0e675bbba411ea5e04df75331908f9c4363a2"
URL = f"https://blockchain.info/rawtx/{tx_id}"

req = requests.get(url=URL)
data = req.json()

pp(req)
pp(data)

exit


# bip32 - https://github.com/richardkiss/pycoin#bip32






#
# # TODO: read transaction from blockcypher
# tx_hex = "...."
#
# # get the spendable from the prior transaction
# tx = network.tx.from_hex(tx_hex)
# tx_out_index = 0
# spendable = tx.tx_outs_as_spendable()[tx_out_index]
#
# # make sure the address is valid
# assert network.parse.address(address) is not None
#
# # create the unsigned transaction
# tx = network.tx_utils.create_tx([spendable], [payable])
#
# print("here is the transaction: %s" % tx.as_hex(include_unspents=True))


# sign TX
# https://github.com/richardkiss/pycoin/blob/master/recipes/multisig/4_sign_tx.py
