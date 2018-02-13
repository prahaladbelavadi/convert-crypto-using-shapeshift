
Reference:
- [Using shapeshift to convert between cryptocurrencies](https://news.earn.com/how-to-use-the-shapeshift-api-and-python-to-convert-between-different-cryptocurrencies-1ae14ff2ff34)


- To get a list of coins
  ```bash
    curl https://shapeshift.io/getcoins
  ```

Get requests include
- getcoins: Returns the list of available coins.
- rate: Returns the exchange rate between two cryptocoins.
- limit: Returns the maximum amount of coin you can deposit.
- marketinfo: Returns the pair, rate, limit, minimum limit, and miner fee of a particular market.
- recenttx: List of the most recent transactions.
- txStat: Status of the most recent transaction at an address.
- timeremaining: Time remaining to deposit on a fixed transaction.
- txbyapikey: Allows vendors to get a list of all transactions that have ever been done using a specific API key.
- txbyaddress: Allows vendors to get a list of all transactions that have ever been sent to one of their addresses.
- validateAddress: Verifies that an address with work against a particular blockchain.

Post requests include:
- shift: Creates a normal transaction and return a deposit address.
- mail: Sends the receipt of a particular transaction to the requested email.
- sendamount: Similar to shift except it allows you to request a fixed amount to the withdrawal address.
- cancelpending: Cancels a pending transaction.
