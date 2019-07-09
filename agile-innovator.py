import json

from project import Project, Sprint

# The Project/Branch/Blockchain Header in markdown .md format
BLOCKCHAIN_HEADER = '# Project/Branch/Blockchain\n'

# The Status Header - Do we need this? Here

# The Transaction/Task/Ops Commit Line before all tx in an .md file
TX_COMMIT_LINE = '### Tx/Task/Ops - git commit\n'

# Our starting innovation for the innovation chain (block => innovation/project)
genesis_innovation = {
    'title': 'Project Title',
    'tags': ''
    'subtitle': 'one liner',
    'description': 'README.md',
    'privacy': '',
    'status': '',
    'created_at': '',
    'last_update': '',
    'owner': 'job_creator_email',
    'project_manager': 'pm_email',
    'schedules': {},
    'todos': {},
    'issues': {},
    'risks': {},
    'parent_project': ''
    'subprojects': {},
    'languages': [],
    'contributors': [],
    'contributions': {},
    'repositories': {},
    'environments': {},
    'config_files': {},
    'command_files': {},
    'budget': 0,
    'investment': 5,  # the famous 5cents for expressing the problem/project
    'timeframe': '',
    'branches': [],
    'contexts': {},
    'tests': {},
    'test_proof': {},
    'license': 'MIT'
    'terms': {},
    'conditions': {},
    'previous_hash': '',
    'index': 0,
}

# Initializing the innovation chain
innovationchain = []

# ProjectChain is equivalent to a Branch in a Git Repo
# A ProjectChain / Branch is a chain of Agile Sprint/Blocks
updated_projectchain = []
for sprint in projectchain:
    converted_tx = [OrderedDict(
        [('sender', tx['sender']), ('recipient',
                                    tx['recipient']), ('amount', tx['amount'])]
    ) for tx in block['transactions']]
    updated_sprint = Sprint(
        sprint['index'], sprint['previous_hash'], converted_tx, sprint['proof'], sprint['timestamp'])
    updated_projectchain.append(updated_sprint)
innovationchain = updated_projectchain
open_transactions = json.loads(file_content[1])
# above line is equivalent line 43 in Max' blockchain.py / Module 146 - Adding a "Block" Class to the Blockchain


def load_work():
    try:
        with open('master-blockchain.md', mode='r') as f:
            file_content = f.readlines()
            # [:-1] - reading all string except the last character
            # blockchain = json.loads(file_content[0][:-1])
            blockchain_header = file_content[0]
            transaction_header = file_content[2]

    except (IOError, IndexError):
        innovation_chain = [genesis_innovation]
        open_transactions = []
    finally:
        print('Cleanup!')

# load_work()


def save_work():
    try:
        with open('master-blockchain.md', mode='w') as f:
            # Write Header(s)
            # or f.write(json.dumps(blockchain))
            f.write(BLOCKCHAIN_HEADER)
            f.write('\n')
            f.write(TX_COMMIT_LINE)
    except IOError:
        print('Saving failed!')


save_work()
