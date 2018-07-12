node {
    stage ('Fetch') {
        git url: 'git@bitbucket.org:itzdata/core2eshop.git'
    }
    stage('Test') {
        sh 'python test.py'
    }
}