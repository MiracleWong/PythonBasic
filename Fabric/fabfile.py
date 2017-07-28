from fabric.api import env, roles, run, execute
env.roledefs = {
    'server1': ['root@192.168.101.30'],
    'server2': ['root@192.168.101.32'],
    'server3': ['root@192.168.101.38']
}

env.password = '123456'
@roles('server1')
def task1():
    run('ls -l /home/ | wc -l')
@roles('server2')
def task2():
    run('du -sh /home')
@roles('server3')
def task3():
    run('w')
def test():
    execute(task1)
    execute(task2)
    execute(task3)

