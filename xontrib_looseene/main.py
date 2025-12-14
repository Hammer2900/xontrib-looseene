import sys
from xonsh.events import events
from .backend import SearchEngineHistory
from .ui import start_search_ui


def _load_xontrib_(xsh, **kwargs):
    xsh.env['XONSH_HISTORY_BACKEND'] = SearchEngineHistory
    global_history = SearchEngineHistory()
    xsh.history = global_history
    print('Looseene: History backend loaded.', file=sys.stderr)

    @events.on_ptk_create
    def custom_keybindings(bindings, **kw):
        @bindings.add('c-r')
        async def _(event):
            await start_search_ui(event)

    def _hsearch(args):
        if not args:
            print('Usage: hsearch <query>')
            return
        query = ' '.join(args)
        if hasattr(xsh.history, 'search'):
            print(f'Searching for: {query}...')
            results = xsh.history.search(query, limit=5)
            if not results:
                print('No matches found.')
            for i, doc in enumerate(results):
                cmd = doc.get('inp', '').strip().replace('\n', ' ')
                print(f'{i + 1}. {cmd}')
        else:
            print('Error: Looseene backend not active.')

    xsh.aliases['hsearch'] = _hsearch
    xsh.aliases['hs'] = _hsearch

    def _compact(args):
        if hasattr(xsh.history, 'run_compaction'):
            xsh.history.run_compaction()
        else:
            print('Looseene backend not active.')

    xsh.aliases['history-compact'] = _compact
    try:
        if hasattr(xsh.history, 'engine') and len(xsh.history.engine.segments) > 50:
            print("Looseene: Many history segments detected (>50). Run 'history-compact'.", file=sys.stderr)
    except:
        pass
