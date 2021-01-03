from number_network import NumberNetwork
from canvas import Canvas

if __name__ == "__main__":
    network = NumberNetwork()
    acc = 0
    while True:
        network.train_with_dataset()
        new_acc = network.test_with_dataset()
        if new_acc <= acc:
            break
        acc = new_acc
        network.lr /= 1.1
        print(acc)
    print(network.test_with_dataset())


    # c = Canvas()
    # c.draw()
    # ip, label = c.get_input()
    # print(network.test(ip, label))
