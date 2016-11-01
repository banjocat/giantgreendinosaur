from fabric.api import run, env, cd, put, hosts

env['user'] = 'root'


@hosts('giantgreendinosaur.com')
def deploy():
    '''
    Deploy the dinosaur
    '''
    run('mkdir -p /app/dino')
    put('./production-compose.yml', '/app/dino/docker-compose.yml')
    with cd('/app/dino'):
        run('docker-compose pull')
        run('docker-compose stop')
        run('docker-compose up -d')
