pipeline {
    agent any // Esto le dice a Jenkins que el pipeline puede ejecutarse en cualquier agente disponible.

    stages {
        stage('Checkout Code') { // Primera etapa: obtener el código del repositorio
            steps {
                echo 'Clonando el repositorio Git...'
                checkout scm // Este paso le dice a Jenkins que clone el repositorio configurado en el trabajo.
                echo 'Código clonado.'
            }
        }
        stage('Print Message') { // Segunda etapa: imprimir un mensaje simple
            steps {
                echo '¡Hola Mundo desde tu primer Jenkins Pipeline!'
                // Aquí podrías agregar más pasos en el futuro, como ejecutar comandos para compilar, probar, etc.
            }
        }
    }
    post { // La sección 'post' define acciones a ejecutar después de que el pipeline termine.
        always {
            echo 'El pipeline ha finalizado.'
        }
        success {
            echo '¡El pipeline se ejecutó con éxito!'
        }
        failure {
            echo '¡El pipeline falló!'
        }
    }
}