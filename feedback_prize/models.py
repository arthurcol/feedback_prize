### MODULE THAT SAVES MODELS THAT WERE TRAINED ###

import tensorflow as tf
from transformers import TFBertModel

DISCOURSE_LEN = 256

pretrained_bert = TFBertModel.from_pretrained("bert-base-uncased")

def create_sentence_based():
    input_ids = tf.keras.layers.Input(shape=(DISCOURSE_LEN,),dtype='int32')
    attention_mask = tf.keras.layers.Input(shape=(DISCOURSE_LEN,),dtype='int32')
    x = pretrained_bert({'input_ids':input_ids,
                        'attention_mask':attention_mask})[0]
    x = tf.keras.layers.GlobalAveragePooling1D()(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    x = tf.keras.layers.Dropout(.2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dropout(.2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(32, activation='relu')(x)
    output = tf.keras.layers.Dense(8, activation='softmax',name='outputs')(x)

    pretrained_bert.trainable=False

    model = tf.keras.Model(inputs={'input_ids':input_ids,
                                'attention_mask':attention_mask},
                        outputs=output)

    return model

def compiler_for_sentence_based(model):
    loss = tf.keras.losses.CategoricalCrossentropy(name='categorical_crossentropy')
    acc = tf.keras.metrics.CategoricalAccuracy(name='accuracy')

    initial_learning_rate = 0.1

    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
                                        initial_learning_rate,
                                        decay_steps=1000,
                                        decay_rate=0.6,
                                        staircase=True)

    opt = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
    model.compile(optimizer=opt,loss=loss,metrics=[acc])
    return model
