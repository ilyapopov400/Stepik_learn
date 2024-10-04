class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, layer):
        self.next_layer = layer
        return self.next_layer


class Input(Layer):
    """
    - формирование входного слоя нейронной сети
    """

    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    '''
    - формирование полносвязного слоя нейронной сети
    '''

    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        return self

    def __next__(self):
        if self.network:
            ret = self.network
            self.network = self.network.next_layer
            return ret
        else:
            raise StopIteration


if __name__ == "__main__":
    network = Input(128)
    layer = network(Dense(network.inputs, 1024, 'linear'))
    layer = layer(Dense(layer.inputs, 10, 'softmax'))

    for x in NetworkIterator(network):
        print(x.name)

    nt = Input(12)
    layer = nt(Dense(nt.inputs, 1024, 'relu'))
    layer = layer(Dense(layer.inputs, 2048, 'relu'))
    layer = layer(Dense(layer.inputs, 10, 'softmax'))
    n = 0
    for x in NetworkIterator(nt):
        assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
        n += 1
    assert n == 4, "итератор перебрал неверное число слоев"
