# Snapster Bot

SnapsterBot is an asynchronous Python bot built to interact with the Sn4pst3r API. It allows users to automate tasks such as claiming daily bonuses, mining bonuses, league bonuses, and completing quests.

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/cucumber_scripts)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cucumber-pickle/Cucumber)

## What is Snapster ?
***Snapster - Trading App :*** easy-to-use telegram app for discovering & trading hot tokens Snapster Points campaign is live with $SNAPS: Airdrop confirmed! Make sure you follow us on our telegram channel and group to get the latest information about this airdrop.

### Register : https://t.me/snapster_bot?start=ref_yOOxVl4ho97nDJ

## Features

- **Claim daily bonus**: Automates the daily bonus claiming process.
- **Claim league bonus**: Automatically claims league bonus if it's unclaimed.
- **Claim mining bonus**: Claims bonuses for mining.
- **Complete quests**: Automates quest completion by either starting new quests or claiming bonuses from finished quests.
- **Referral points**: Claims referral points.

## Requirements

- Python 3.8+
- Libraries:
  - `aiohttp`
  - `colorama`
  - `urllib.parse`
  - `json`
  - Custom modules in `src/` such as `headers`, `deeplchain`

## Setup
1. Clone the repository:

```bash
git clone https://github.com/nadirasaid8/SnapsterCum.git
```
2. Navigate to the project directory:

```bash
cd SnapsterCum
```
3. Ensure that you have the following directory structure:

```bash
snapster-bot/
├── src/
│   ├── __init__.py
│   ├── headers.py
│   ├── deeplchain.py
│   └── core.py
├── proxies.txt
├── main.py
├── data.txt
├── requirements.txt
└── README.md
```

4. Install the Dependencies:

    Use `pip` to install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a file called proxies.txt (optional):

If you plan on using proxies, create a proxies.txt file with the following format:

```ruby
username:password@host:port
username:password@host:port
```

6. Configure the config.json to include necessary options:

```json
{
    "use_proxy": false,
    "auto_complete_tasks": false,
    "account_delay": 5,
    "loop_countdown": 3800
}
```  

7. Prepare the Authorization Tokens:

    before starting the bot you must have your own initdata / query id telegram! 

    - Use PC/Laptop or Use USB Debugging Phone
    - open the `Sn4pst3r bot miniapp`
    - Inspect Element `(F12)` on the keyboard
    - at the top of the choose "`Application`" 
    - then select "`Session Storage`" 
    - Select the links "`Sn4pst3r`" and "`tgWebAppData`"
    - Take the value part of "`tgWebAppData`"
    - take the part that looks like this: 

```txt 
query_id=xxxxxxxxx-Rxxxxuj
```
8. add it to `data.txt` file or create it if you dont have one

You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id1=xxxxxxxxx-Rxxxxuj
query_id2=xxxxxxxxx-Rxxxxuj
query_id3=xxxxxxxxx-Rxxxxuj
```

## Usage

Run the bot using the following command:

```bash
python main.py
```

## Proxy Support
To enable proxy support, ensure that:

- The use_proxy setting in config.json is set to true.
- The proxies.txt file contains valid proxy information in the format username:password@host:port.


## How to get tgWebAppData (query_id / user_id)

1. Login telegram via portable or web version
2. Launch the bot
3. Press `F12` on the keyboard 
4. Open console
5. Сopy this code in Console for getting tgWebAppData (user= / query=):

```javascript
copy(Telegram.WebApp.initData)
```

6. you will get data that looks like this

```
query_id=AA....
user=%7B%22id%....
```
7. add it to `data.txt` file or create it if you dont have one


## This bot helpfull?  Please support me by buying me a coffee: 
``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - BSC (BEP 20)

``` UQBiNbT2cqf5gLwjvfstTYvsScNj-nJZlN2NSmZ97rTcvKz0 ``` - TON

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - Optimism

``` THaLf1cdEoaA73Kk5yiKmcRwUTuouXjM17 ``` - TRX (TRC 20)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please contact [CUCUMBER TG CHAT](https://t.me/cucumber_scripts_chat)