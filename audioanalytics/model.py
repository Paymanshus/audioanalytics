import keras
import pkgutil  # dependency covered as part of setuptools?
import json
import importlib.resources
import pkg_resources


def pretrained_model_load():
    json_file = pkgutil.get_data("audioanalytics", "models/model.json")
    loaded_model_json = json.dumps(json.loads(json_file.decode('utf-8')))

    loaded_model = keras.models.model_from_json(loaded_model_json)

    with importlib.resources.path("audioanalytics", "model.h5") as p:
        h5_path = p

    loaded_model.load_weights(h5_path)
    # loaded_model.load_weights(pkgutil.get_data(
    #     "audioanalytics", "models/model.h5"))

    return loaded_model


# def model_load(): # using pkg_resources
    # with importlib.resources.path("audioanalytics", "model.json") as p:
    #     json_path = p
    # json_file = open(json_path, 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
#     loaded_model = keras.models.model_from_json(loaded_model_json)
#     loaded_model.load_weights(
#         "D:\\PyCharm Projects\\audioanalytics\\audioanalytics\\model.h5")
#     return loaded_model
