"""
Given a list of accounts, whose IDs may not be unique.
Each account has field: ID, isSensitive, and other data
You need to send all the "sensitive" accounts for encrypting some of their data, and
return the result as a list of accounts too, in the same order as original, where data has been encrypted.
"""
import uuid


class Account:
    def __init__(self, id, is_sensitive, data):
        self.id = id
        self.is_sensitive = is_sensitive
        self.data = data
    def set_data(self, data):
        self.data = data


class EncryptingRequest:
    def __init__(self, track_id, data):
        self.track_id = track_id
        self.data = data

class EncryptingResponse:
    def __init__(self, track_id, encrypted_data):
        self.track_id = track_id
        self.encrypted_data = encrypted_data
class EncryptingService:
    def encrypt(self, requests: list[EncryptingRequest]):
        # this is an external service. No modificationis allowed.
        # order of the result may differ from the input
        responses: list[EncryptingResponse] = []
        responses = [EncryptingResponse(req.track_id, "encrypted_" + req.data) for req in requests]
        return responses

def handle_accounts(accounts: list[Account]):
    """
    Requirement:
    Need to only encrypt the data for those accounts that are sensitive.
    Return the list of accounts in the same order as in the original list, where sensitive accounts have their data encrypted.
    To encrypt data, simply call EncryptingService.
    Note that account IDs may not be unique.

    Solution: for each account, we generate a globally unique ID for it (UUID), and store them in an ordered dict.
    """
    map: dict[str, Account] = {} #ordered dict in python 3
    for acc in accounts:
        track_id = str(uuid.uuid4())
        map[track_id] = acc

    requests: list[EncryptingRequest] = [EncryptingRequest(key, val.data) for key, val in map.items() if val.is_sensitive]
    encrypting_servive = EncryptingService()
    responses: list[EncryptingResponse] = encrypting_servive.encrypt(requests)
    for res in responses:
        map.get(res.track_id).set_data(res.encrypted_data)

    return [val for (key, val) in map.items()]

if __name__ == '__main__':
    acc1 = Account(1, True, "acc1")
    acc2 = Account(1, False, "acc2")
    acc3 = Account(3, True, "acc3")
    acc4 = Account(3, True, "acc4")

    accs = handle_accounts([acc1, acc2, acc3, acc4])
    for acc in accs:
        print(acc.id, acc.data)

