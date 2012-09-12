from abjad.tools import sequencetools


def apply_request_transforms(request, payload):
    r'''.. versionadded:: 1.0 
    
    Apply nonnone ``request.index`` to `payload`.

    Apply nonnone ``request.count`` to `payload`.

    Apply nonnone ``request.reverse`` to `payload`.

    Return `payload`.
    '''

    if request.index is not None or request.count is not None:
        original_payload_type = type(payload)
        index = request.index or 0
        if index < 0:
            index = len(payload) - -index
        if request.count is None:
            count = len(payload) - index    
        else:
            count = request.count
        payload = sequencetools.CyclicTuple(payload)
        payload = payload[index:index+count]
        payload = original_payload_type(payload)

    if getattr(request, 'reverse', False):
        original_payload_type = type(payload)
        payload = list(reversed(payload))
        payload = original_payload_type(payload)

    return payload 
