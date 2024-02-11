# Password Manager CLI Tool

A simple command-line interface (CLI) tool for managing passwords securely.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is a lightweight CLI tool built in Python for managing passwords. It allows users to generate strong passwords, store them securely, and retrieve them when needed.

## Features

- **Password Generation**: Generate strong passwords with customizable length and character sets.
- **Secure Storage**: Encrypt and store passwords securely using the Fernet symmetric encryption scheme.
- **Simple CLI Interface**: Intuitive command-line interface for easy interaction.
- **Create and Retrieve Passwords**: Add new entries with usernames and passwords, and retrieve passwords for existing entries.
- **Environment Variable Configuration**: Utilizes environment variables for storing encryption keys, enhancing security.
- **JSON File Storage**: Passwords are stored in a JSON file locally.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bawejahritik/password-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-manager
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Generate a New Password**:

    ```bash
    python main.py -g
    ```

2. **Create a New Entry**:

    ```bash
    python main.py -c [account] [username] [password]
    ```

3. **Retrieve an Existing Password**:

    ```bash
    python main.py -r [account]
    ```

4. For detailed help and options, use the `--help` flag:

    ```bash
    python main.py --help
    ```
