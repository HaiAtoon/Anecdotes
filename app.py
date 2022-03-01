from parser import Parser
from storage import Storage
from flask import Flask, request
from typing import Dict

app = Flask(__name__)


@app.route("/add", methods=['POST'])
def add_evidence_endpoint():
    try:
        data = request.json
        if not data:
            return dict(message="No data provided"), 400
        data = data.get('evidence_data')
        if not data:
            return dict(message="No evidence_data provided"), 400
        success = 0
        errors = {}
        for i, evidence in enumerate(data, start=1):
            try:
                evidence_parser = Parser(evidence)
                evidence_parser.save_new_evidence()
                success += 1
            except Exception as e:
                errors[f"error_in_evidence_no_{i}"] = f"Exception-Type: {type(e).__name__}, " \
                                                      f"Exception-Message: {e.__name__} "
        if not errors:
            return dict(message="All evidences were successfully saved", count=success)
        return dict(message="Some evidences were not saved",
                    success_count=success, failed_count=len(errors), errors=errors), 400
    except Exception:
        return dict(message="Bad Request"), 400


@app.route("/get", methods=["GET"])
def get_evidence_endpoint():
    collection = request.args.get("collection")
    table = request.args.get("table")
    if not collection:
        return "Please specify the collection name", 400
    try:
        results = Storage.get(collection)
        if not results:
            return f"No data found for the collection {collection}"
        if table:
            return parse_to_table(results)
        return str(results)
    except Exception as e:
        return dict(message=f"Exception-Type: {type(e).__name__}, Exception-Message: {e.__name__} "), 400


def parse_to_table(data: Dict) -> str:
    """
    Parse the results data to a HTML table
    :param data: results data in list of dicts
    :return: str representation of HTML table
    """
    keys = data[0].keys()
    data_str = "<table border=1><tr>"
    data_str += ''.join(f"<th>{head}</th>" for head in keys)
    data_str += "</tr>"
    rows = ""
    for row in data:
        rows += "<tr>"
        rows += ''.join(f'<td>{row[k]}</td>' for k in keys)
        rows += "</tr>"
    return data_str + rows + "</table>"


if __name__ == "__main__":
    app.run()
