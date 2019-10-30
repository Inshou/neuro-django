import tensorflow as tf
import numpy as np
from .label_image import load_graph
from .label_image import read_tensor_from_image_file
from .label_image import load_labels
import time


def test_func(file_name):
    #file_name = "neuroapp/image.jpg"
    model_file = "neuroapp/tf_files/retrained_graph.pb"
    label_file = "neuroapp/tf_files/retrained_labels.txt"
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "Mul"
    output_layer = "final_result"

    graph = load_graph(model_file)
    t = read_tensor_from_image_file(file_name,
                                    input_height=input_height,
                                    input_width=input_width,
                                    input_mean=input_mean,
                                    input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);

    with tf.Session(graph=graph) as sess:
        start = time.time()
        results = sess.run(output_operation.outputs[0],
                           {input_operation.outputs[0]: t})
        end = time.time()
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)

    #template = "{} (score={:0.5f})"
    neuro_evaluate = {}
    for i in top_k:
        neuro_evaluate.update({labels[i]: results[i]})
        #print(template.format(labels[i], results[i]))

    return neuro_evaluate
