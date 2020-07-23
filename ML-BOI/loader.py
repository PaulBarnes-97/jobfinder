import tensorflow
from keras.datasets import cifar10
import keras.utils as k_utils
from keras.models import load_model
import numpy as np
from keras.optimizers import SGD

def train(numEpoch):
    labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    (xtrain, ytrain), (xtest, ytest) = cifar10.load_data()

    xtrain = xtrain.astype('float32') / 255.0
    #xtest = xtest.astype('float32') / 255.0

    ytrain= k_utils.to_categorical(ytrain)
    #ytest= k_utils.to_categorical(ytest)


    model = load_model("Image_Classifier.h5")
    model.compile(optimizer=SGD(lr=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
    with tensorflow.device('GPU:0'):
        model.fit(x=xtrain, y=ytrain, epochs=numEpoch, batch_size=32)
    model.save(filepath=("Image_Classifier.h5"))

def test():
    labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    (xtrain, ytrain), (xtest, ytest) = cifar10.load_data()

    #xtrain = xtrain.astype('float32') / 255.0
    xtest = xtest.astype('float32') / 255.0

    #ytrain = k_utils.to_categorical(ytrain)
    ytest = k_utils.to_categorical(ytest)

    model = load_model("Image_Classifier.h5")

    with tensorflow.device('GPU:0'):
        #result = model.evaluate(x=xtest, y=ytest)
        test_img_data = np.asarray([xtest[0]])
    predict = model.predict(x=test_img_data)
    max_index = np.argmax(predict[0])
    print("prediction:", labels[max_index])
def main():
    valid = False
    while valid == False:
        numEpoch = int(input("How many epochs will you run: "))
        if numEpoch >= 1:
            train(numEpoch)
            valid == True
            break
        elif numEpoch == 0:
            valid == True
            break
        else:
            valid == False

    test()
main()

