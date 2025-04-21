pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose-dev.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/abhi1797/Backend-Social-media-app'
            }
        }

        stage('Inject .env Files') {
            steps {
                withCredentials([
                    file(credentialsId: 'ENV_FILE', variable: 'ENV_PATH'),
                    file(credentialsId: 'ENV_POSTGRES_FILE', variable: 'ENV_POSTGRES_PATH')
                ]) {
                    sh '''
                    cp $ENV_PATH .env
                    cp $ENV_POSTGRES_PATH .envpostgres
                    '''
                }
            }
        }

        stage('Start Docker Compose') {
            steps {
                sh '''
                docker compose -f $COMPOSE_FILE up -d
                sleep 10
                '''
            }
        }

        stage('Run Health Check') {
            steps {
                sh '''
                curl -sf http://localhost:8000/health || (echo " Health check failed" && exit 1)
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Stopping and cleaning up containers...'
            sh 'docker compose -f $COMPOSE_FILE down -v'
        }
    }
}
