def yanghui_trangle(n):
    def _yanghui_trangle(n, result):
        if n == 1:
            return [1]
        else:
            return [sum(i) for i in zip([0] + result, result + [0])]
    pre_result = []
    for i in xrange(n):
        pre_result = _yanghui_trangle(i + 1, pre_result)
        yield pre_result
if __name__ == "__main__":
    for line in yanghui_trangle(10):
        print line
