from web3 import Web3
from decouple import config
import os
from pathlib import Path
import time

# First Install
# from solcx import install_solc
# install_solc(version='latest')

from solcx import compile_files


def get_context(f, w3):

    this_dir = Path(os.path.abspath(os.path.dirname(__file__)))
    this_dir = this_dir / "contracts" / f
    sol = Path(this_dir) 

    # Compile Smart Contract
    compiled_sol = compile_files([sol], output_values=["abi", "bin"])

    # retrieve the contract interface
    contract_id, contract_interface = compiled_sol.popitem()

    # get bytecode / bin & abi
    bytecode = contract_interface['bin']
    abi = contract_interface['abi']

    # web3.py instance
    

    # set pre-funded account as sender
    w3.eth.default_account = w3.eth.accounts[0]

    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Contract.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    contract = w3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=abi
    )

    return contract

def write_transact(fn, args, w3):
    tx_hash = fn(*args).transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

w3 = Web3(Web3.EthereumTesterProvider())
latest = w3.eth.get_block('latest')
print("== Latest ==")
print(latest)


person = get_context("example.sol", w3)

print("----- Get and Set Date -------")

a = person.functions.birthDate().call()
print(a)  # '0'
write_transact(person.functions.setBirthDate, [int(time.time())], w3)
a = person.functions.birthDate().call()
print(a)  # 'big nubmer'

print("----- Relationships -------")

# a = person.functions.names().call()
# print(a)  # '0'
a = person.functions.spouse().call()
print(a)  # '0'
person2 = get_context("example.sol", w3)
print(dir(person2))
# person2 = person2.encodeABI()
write_transact(person.functions.setSpouse, [person2.address], w3)
a = person.functions.spouse().call()
print(a)  # '0'
