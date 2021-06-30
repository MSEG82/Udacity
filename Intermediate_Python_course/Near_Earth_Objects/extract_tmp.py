# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 07:41:47 2021

@author: U324451
"""

"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
       
    extraction = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if not row["diameter"]:
                row["diameter"] = float("nan")
            else:
                row["diameter"] = float(row["diameter"])

            if not row["name"]:
                row["name"] = None
                
            if  row["pha"] in ["N", ""]:
                row["pha"] = False
            else: 
                row["pha"] = True
            try: 
                neo = NearEarthObject(pdes=row["pdes"], name=row["name"],diameter=row["diameter"],pha=row["pha"])
            except Exception as exc:
                print(exc)
                continue
            extraction.append(neo)
            
    return extraction
    


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches=[]
    with open(cad_json_path, 'r') as infile:
        reader = json.load(infile) 
        reader1 = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        for row in reader1:
            closeapproach = CloseApproach( des=row["des"],  cd=row["cd"], dist=float(row["dist"]), v_rel=float(row["v_rel"]) )
            approaches.append(closeapproach)
    
    return approaches
