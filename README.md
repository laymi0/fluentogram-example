# Fluentogram Multilingual Bot Example

This repository provides an example of how to add multilingual support to your Telegram bot using [Fluentogram](https://github.com/Arustinal/fluentogram).

## Overview

This example demonstrates how to easily manage multilingual support in a Telegram bot using Fluentogram. The key features of this example include:

- **Automatic language detection**: The bot detects the user's language based on their profile settings.
- **Localized messages**: The Fluentogram library is used to manage and load message templates in different languages.
- **Fallback language**: A default language is set to be used when the preferred language translation is unavailable.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/laymi0/fluentogram-example
    cd fluentogram-example
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Add your bot token**: Open the `.env.example` file, rename it to `.env`, and replace `BOT_TOKEN` with the token you obtained from BotFather.

2. **Language Configuration**: In the `locales` folder, you’ll find files for each supported language. Add your translations as needed.

## Running the Bot

To run the bot, execute the following command:

```bash
 python main.py
```
