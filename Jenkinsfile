pipeline {
  agent none
  stages {
    stage('Unit Test') {
      agent { dockerfile true }
      steps {
        sh '/app/test.sh'
      } 
    }
  }
}
