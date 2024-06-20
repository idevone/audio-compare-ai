import torch
import numpy as np
import matplotlib.pyplot as plt
from bindsnet.encoding import PoissonEncoder
from bindsnet.network import Network
from bindsnet.network.nodes import Input, LIFNodes
from bindsnet.network.topology import Connection
from bindsnet.learning import PostPre
from bindsnet.network.monitors import Monitor


# Параметры сети
input_size = 13  # Размерность MFCC признаков
chroma_size = 12  # Размерность хрома признаков
hidden_size = 100
num_timesteps = 1000
dt = 1.0  # Шаг времени симуляции

# Создание сети
network = Network()

# Входные слои для MFCC и хрома
input_mfcc_layer = Input(n=input_size)
input_chroma_layer = Input(n=chroma_size)
network.add_layer(input_mfcc_layer, name="input_mfcc")
network.add_layer(input_chroma_layer, name="input_chroma")

# Скрытый слой
hidden_layer = LIFNodes(n=hidden_size)
network.add_layer(hidden_layer, name="hidden")

# Соединения между слоями
connection_mfcc = Connection(source=input_mfcc_layer, target=hidden_layer)
connection_chroma = Connection(source=input_chroma_layer, target=hidden_layer)
network.add_connection(connection_mfcc, source="input_mfcc", target="hidden")
network.add_connection(connection_chroma, source="input_chroma", target="hidden")

# Монитор для отслеживания спайков
monitor = Monitor(obj=hidden_layer, state_vars=["s"])
network.add_monitor(monitor, name="hidden_monitor")

