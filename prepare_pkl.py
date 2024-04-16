import pickle
import json
from collections import defaultdict
import os

# with open("sample_data/data.pkl", 'rb') as f:
#     data = pickle.load(f)
# print(json.dumps(data, indent=4))

studies = defaultdict(dict)

for img in os.listdir("experiment_data/images"):
    im_name = img[:-4]
    print(im_name)
    group_id, study_id, image_id = im_name.split("-",2)
    study_id = group_id + "-" + study_id
    studies[study_id][image_id] = [im_name]
    
    print(study_id, image_id)

studies_tmp = list(studies.values())
studies = []

for s in studies_tmp:
    if len(s.keys()) != 4:
        continue
    s_id = list(s.values())[0]
    s["horizontal_flip"] = "NO"
    s["cancer_label"] = {
        "left_malignant": 1*("PACZKA_5" in s_id and "PACZKA_6" in s_id),
        "left_benign": 1*("PACZKA_3" in s_id and "PACZKA_4" in s_id),
        "right_benign": 1*("PACZKA_3" in s_id and "PACZKA_4" in s_id),
        "right_malignant": 1*("PACZKA_5" in s_id and "PACZKA_6" in s_id),
        "unknown": 0,
        "benign": 1*("PACZKA_3" in s_id and "PACZKA_4" in s_id),
        "malignant": 1*("PACZKA_5" in s_id and "PACZKA_6" in s_id)
    }
    studies.append(s)

print(json.dumps(studies, indent=4))
with open('experiment_data/data.pkl', 'wb') as handle:
    pickle.dump(studies, handle)
