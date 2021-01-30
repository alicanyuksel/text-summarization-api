# Text Summarization API Backend

For this API backend, [FlaskRESTful](https://flask-restful.readthedocs.io/en/latest/) has been used. It has no database and does not record inputs.

## Requirements

    pip install -r requirements.txt


## To run

The server will initialize the model [BART](https://github.com/pytorch/fairseq/tree/master/examples/bart) at the same time with the API server. So running the server can take 20-30 seconds. Don't worry about it! After that, you can send your request.

    python app.py

## Config

If you want to change the model used in the backend by default, you just need to put the name of model you want to use in [config.py](./config.py)

Take a look on the [BART repository](https://github.com/pytorch/fairseq/tree/master/examples/bart) to discover other models.

## Example

Send a post request to API:

    {
        text: "US rapper Snoop Dogg has been sued for $25 (£13m) by a make-up artist who claimed he and his entourage drugged and raped her two years ago. The woman said she was assaulted after a recording of the Jimmy Kimmel Live TV show on the ABC network in 2003. The rapper's spokesman said the allegations were 'untrue' and the woman was 'misusing the legal system as a means of extracting financial gain'. ABC said the claims had 'no merit'. The star has not been charged by police. The lawsuit, filed in Los Angeles on Friday, says the woman's champagne was spiked and she was then assaulted. The rapper's spokesperson said: 'Snoop will have the opportunity to prove in a court of law that [the alleged victim] is opportunistic and deceitful. 'We are confident that in this case, [the alleged victim's] claims against Snoop Dogg will be rejected.' The lawsuit names Snoop Dogg - real name Calvin Broadus - plus three associates, The Walt Disney Company and its parent company ABC Inc."
    }

Response :

    {
        summary_text: "Make-up artist claims she was drugged and raped two years ago. Rapper's spokesman said the allegations were 'untrue' and the woman was'misusing the legal system as a means of extracting financial gain' The lawsuit names Snoop Dogg plus three associates, The Walt Disney Company and its parent company ABC Inc."
    }
