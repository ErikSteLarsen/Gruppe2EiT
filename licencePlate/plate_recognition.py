#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
import os
import json
import time
from collections import OrderedDict

import requests

'''
Input: A relative input path from where this file is located (String).
Returns: The license plate that were visuble in the picture.

Note:   As of now, only takes care of pictures with one visible licence plate.
        If more than one is visible, it chooses the first one.
'''
def findLicensePlate(imagePath):
    result = []
    path = imagePath
    apiToken = 'ec115dfe234d37a339be12d3e69300715714ee2b'

    if len(path) == 0:
        print('File {} does not exist.'.format(path))
        return
    if not os.path.exists(path):
        return

    #for path in paths:
    response = None
    with open(path, 'rb') as fp:
        for _ in range(3):
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                files=dict(upload=fp),
                headers={'Authorization': 'Token ' + apiToken})
            if response.status_code == 429:  # Max calls per second reached
                time.sleep(1)
            else:
                break

    result.append(response.json(object_pairs_hook=OrderedDict))
    output = json.dumps(result, indent=2)

    numberPlate = result[0]['results'][0]['plate']

    return numberPlate





