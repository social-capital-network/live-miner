# The Project/Branch/Blockchain Header in markdown .md format
BLOCKCHAIN_HEADER = '# Project/Branch/Blockchain\n'

# The Transaction/Task/Ops Commit Line before all tx in an .md file
TX_COMMIT_LINE = '### Tx/Task/Ops - git commit\n'


def save_work():
    with open('master-blockchain.md', mode='w') as f:
        f.write(BLOCKCHAIN_HEADER)
        f.write('\n')
        f.write(TX_COMMIT_LINE)


save_work()
