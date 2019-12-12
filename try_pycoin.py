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

url_rawtx_bcinfo = f"https://blockchain.info/rawtx/{tx_id}"

req = requests.get(url=url_rawtx_bcinfo)
data = req.json()
print("rawtx bcinfo:")
pp(req)
pp(data)

url_rawtx_insight = f"https://insight.bitpay.com/api/rawtx/{tx_id}"

req = requests.get(url=url_rawtx_insight)
data = req.json()
print("rawtx insight:")
pp(req)

tx_raw = data["rawtx"]

tx_prev = network.tx.from_hex(tx_raw)
tx_prev_out_index = 0
spendable_output = tx_prev.tx_outs_as_spendable()[tx_prev_out_index]

print("prev tx:")
pp(tx_prev)
print("spendable output:")
pp(spendable_output)


assert network.parse.address(address) is not None

tx = network.tx_utils.create_tx([spendable_output], [address])


exit


# bip32 - https://github.com/richardkiss/pycoin#bip32







# # get the spendable from the prior transaction

#
# # make sure the address is valid
#
# # create the unsigned transaction
# tx = network.tx_utils.create_tx([spendable], [payable])
#
# print("here is the transaction: %s" % tx.as_hex(include_unspents=True))


# sign TX
# https://github.com/richardkiss/pycoin/blob/master/recipes/multisig/4_sign_tx.py
