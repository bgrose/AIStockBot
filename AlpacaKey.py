class AlpacaKey(REST):
    def __int__(self):
        super().__init__(
            key_id='KEY',
            secret_key='KEY',
            base_url='https://paper-api.alpaca.markets'
        )