from common import Config, VocabType
from model import Model
import sys

from extractor import Extractor

from interactive_predict import InteractivePredictor

class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        
if __name__ == '__main__':
    args = Bunch(data_path=None, test_path=None, save_path=None, load_path='models/java14_model/saved_model_iter8.release', release=None)
    config = Config.get_default_config(args)

    model = Model(config)

    SHOW_TOP_CONTEXTS = 10
    MAX_PATH_LENGTH = 8
    MAX_PATH_WIDTH = 2
    JAR_PATH = 'JavaExtractor/JPredict/target/JavaExtractor-0.0.1-SNAPSHOT.jar'

    model.predict([])

    path_extractor = Extractor(config, jar_path=JAR_PATH, max_path_length=MAX_PATH_LENGTH, max_path_width=MAX_PATH_WIDTH)
    input_filename = 'Input.java'
    predict_lines, hash_to_string_dict = path_extractor.extract_paths(input_filename)

    results = model.predict(predict_lines)
    print(results)

    model.close_session()
