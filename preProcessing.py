import os.path

DATADIR = "./poem"


def create_vocab(train_file):
    vocab = set()
    with open(train_file, 'r') as f:
        for line in f:
            line = line.replace('\t', ' ').split()
            if len(line) == 20:
                for w in line:
                    vocab.add(w)
    return vocab


def map_data(vocab_map, in_file, out_file):
    outF = open(out_file, 'w')
    with open(in_file, 'r') as f:
        for line in f:
            idxs = []
            line = line.replace('\t', ' ').split()
            if len(line) == 20:
                for w in line:
                    idx = vocab_map.get(w)
                    idxs.append(idx)
            if idxs:
                buffer = ' '.join([str(x) for x in idxs]) + '\n'
                outF.write(buffer)
    outF.close()

def read_poem(train_file, valid_file, test_file, vocab_file):
    train_vocab = create_vocab(train_file)
    valid_vocab = create_vocab(valid_file)
    test_vocab = create_vocab(test_file)
    vocab = train_vocab.union(valid_vocab)
    vocab = vocab.union(test_vocab)
    vocab_map = dict()
    with open(vocab_file, 'w') as f:
        for i, w in enumerate(vocab):
            vocab_map[w] = i
            buffer = w + ',' + str(i) + '\n'
            f.write(buffer)

    print 'vocab size:', len(vocab)
    map_data(vocab_map, train_file, "./save/train")
    map_data(vocab_map, train_file, "./save/real_data.txt")
    map_data(vocab_map, valid_file, "./save/valid")
    map_data(vocab_map, test_file, "./save/test")

if __name__ == '__main__':
    train_file = os.path.join(DATADIR, "qtrain")
    valid_file = os.path.join(DATADIR, "qvalid")
    test_file = os.path.join(DATADIR, "qtest")
    vocab_file = './save/vocab'
    read_poem(train_file, valid_file, test_file, vocab_file)