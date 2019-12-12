import random
import requests
import inspect
import pprint
from pycoin.symbols.btc import network
from pycoin.encoding.hexbytes import h2b

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


output_index = 0
output_script = data["out"][output_index]["script"]

url_rawtx_insight = f"https://insight.bitpay.com/api/rawtx/{tx_id}"

req = requests.get(url=url_rawtx_insight)
data = req.json()
print("rawtx insight:")
pp(req)

tx_raw = data["rawtx"]

tx_prev = network.tx.from_hex(tx_raw)
spendable_output = tx_prev.tx_outs_as_spendable()[output_index]

print("prev tx:")
pp(tx_prev)
print("spendable output:")
pp(spendable_output)


assert network.parse.address(address) is not None

tx = network.tx_utils.create_tx([spendable_output], [address])

print("tx:")
pp(tx)

output_scripts = [h2b(output_script)]
p2sh_lookup = network.tx.solve.build_p2sh_lookup(output_scripts)

# sign the transaction with the given WIF
network.tx_utils.sign_tx(tx, wifs=[priv_key.wif()], p2sh_lookup=p2sh_lookup)

bad_solution_count = tx.bad_solution_count()
print("tx %s now has %d bad solution(s)" % (tx.id(), bad_solution_count))

include_unspents = (bad_solution_count > 0)
print("TX - serialized:")
print(tx.as_hex(include_unspents=include_unspents))
