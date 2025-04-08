import os
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, List
from util.emaillookup.reader.reader import Reader, Data

class ResultObject:
    def __init__(self, creationTime: int, filename: str, data: Data):
        self.creationTime = creationTime
        self.fileName = filename
        self.data = data

def hashToInt(self, inputStr: str) -> int:
    return int(hashlib.sha256(inputStr.encode()).hexdigest(), 16)  # get the int form of the hash

class EmailLookup:
    def __init__(self, path: str):
        self.path = path  # Declare path
    def lookupEmail(self, inputStr: str) -> Optional[Data]:
        try:
            entries = os.listdir(os.path.dirname(self.path))
        except Exception as e:
            print(e)
            return None
        resultsEmail = []
        resultsDomain = []
        resultsLockEmail = threading.Lock()
        resultsLockDomain = threading.Lock()
        threads = []
        
        def processFile(self, inputStr: str, filename: str):
            try:
                with open(os.path.join(os.path.dirname(self.path), filename), "rb") as file:
                    readerInstance = Reader(file)
                    if readerInstance.header.type == 0x01:
                        domain = inputStr.split("@")[1] if "@" in inputStr else inputStr
                        data = readerInstance.contains_offset(hashToInt(domain), readerInstance.header.get_size())
                        if data:
                            with resultsLockDomain:
                                resultsDomain.append(ResultObject(readerInstance.header.creationTime, filename, data))
                    else:
                        data = readerInstance.contains_offset(hashToInt(inputStr), readerInstance.header.get_size())
                        if data:
                            with resultsLockEmail:
                                resultsEmail.append(ResultObject(readerInstance.header.creationTime, filename, data))
            except Exception as e:
                print(e)
        for entry in entries:
            thread = threading.Thread(target=processFile, args=(inputStr, entry))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        finalResultEmail = max(resultsEmail, key=lambda x: x.creationTime, default=None)
        finalResultDomain = max(resultsDomain, key=lambda x: x.creationTime, default=None)
        if finalResultEmail and finalResultDomain:
            finalResultEmail.data.data.extend(finalResultDomain.data.data)
            return finalResultEmail.data
        return finalResultEmail.data if finalResultEmail else (finalResultDomain.data if finalResultDomain else None)
