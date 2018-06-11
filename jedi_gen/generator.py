from __future__ import unicode_literals, print_function

import time
import jedi

SOURCE_TEMPLATE = '''
import %s
%s
'''

TYPE_SHORTS = {
    'class': '',
    'function': 'def',
    'instance': 'var',
    'module': 'mod',
    'statement': 'var'
}


def get_params(completion):
    params = []
    for param in completion.params:
        params.append(param.description.split()[-1])
    return params


def find_model(model_path):
    # re.
    if model_path.endswith('.'):
        return model_path[:-1]
    # re.search
    elif '.' in model_path:
        index = model_path.rfind('.')
        return model_path[:index]
    else:
        return model_path


def generate(model_path):
    if '.' not in model_path:
        model_path = model_path + '.'

    model = find_model(model_path)
    source = SOURCE_TEMPLATE % (model, model_path)
    script = jedi.Script(source, 3, len(model_path), 'example.py')

    completions = []
    for completion in script.completions():
        if completion.type not in ('statement', 'module', 'instance'):
            params = get_params(completion)
        else:
            params = None

        info = {
            'short_type': TYPE_SHORTS[completion.type],
            'doc': completion.docstring(),
            'name': completion.name,
            'type': completion.type,
            'params': params,
            'module': completion.module_path
        }
        completions.append(info)

    record_time = time.time()

    if completions:
        modules = {completions[0]['module']: int(record_time)}
    else:
        modules = None

    result = {
        'version': 16,
        'cache_key': [model, 'package'],
        'completions': completions,
        'modules': modules,
        'time': record_time
    }

    return result
