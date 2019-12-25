from mamba import description, context, it
from expects import expect, equal, be_true

from pycoin.key import Key

from try_pycoin import load_priv_key

def is_key(obj):
  return obj.__class__.__name__ == "Key"

with description('App'):
  # note: you have to have a file named `.private_key` with a valid private key for this spec to work
  with it('loads the private key'):
    priv_key = load_priv_key()
    expect(is_key(priv_key)).to(be_true)
