


def read_vocab(vocab_file):
    vocab_map = dict()
    with open(vocab_file, 'r') as f:
        for line in f:
            w, i = line.strip().split(',')
            vocab_map[int(i)] = w
    return vocab_map


def write_poem(vocab_file, generator_file, out_file):
    print 'read index from', generator_file
    vocab_map = read_vocab(vocab_file)
    out_f = open(out_file, 'w')
    with open(generator_file, 'r') as f:
        for line in f:
            line = line.strip()
            idxs = [int(x) for x in line.split(' ')]
            words = [str(vocab_map.get(x)) for x in idxs]
            buffer = ' '.join(words)+'\n'
            out_f.write(buffer)
    out_f.close()
    print 'write poems into', out_file

if __name__ == '__main__':
    vocab_file = './save/vocab'
    generator_file = './save/generator_sample.txt'
    out_file = './save/genertor_poem.txt'
    write_poem(vocab_file, generator_file, out_file)

