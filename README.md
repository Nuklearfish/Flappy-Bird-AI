# Flappy Bird AI
Flappy Bird with NEAT and PyTorch DQN AI

## Installation

Zur Installation dieser Umgebung wird zunächst vorausgetzt, dass eine aktuelle Version von Python und pip zur Installation weiterer Pakete bereits installiert ist.

Ist dies der Fall, müssen nach dem klonen dieses Repositorys Abhängigkeiten für Deep Q-Learning installiert werden. Dies kann mit den folgenden Befehlen getan werden:
```bash
pip install flappy-bird-env
pip install matplotlib
pip install torch
pip install pyyaml
```
Die für NEAT erforderlichen Abhängigkeiten können durch die folgenden Befehle installiert werden.
```bash
pip install flappy-bird-env
pip install matplotlib
pip install torch
pip install pyyaml
```

## Befehlsreferenz

#### Deep Q-Learning


| Befehl     | Wirkung                |
| :--------  | :--------------------- |
| `python agent.py flappybird24h`  | Führt das unter dem Namen (in hyperparameters.yml) "flappybird24h"  Trainierte Modell aus |
| `python agent.py flappybird24h --train`  | Startet das Traing für das Modell Namen "flappybird24h" |

#### NEAT


| Befehl     | Wirkung                |
| :--------- | :--------------------- |
| `python flappy_bird_neat.py ` | Startet training mit NEAT |




## Weitere Informationen

Weitere informationen finden Sie ind den Repositories auf denen diese Umgebung basiert:

https://github.com/techwithtim/NEAT-Flappy-Bird/tree/master

und

https://github.com/johnnycode8/dqn_pytorch?tab=readme-ov-file
