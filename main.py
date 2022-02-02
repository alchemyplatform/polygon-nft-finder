from flask import Flask, jsonify, render_template, request
from forms import DataTriggerForm
import os
import json
from web3 import Web3
import requests

# https://composer.alchemyapi.io?composer_state=%7B%22chain%22%3A2%2C%22network%22%3A401%2C%22methodName%22%3A%22alchemy_getAssetTransfers%22%2C%22paramValues%22%3A%5B%7B%22excludeZeroValue%22%3Atrue%2C%22fromBlock%22%3A%220x1664765%22%2C%22toAddress%22%3A%220xce90a7949bb78892f159f428d0dc23a8e3584d75%22%2C%22contractAddresses%22%3A%22%22%2C%22fromAddress%22%3A%220x0000000000000000000000000000000000000000%22%2C%22category%22%3A%5B%22erc721%22%5D%2C%22toBlock%22%3A%22%22%2C%22maxCount%22%3A%22%22%7D%5D%7D

try:
    ALCHEMY_KEY = "Rt4_MeHNZEE8mQWVi9Ct-uSppHNSDmOG"
except:
    print("Configure your Alchemy Key correctly as an environment variable or simply paste it as a string within the try statement")

MINT_ADDRESS = '0x0000000000000000000000000000000000000000'
MEDICI_ADDRESS = '0xce90a7949bb78892f159f428d0dc23a8e3584d75'

from_Block = '0x1664765'

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

def get_medici_info():
    total_burn = requests.post('https://polygon-mainnet.g.alchemy.com/v2/'+ALCHEMY_KEY, json={"jsonrpc": "2.0","id": 0,"method": "alchemy_getAssetTransfers","params": [{"fromBlock": from_Block,"toBlock": "latest","fromAddress": MINT_ADDRESS,"toAddress": MEDICI_ADDRESS,"category": ["erc721"]}]})

    json_response = total_burn.json()
    transfer_nums = len(json_response['result']['transfers'])-1

    last_mint_address = json_response['result']['transfers'][transfer_nums]['rawContract']['address']
    last_mint_block = json_response['result']['transfers'][transfer_nums]['blockNum']
    last_mint_hash= json_response['result']['transfers'][transfer_nums]['hash']
    return (last_mint_address, last_mint_block, last_mint_hash)

@app.route('/', methods=['GET', 'POST'])
def refresh():

    last_mint_address, last_mint_block, last_mint_hash = get_medici_info()

    print(last_mint_block)
    print(last_mint_address)

    form = DataTriggerForm()

    if request.method == 'POST':
        #num1 = form.num1.data
        last_mint_address, last_mint_block, last_mint_hash = get_medici_info()

    return render_template('index.html', form=form, last_mint_block=last_mint_block, last_mint_address=last_mint_address, last_mint_hash=last_mint_hash)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
