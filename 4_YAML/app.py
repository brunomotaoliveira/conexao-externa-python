import yaml

if __name__ == '__main__':

    stream = open("test.yaml", "r")
    dictionary = yaml.safe._load(stream)

    for key, value in dictionary.items();
        print(key: " : " + str(value))