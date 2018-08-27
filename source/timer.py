import timeit

setupStr = """
a = list(range({N})); b=list(range({N}, 2*{N}))
"""

statement = {
    'add': "a + b"
    'ext': "a.extend(b)",
    'iadd': "a += b",
}


def main():
    import collections
    results = collections.defaultdict(list)
    powTot = 7
    for powval in range(1, powTot):
        results["Npow"].append(powval)
        listsize, numruns = 10 ** powval, 10 ** (powTot-powval)
        print(f"N = {listsize}, n = {numruns}")
        setup = setupStr.format(N=listsize)
        for method, stmt in statement.items():
            time = min(timeit.repeat(stmt, setup, repeat=numruns, number=1))
            print(f"{method}: {time*numruns:.3f}")
            results[method].append(time)

    import tabulate
    print(tabulate.tabulate(results, headers='keys', tablefmt="pipe"))
    from matplotlib import style
    style.use('ggplot')
    from matplotlib import pyplot as plt
    xaxis = results.pop('Npow')
    for method, res in results.items():
        plt.semilogy(xaxis, res, label=method)
    plt.title("Times for various methods")
    plt.xlabel("Log of listsize")
    plt.ylabel("Time taken")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()