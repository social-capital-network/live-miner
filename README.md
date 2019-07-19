# Innovation Mining Protocol for Social Capital Networks

## High level social capital network diagram

![](/yuml/social-capital-network.svg)

## Recombinant Social Skills as Coins for Social Innovations

In order to speedup and distribute value mining to large population of local teams we propose replacement of the mining functions with solving QA test in git project repos.
Thus:

- miners are web workers with a specific set of skills/services (like the natural recombinant genes: rDNA/rRNA)
- coins are equivalent to the nature's universal energy currency ATP: https://en.wikipedia.org/wiki/ATP_synthase
- blocks are git contributions of multiple transactions like git commits which will pass a project defined test condition
- git projects are sets of QA tests
- natural economies are smart markets (https://en.wikipedia.org/wiki/Smart_market) where professionals and buisnesses collaborate in solving the top budgeted/voted projects they can find in their social networks.

## Continuous Ecosystem Growth - Agile Innovation Lifecycle

### DNA/ATP OS = Extreme Social Programming MVP: Mine (or Marry) Viral Program

![](/yuml/Innovation-Miner-Classes.svg)

## Agile Project mapping to Blockchain Classes

### Task_Transaction : Tuple

- Blockchain: transaction: (sender, recipient, amount) tuple
- AI Miner: task_transaction: (service, project, amount, duration, terms, contract) tuple

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

- Open ai economy UI at localhost:5000

ToDo:

- Add project / list of tasks to implement all the components of a functional business/economy organism

© Ianta Labs / MIT license
