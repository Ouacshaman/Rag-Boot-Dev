from search_cmd import tokenization


class InvertedIndex:
    def __init__(self, index, docmap):
        self.index = index
        self.docmap = docmap

    def __add_documents(self, doc_id, text):
        token = tokenization(text)
        for v in token:
            if v in self.index:
                self.index = self.index[v].set(doc_id)
            else:
                self.index[v] = {doc_id}

    def get_documents(self, term):
        term = term.lower()
        out = self.index[term].sort()
        return out

    def build(self, movies, doc_id):
        for i in range(0, len(movies), 1):
            joined = f"{movies[i]["title"]} {movies[i]["descriptions"]}"
            self.__add_documents(doc_id, joined)
            self.docmap[doc_id] = joined
        return

    def save():
        pass
