import json
import Connectors
import Transformations
import AutoML
try:
    Adnan_DBFS = Connectors.DBFSConnector.fetch([], {}, "5e96caf9737c493d8c9fd3ef", spark,
                                                "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Adnan_AutoFE = Transformations.TransformationMain.run(["5e96caf9737c493d8c9fd3ef"], {
                                                          "5e96caf9737c493d8c9fd3ef": Adnan_DBFS}, "5e96caf9737c493d8c9fd3f0", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(Adnan_AutoFE, [], "")

except Exception as ex:
    print(ex)
