from flask_restful import Resource, reqparse
from flask_cors import CORS, cross_origin
from config import model_name, tokenizer_name

# ML model
#from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM



class BartModel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("text", required=True,
                        help="This field cannot be left blank!")

    def post(self, id_):
        data = BartModel.parser.parse_args()

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(tokenizer_name)

        text_to_summarize = data["text"]

        # Encoding the inputs and passing them to model.generate()

        inputs = tokenizer.batch_encode_plus([text_to_summarize], return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'], early_stopping=True)

        # get summarized text from BART
        bart_summary = tokenizer.decode(
            summary_ids[0], skip_special_tokens=True)

        json_return = {
            "summary_text": bart_summary
        }

        return json_return, 201
