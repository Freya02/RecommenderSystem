from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
def train_nlu(data, config, model_dir):
    traingData = load_data(data)
    trainer = Trainer(RasaNLUModelConfig(config))
    trainer.train(traingData)
    model_diretory = trainer.persist(model_dir,fixed_model_name="phonenlu")

def run_nlu(config):
    interpreter = Interpreter.load("./models/nlu/default/phonenlu")
    print(interpreter.parse(u"Best phone between 5000 to 10000")["intent_ranking"])

if __name__=="__main__":
    temp = {"pipeline": "spacy_sklearn","path": "./models/nlu","data": "./data/data.json"}
    train_nlu("./data/data.json",temp,"./models/nlu")
    run_nlu(temp)
