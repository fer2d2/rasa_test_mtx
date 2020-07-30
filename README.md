# Alma chatbot (Rasa)

> This is a chatbot built using the Rasa Stack (Rasa NLU + Rasa Core).

This bot is mainly designed to create requests in MTX. It is expected to include new functionalities such as the search for queries or the possibility of extending it to interact with third-party applications.

As it is based on Rasa, development is done using Python. To start developing, you will need to install `virtualenv` and use the `Makefile` commands.

- [Install `virtualen`](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Bootstrap

Having `virtualenv` and `make` installed, run:

```sh
make bootstrap
make install
```

## Running the project

To run the project using a command line chat, open **two terminals** and run:

```sh
# Terminal 1: run the Rasa Action Server
make run-endpoints
```

```sh
# Terminal 2: run the Rasa stories server with a CLI chat
make chat
```

## Debugging

The bot includes settings to debug using VSCode. Run the `Python: Rasa Action Server` configuration to start debugging your actions. As this will run an action server, be aware that no other action server is running.

## Dialog flow

- @WIP: to design deterministic dialog flows for complex forms (like request creation in MTX), we will use a custom policy (`IterativeActionPolicy`) and a custom action (`IterRequestAction`).

To take a look at a general diagram of the dialog flow, run `make visualize`.