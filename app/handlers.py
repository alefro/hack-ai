from flask import request, render_template
from flask_restful import Resource
import json

class BaseHandler(Resource):
    def __init__(self):
        pass


class IndexHandler(BaseHandler):
    def dispatch_request(self):
        return render_template('index.html')


class PipelineHandler(BaseHandler):
    def dispatch_request(self):
        sol_treshold_lo = -5
        sol_treshold_hi = 0
        dist_treshold = 1

        smiles = ["CCCS(=O)(=O)Nc1ccc(F)c(c1F)C(=O)c2c[nH]c3c2cc(cn3)c4ccc(Cl)cc4",
                  "CC(C)(C)c1nc(c(s1)c2ccnc(n2)N)c3cccc(c3F)NS(=O)(=O)c4c(cccc4F)F",
                  "CNC(=O)c1cc(ccn1)Oc2ccc(cc2)NC(=O)Nc3ccc(c(c3)C(F)(F)F)Cl",
                  "C[C@@H](CNc1nccc(n1)c2cn(nc2c3cc(cc(c3F)NS(=O)(=O)C)Cl)C(C)C)NC(=O)OC"]
        print (request.data)
        data = request.json
        target = data.get(u'target')

        smiles = generate_molecules()
        # smiles = filter_solubility(smiles, sol_treshold_lo, sol_treshold_hi)
        # smiles = filter_bbb(smiles)
        # smiles = filter_distance(smiles, target, dist_treshold)

        return json.dumps(smiles)


def generate_molecules():
    import subprocess
    output = subprocess.Popen(
        ["python", "/home/devel/char-rnn-tensorflow/sample.py", "--save_dir", "/home/devel/smiles2", "--prime", "c", "-n", "10000"],
        stdout=subprocess.PIPE).communicate()[0]
    smiles = output.split("\n")
    smiles = smiles[:-2]
    return smiles

def filter_solubility(smiles, treshold_lo, treshold_hi):
    pass

def filter_bbb(smiles):
    pass

def filter_distance(smiles, target, dist_treshold):
    pass
