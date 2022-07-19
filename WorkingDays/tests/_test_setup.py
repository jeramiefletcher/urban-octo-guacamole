def lines(func):
    def inner(*args, **kwargs):
        print("-" * 88)
        func(*args, **kwargs)
        print("-" * 88)

    return inner


@lines
def printVersion(testversion, pyfile, version):  # pragma: no cover
    pyfile = pyfile.capitalize()
    PrintVersion = "Tested with " + pyfile + " Version: {}"
    print(
        "\n"
        + "TestCase Version: "
        + testversion
        + " \n"
        + PrintVersion.format(version)
        + " \n"
    )
