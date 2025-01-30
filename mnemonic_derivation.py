from bip_utils import (
    Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes,
    Bip39WordsNum
)
import argparse

def generate_mnemonic(length=12):
    """
    Generate a BIP39 mnemonic phrase of the specified length.
    Supported lengths are 12, 15, 18, 21, and 24 words.
    """
    if length not in [12, 15, 18, 21, 24]:
        raise ValueError("Mnemonic length must be 12, 15, 18, 21, or 24")
    num_words = Bip39WordsNum(length)  # Use enumeration member
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(num_words)
    return mnemonic

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
    
    keys = {}
    
    for coin_name, coin in coins.items():
        try:
            bip44_ctx = Bip44.FromSeed(seed_bytes, coin)
            account = bip44_ctx.Purpose().Coin().Account(0)
            change = account.Change(Bip44Changes.CHAIN_EXT)
            
            keys[coin_name] = []
            for i in range(num_addresses):
                address = change.AddressIndex(i)
                private_key_hex = address.PrivateKey().Raw().ToHex()
                public_key_hex = address.PublicKey().RawCompressed().ToHex()
                addr = address.PublicKey().ToAddress()
                
                # For Bitcoin, generate WIF private key
                if coin == Bip44Coins.BITCOIN:
                    private_key_wif = address.PrivateKey().ToWif()
                else:
                    private_key_wif = None
                
                key_info = {
                    "private_key": private_key_hex,
                    "public_key": public_key_hex,
                    "address": addr
                }
                
                if private_key_wif:
                    key_info["wif_private_key"] = private_key_wif
                
                keys[coin_name].append(key_info)
                
        except Exception as e:
            print(f"Warning: Unable to process coin '{coin_name}': {e}")
            continue  # Skip current coin and continue with the next one
    
    return keys

def main():
    """
    Main function to generate mnemonic phrases and derive keys and addresses.
    Supports generating multiple random mnemonics and multiple addresses per mnemonic.
    """
    parser = argparse.ArgumentParser(description="BIP39 Mnemonic Generator and Cryptocurrency Address Derivation Tool")
    parser.add_argument("-l", "--length", type=int, choices=[12, 15, 18, 21, 24], default=12,
                        help="Mnemonic length (12, 15, 18, 21, 24), default is 12")
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Number of mnemonics to generate, default is 1")
    parser.add_argument("-a", "--addresses", type=int, default=1,
                        help="Number of addresses to generate per mnemonic, default is 1")
    parser.add_argument("-p", "--passphrase", type=str, default="",
                        help="Passphrase for the seed (optional)")
    
    args = parser.parse_args()

    try:
        for i in range(args.number):
            mnemonic = generate_mnemonic(args.length)
            print(f"\nMnemonic {i+1}: {mnemonic}")
            
            keys = derive_keys(mnemonic, passphrase=args.passphrase, num_addresses=args.addresses)
            
            for coin, details in keys.items():
                print(f"\n{coin.capitalize()} Information:")
                for j, key in enumerate(details, start=1):
                    print(f"Address {j}:")
                    print(f"  Private Key: {key['private_key']}")
                    if 'wif_private_key' in key:
                        print(f"  WIF Private Key: {key['wif_private_key']}")
                    print(f"  Public Key: {key['public_key']}")
                    print(f"  Address: {key['address']}")
                    
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

if __name__ == "__main__":
    main()
