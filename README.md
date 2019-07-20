# Innovation Mining Protocol for Social Capital Networks

## High level social capital network diagram

![](/yuml/social-capital-network.svg)

## Recombinant Skills and Services as Coins of Social Innovation

In order to speedup and distribute value mining to large population of local teams we propose replacement of the mining functions with solving QA test in git project repos.
Thus:

- Users and miners(innovators) are people with a specific set of skill coins
- the skill coins are equivalent to genes with a cost value linked to nature's universal energy currency ATP: https://en.wikipedia.org/wiki/Adenosine_triphosphate
- blocks are git contributions of multiple transactions like git commits which will pass a project defined test condition
- projects are github repos defined as a sets of QA tests
- economies are smart markets (https://en.wikipedia.org/wiki/Smart_market) of project/jobs and service/skills where students, professionals and buisnesses collaborate in solving the top budgeted/voted projects they can find in their social networks.

## Continuous Ecosystem Progress - Agile Innovation Lifecycle

Such Ecosystems ( Markets, Nations ) progress by extending the number of services or skills immediatelly available to address the top projects (market or environment challenges or opportunities).
All participants can calculate their own Progress (growth in number of skills) Investments (Innovation Projects that produce better/skills and services) or even a evolutionary speed as the number of new skills/services innovated in a period of time.
The Progress of the web ecosystem can be compared to the Progress in the number of genes added to the natural genoms in the past Billion year - after Nature invented the Dynamic Monetary system - Mitochondria used now by nearly all live cells on Earth. (https://en.wikipedia.org/wiki/Mitochondrion Mitochondria are the producers of the ATP miners: ATP synthase https://en.wikipedia.org/wiki/ATP_synthase )

### DNA/RNA/ATP OS = Extreme Social Programming MVP: Mine (or Marry) Viral Programs

One can either "marry" the best skills/services (genes) she/he can find in the social network or openly or privatelly could try to mine/coin a better/faster/cheaper skill or service by initiating and promoting/funding a new project in her social network.

![](/yuml/Innovation-Miner-Classes.svg)

## Agile Project mapping to Blockchain Classes

### Task_Transaction : Tuple

- Blockchain: transaction: (sender, recipient, amount, signature) tuple
- Innovation Miner: task_transaction: (service, project, amount, duration, result, start, finish, contract) tuple

### Open_Tasks_Transactions : List []

### Sprint_Block : Dictionary {}

### Project_Blockchain : List []

### Innovator_Node : Set {}

## Miner Server Installation

- Clone ai-eco-miner repo and install Anaconda Navigator
- Create Conda ucoin environment:

```bash
$ conda env create -n ucoin -f=ucoin.yml
```

- Activate ucoin environment

```bash
$ conda activate ucoin
```

- Run ai economy miner server:

```bash
$ python node.py
```

or start multiple miner servers on different ports:

```bash
$ python node.py -p 5001
```

- Open UI at localhost:5000

## Credits:

This project extends the excellent educational Python Blockchain developed by Maximilian Schwarzmuller in his popular Udemy Course:
[Learn Python by Building a Blockchain & Cryptocurrency](https://www.udemy.com/learn-python-by-building-a-blockchain-cryptocurrency/)

## Contributors:

- Stefan Ianta - initiator
- Alex Ianta - code reviews

© Ianta Labs / MIT license
