pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Clonando el repositorio Git...'
                checkout scm
                echo 'Código clonado.'
            }
        }
        stage('Run Basic Tests') { // <--- ASEGÚRATE DE QUE ESTA ETAPA ESTÉ AQUÍ
            steps {
                echo 'Iniciando las pruebas automatizadas...'
                // Descomenta la línea correcta para tu sistema operativo
                bat 'run_tests.bat' // Si estás en Windows
                // sh './run_tests.sh' // Si estás en macOS/Linux
                echo 'Pruebas completadas.'
            }
        }
        stage('Print Message') {
            steps {
                echo '¡Hola Mundo desde tu primer Jenkins Pipeline!'
            }
        }
    }
    post {
        always {
            echo 'El pipeline ha finalizado.'
        }
        success {
            echo '¡El pipeline se ejecutó con éxito!'
        }
        failure {
            echo '¡El pipeline falló! Se encontraron problemas.'
        }
    }
}