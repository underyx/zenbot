import re

from aiohttp import web
from . import zencyclopedia

async def provide_zen(request):
    await request.post()
    fragments_of_zen = [
        re.search(r'\w*', fragment.lower()).group()
        for fragment in request.POST['text'].split()
    ]

    try:
        zen_results = [
            zencyclopedia.index[fragment]
            for fragment in fragments_of_zen
        ]
        zen_candidates = set.intersection(*zen_results)
    except KeyError:
        return web.json_response({
            'response_type': 'in_channel',
            'text': (
                'Sorry, but I scoured the entire zencyclopedia and still '
                "couldn't find a match for your request :("
            ),
        })

    if len(zen_candidates) > 1:
        return web.json_response({
            'response_type': 'ephemeral',
            'text': (
                'Your request could match multiple lines, and in the face of '
                'ambiguity, I refused the temptation to guess. Try again '
                'with a request that only matches one of these lines:\n\n'
            ) + '\n'.join(' - ' + candidate for candidate in zen_candidates),
        })

    return web.json_response({
        'response_type': 'in_channel',
        'text': list(zen_candidates)[0],
    })


app = web.Application()
app.router.add_route('POST', '/', provide_zen)
