from brownie import MockV3Aggregator, network
from scripts.helpful_scripts import get_account, DECIMALS, STARTING_PRICE


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed!")


def main():
    deploy_mocks()
