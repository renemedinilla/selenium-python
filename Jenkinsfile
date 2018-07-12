node {
    stage ('Fetch') {
        git url: 'https://github.com/renemedinilla/selenium-python.git'
    }
    stage('Test') {
        sh 'python test.py'
    }
}