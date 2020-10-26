import keras
import pkgutil
import json


def pretrained_model_load():
    json_file = pkgutil.get_data("audioanalytics", "models/model.json")
    # loaded_model_json = json_file.read()
    loaded_model_json = json.dumps(json.loads(json_file.decode('utf-8')))
    # json_file.close()

    loaded_model = keras.models.model_from_json(loaded_model_json)
    print(loaded_model)
    print(type(loaded_model))
    # loaded_model.load_weights(pkgutil.get_data(
    #     "audioanalytics", "models/model.h5"))

    return loaded_model


# def model_load(): # using pkg_resources
#     json_path = pk
#     json_file = open(json_path, 'r')
#     loaded_model_json = json_file.read()
#     json_file.close()
#     loaded_model = keras.models.model_from_json(loaded_model_json)
#     loaded_model.load_weights(
#         "D:\\PyCharm Projects\\audioanalytics\\audioanalytics\\model.h5")
#     return loaded_model
