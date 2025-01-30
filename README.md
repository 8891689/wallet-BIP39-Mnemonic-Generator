# BIP39 Mnemonic Generator & Cryptocurrency Address Derivation Tool

## Introduction
The **BIP39 Mnemonic Generator & Cryptocurrency Address Derivation Tool** It is a Python-based utility that allows users to generate BIP39 mnemonics and derive corresponding private keys, public keys and addresses for various cryptocurrencies based on these mnemonics. The tool is open source and is particularly suitable for use in tighter security environments.

## Features
- **Mnemonic Generation**: Create 12, 15, 18, 21, or 24-word mnemonics compliant with the BIP39 standard.
- **Key Derivation**: Derive private keys, public keys, and addresses for multiple cryptocurrencies using the BIP44 standard.
- **Multi-Currency Support**: Supports a variety of cryptocurrencies, including Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Solana, Stellar, Dash, and Bitcoin Cash, among others.
- **Customizable**: Supports generating multiple mnemonics and multiple addresses per mnemonic, with the option to add a passphrase.
- **Command-Line Interface (CLI)**: User-friendly CLI for easy integration into scripts and workflows.

## Prerequisites
- **Python or Python 3+**: Ensure Python is installed. Download it from the [official Python website](https://www.python.org/downloads/).

## Installation
Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/8891689/wallet-BIP39-Mnemonic-Generator.git
cd wallet-BIP39-Mnemonic-Generator
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies and avoid conflicts with other projects.

**Using `venv`:**
```bash
python3 -m venv venv
```

**Activate the Virtual Environment:**

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **On Unix or MacOS:**
  ```bash
  source venv/bin/activate
  ```

After activation, your terminal prompt should start with `(venv)`.

### 3. Install Dependencies
With the virtual environment activated, install the required Python libraries using `pip`:
```bash
pip install bip-utils
```
*Note*: The `argparse` module is part of Python's standard library and does not need to be installed separately.

## Usage
This tool operates via the command line. Below are the instructions and available options for using the script.

### Basic Usage
```bash
python mnemonic_derivation.py
```
This command will generate a 12-word mnemonic and derive an address for each supported cryptocurrency.

### Command-Line Arguments
- `-l, --length`: Length of the mnemonic (optional: 12, 15, 18, 21, 24). Default is 12.
  ```bash
  -l 24
  ```
- `-n, --number`: Number of mnemonics to generate. Default is 1.
  ```bash
  -n 5
  ```
- `-a, --addresses`: Number of addresses to generate per mnemonic. Default is 1.
  ```bash
  -a 3
  ```
- `-p, --passphrase`: Passphrase for the seed (optional).
  ```bash
  -p your_secure_passphrase
  ```

### Complete Command Example
Generate 3 mnemonics, each with 24 words, and derive 2 addresses for each mnemonic using a passphrase:
```bash
python mnemonic_derivation.py -l 24 -n 3 -a 2 -p mySecretPassphrase
```

### Example
Generate a single 12-word mnemonic:
```bash
python mnemonic_derivation.py
```
**Sample Output:**
```
Mnemonic 1: extend canoe level broken swear special unfold area popular asthma mango wood

Bitcoin Information:
Address 1:
  Private Key: 321537462e0bfe56c6a83499be65499704ed7b623cacae73f9f5fe7ad8e89f36
  WIF Private Key: Kxu4kQn3s8MBUDXHZCi2NB4PueipQxAutwEcKNdSJUxB2kPQLqJL
  Public Key: 030396af85747750de418f30010ffd56fc6e6a8c93061f9ccabd4242ab44aa96d1
  Address: 1DZ3ZN1xNFgrNt69wiAxMHimp9xcHxejPt

Ethereum Information:
Address 1:
  Private Key: 9351a6e393c53b7a8170a11933baba98f9c7cf14a599daa0046e3ae68c05af31
  Public Key: 03c3d36cdb5698dd23a0e1c0090fbf54e5432880d9b86091d2da008004b129e7c8
  Address: 0xfA393CD3Fa90e747a5C99004ddF106da7F93a845

Litecoin Information:
Address 1:
  Private Key: 8b450114ba0864e6140032807948a0a4d82497e1b9107df5a0da71cabcba60fc
  Public Key: 024c7cca34fcdb37df33aea258daf49a5bfde701188825e8b2ffdc983a3f8df79f
  Address: LU8PaQTjPVnKCaLof25U3ejBytfU7GfyhD

Dogecoin Information:
Address 1:
  Private Key: 373ed28ff7e3e65d45466fa89ae8a1be95f5ea5b9d100be722a19d92d41eb6fc
  Public Key: 02546011ad4c72b3b3d567fcf5932d945fb106d9311ef657cd0c603ba77c1cac96
  Address: DTJ9cnrcpMnS5YPoVQt1Y8VajJK2B5RH6q

... (Other supported cryptocurrencies)

Generate Multiple Mnemonics and Addresses
```bash
```
## Security Considerations

1. **Protect Your Mnemonics and Keys**: Mnemonics and derived keys can be used to access cryptocurrency funds. Ensure they are stored securely and never shared publicly.
2. **Backup**: Always back up your mnemonics and keys in a secure location.
3. **Use a Passphrase**: Adding a passphrase can provide an additional layer of security. Ensure the passphrase is strong and memorable.
4. **Use a Secure Environment**: After installing the necessary dependencies, disconnect from all networks, including VPNs (to prevent traffic hijacking, malware, remote monitoring, backdoors, etc.), Bluetooth, and others. Ensure there are no risks by, if necessary, wiping all system data and reinstalling the operating system. Run this tool in a trusted and secure environment to prevent unauthorized access.

## Adding More Currencies

### 1. Add Support for More Currencies in `mnemonic_derivation.py`
Edit the `mnemonic_derivation.py` script to include additional currencies.

```python
def derive_keys(mnemonic, passphrase="", num_addresses=1):
    """
    Derive multiple cryptocurrency private keys, public keys, and addresses based on the mnemonic and optional passphrase.
    """
    # Generate seed
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
    
    # Define supported coins
    coins = {
        "bitcoin": Bip44Coins.BITCOIN,
        "ethereum": Bip44Coins.ETHEREUM,
        "litecoin": Bip44Coins.LITECOIN,
        "dogecoin": Bip44Coins.DOGECOIN,
        "ripple": Bip44Coins.RIPPLE,
        "solana": Bip44Coins.SOLANA,
        "stellar": Bip44Coins.STELLAR,
        "dash": Bip44Coins.DASH,
        "bitcoin_cash": Bip44Coins.BITCOIN_CASH,
        
        # Add more currency support here.
        # "bitcoin_cash": Bip44Coins.BITCOIN_CASH,  # Uncomment if supported
    }
```

### 2. Supported Coins List
To add the currencies you need to generate, simply copy them into the code. Unsupported currencies will cause the script to error out; you can comment them out by adding a `#` at the beginning to allow the script to run normally.

```python
# Supported BIP coins
"akash_network": Bip44Coins.AKASH_NETWORK,
"algorand": Bip44Coins.ALGORAND,
"aptos": Bip44Coins.APTOS,
"arbitrum": Bip44Coins.ARBITRUM,
"avalanche": Bip44Coins.AVALANCHE,
"axelar": Bip44Coins.AXELAR,
"band_protocol": Bip44Coins.BAND_PROTOCOL,
"binance_chain": Bip44Coins.BINANCE_CHAIN,
"binance_smart_chain": Bip44Coins.BINANCE_SMART_CHAIN,
"bitcoin": Bip44Coins.BITCOIN,
"bitcoin_cash": Bip44Coins.BITCOIN_CASH,
"bitcoin_cash_simple_ledger_protocol": Bip44Coins.BITCOIN_CASH_SIMPLE_LEDGER_PROTOCOL,
"bitcoinsv": Bip44Coins.BITCOINSV,
"cardano": Bip44Coins.CARDANO,
"celestia": Bip44Coins.CELESTIA,
"celo": Bip44Coins.CELO,
"certik": Bip44Coins.CERTIK,
"cosmos": Bip44Coins.COSMOS,
"dash": Bip44Coins.DASH,
"dogecoin": Bip44Coins.DOGECOIN,
"dydx": Bip44Coins.DYDX,
"ecash": Bip44Coins.ECASH,
"elrond": Bip44Coins.ELROND,
"eos": Bip44Coins.EOS,
"ergo": Bip44Coins.ERGO,
"ethereum": Bip44Coins.ETHEREUM,
"ethereum_classic": Bip44Coins.ETHEREUM_CLASSIC,
"fantom_opera": Bip44Coins.FANTOM_OPERA,
"filecoin": Bip44Coins.FILECOIN,
"fetch_ai": Bip44Coins.FETCH_AI,
"harmony_one": Bip44Coins.HARMONY_ONE,
"huobi_heco_chain": Bip44Coins.HUOBI_HECO_CHAIN,
"iris_network": Bip44Coins.IRIS_NETWORK,
"kava": Bip44Coins.KAVA,
"kusama": Bip44Coins.KUSAMA,
"litecoin": Bip44Coins.LITECOIN,
"metis": Bip44Coins.METIS,
"monero": Bip44Coins.MONERO,
"nano": Bip44Coins.NANO,
"near_protocol": Bip44Coins.NEAR_PROTOCOL,
"neo": Bip44Coins.NEO,
"neutron": Bip44Coins.NEUTRON,
"nimiq": Bip44Coins.NIMIQ,
"okex_chain": Bip44Coins.OKEX_CHAIN,
"ontology": Bip44Coins.ONTOLOGY,
"optimism": Bip44Coins.OPTIMISM,
"osmosis": Bip44Coins.OSMOSIS,
"pi_network": Bip44Coins.PI_NETWORK,
"polkadot": Bip44Coins.POLKADOT,
"polygon": Bip44Coins.POLYGON,
"ripple": Bip44Coins.RIPPLE,
"secret_network": Bip44Coins.SECRET_NETWORK,
"solana": Bip44Coins.SOLANA,
"stafi": Bip44Coins.STAFI,
"stellar": Bip44Coins.STELLAR,
"sui": Bip44Coins.SUI,
"terra": Bip44Coins.TERRA,
"tezos": Bip44Coins.TEZOS,
"theta_network": Bip44Coins.THETA_NETWORK,
"tron": Bip44Coins.TRON,
"vechain": Bip44Coins.VECHAIN,
"verge": Bip44Coins.VERGE,
"zcash": Bip44Coins.ZCASH,
"zilliqa": Bip44Coins.ZILLIQA,

# Supported Substrate coins
"acala": Bip44Coins.ACALA,
"bifrost": Bip44Coins.BIFROST,
"chainx": Bip44Coins.CHAINX,
"edgeware": Bip44Coins.EDGEWARE,
"karura": Bip44Coins.KARURA,
"moonbeam": Bip44Coins.MOONBEAM,
"moonriver": Bip44Coins.MOONRIVER,
"phala_network": Bip44Coins.PHALA_NETWORK,
"plasm_network": Bip44Coins.PLASM_NETWORK,
"sora": Bip44Coins.SORA,
"generic_substrate_coin": Bip44Coins.GENERIC_SUBSTRATE_COIN,
```

## Sponsorship
If this project has been helpful to you, please consider sponsoring. It is the greatest support for me, and I am deeply grateful. Thank you.

- **BTC**: bc1qt3nh2e6gjsfkfacnkglt5uqghzvlrr6jahyj2k
- **ETH**: 0xD6503e5994bF46052338a9286Bc43bC1c3811Fa1
- **DOGE**: DTszb9cPALbG9ESNJMFJt4ECqWGRCgucky
- **TRX**: TAHUmjyzg7B3Nndv264zWYUhQ9HUmX4Xu4

## License
This project is licensed under the MIT License.
