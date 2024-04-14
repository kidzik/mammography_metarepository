import pickle
import json
from collections import defaultdict
import os

with open("sample_data/data.pkl", 'rb') as f:
    data = pickle.load(f)
print(json.dumps(data, indent=4))

studies = defaultdict(dict)

for img in os.listdir("sample_data/images"):
    im_name = img[:-4]
    study_id, image_id = im_name.split("_",1)
    image_id = image_id.replace("_","-")
    studies[study_id][image_id] = [im_name]
    
    print(study_id, image_id)

studies = list(studies.values())

for s in studies:
    s["horizontal_flip"] = "NO"
    s["cancer_label"] = {
        "left_malignant": 0,
        "left_benign": 0,
        "right_benign": 0,
        "right_malignant": 0,
        "unknown": 0,
        "benign": 0,
        "malignant": 0
    }

print(json.dumps(studies, indent=4))
with open('sample_data/data.pkl', 'wb') as handle:
    pickle.dump(studies, handle)
