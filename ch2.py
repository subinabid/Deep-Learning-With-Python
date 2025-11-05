import marimo

__generated_with = "0.17.7"
app = marimo.App()


@app.cell
def _():
    from tensorflow.keras.datasets import mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    return test_images, test_labels, train_images, train_labels


@app.cell
def _(train_images):
    train_images.shape
    return


@app.cell
def _(train_images):
    len(train_images)
    return


@app.cell
def _(train_labels):
    train_labels
    return


@app.cell
def _(test_images):
    test_images.shape
    return


@app.cell
def _(test_images):
    len(test_images)
    return


@app.cell
def _(test_labels):
    test_labels
    return


@app.cell
def _():
    from tensorflow import keras
    from tensorflow.keras import layers
    model = keras.Sequential([
        layers.Dense(512, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='rmsprop',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return (model,)


@app.cell
def _(test_images, train_images):
    train_images_1 = train_images.reshape((60000, 28 * 28))
    train_images_1 = train_images_1.astype('float32') / 255
    test_images_1 = test_images.reshape((10000, 28 * 28))
    test_images_1 = test_images_1.astype('float32') / 255
    return test_images_1, train_images_1


@app.cell
def _(model, train_images_1, train_labels):
    model.fit(train_images_1, train_labels, epochs=5, batch_size=128)
    return


@app.cell
def _(model, test_images_1):
    test_digits = test_images_1[0:10]
    predictions = model.predict(test_digits)
    predictions[0]
    return (predictions,)


@app.cell
def _(predictions):
    predictions[0].argmax()
    return


@app.cell
def _(predictions):
    predictions[0][7]
    return


@app.cell
def _(test_labels):
    test_labels[0]
    return


@app.cell
def _(model, test_images_1, test_labels):
    test_loss, test_acc = model.evaluate(test_images_1, test_labels)
    print('Test accuracy:', test_acc)
    return


if __name__ == "__main__":
    app.run()

