from torch import nn

class MultipleInputSequential(nn.Sequential):
    def forward(self, *inputs):
        for module in self._modules.values():
            if type(inputs) == tuple:
                output = module(*inputs)
            else:
                inputs = module(inputs)
        return output