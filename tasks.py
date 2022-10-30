from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest --ignore=src/tests/performance_tests/ src", pty=True)

@task
def perf_test(ctx):
    ctx.run("python3 src/tests/performance_tests/main_perf_test.py", pty=True)

@task
def dijkstra_test_all(ctx):
    ctx.run("python3 src/tests/performance_tests/dijkstra_test_all_cases.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest --ignore=src/tests/performance_tests/ src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)