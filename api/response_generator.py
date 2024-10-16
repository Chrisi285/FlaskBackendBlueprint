import json

from flask import Response


def respond(r=None, status=200, json_dump=True, cookie="", authorized=True):
    if not authorized:
        return Response(
            json.dumps({'success': False, 'error': 'unauthorized', 'description': 'Action requires higher privileges'}),
            status=401, mimetype='application/json')
    if r is None:
        r = {'success': True}
    headers = {"Cache-Control": "no-cache, no-store, must-revalidate, public, max-age=0",
               "Pragma": "no-cache",
               "Expires": "0",
               "Access-Control-Allow-Origin": "*"}
    if cookie != "":
        headers['Set-Cookie'] = cookie
    if json_dump:
        return Response(json.dumps(r), status=status, mimetype='application/json', headers=headers)
    return Response(r, status=status, mimetype='application/json', headers=headers)
