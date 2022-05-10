from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from typing import Optional
from pydantic import BaseModel
import traceback

from islenska import Bin

__version__ = 0.1


app = FastAPI()

def error(errors):
    return JSONResponse(content=({"failure":{"errors":[errors]}}))

b = Bin()


@app.get('/', response_class=HTMLResponse)
def home() -> str:
	return """
<html>
	<head><title>POS API</title></head>
	<body>
		<h1>POS API Server v{0}</h1>
		<ul><li><a href="/docs">Documentation</a></li></ul>
	</body>
</html>
""".format(__version__)

class BinPackageInput(BaseModel):
	type: Optional[str] = "text"
	content: str

@app.post('/binpackage')
def binpackage(request : BinPackageInput) -> str:
    lookup = (b.lookup(request.content))
    resp = []
    for l in lookup[1]:
        resp.append({'content': l[0], 'features':\
                        {'bin_id': l[1],\
                         'ofl': l[2],\
                         'hluti': l[3],\
                         'bmynd': l[4],\
                         'mark': l[5]}})

    return JSONResponse(content={"response":{"type":"texts", "texts":resp}})


