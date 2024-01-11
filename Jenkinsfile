
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Installer les dépendances
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Addition') {
            steps {
                script {
                    // Exécuter les tests d'addition
                    sh 'python3 -m unittest discover -s tests -p "test_add.py" --junit-xml=test-results-addition.xml'
                }
            }
        }

        stage('Test Soustraction') {
            steps {
                script {
                    // Exécuter les tests de soustraction
                    sh 'python3 -m unittest discover -s tests -p "test_sous.py" --junit-xml=test-results-subtraction.xml'
                }
            }
        }

        stage('Test Multiplication') {
            steps {
                script {
                    // Exécuter les tests de multiplication
                    sh 'python3 -m unittest discover -s tests -p "test_mult.py" --junit-xml=test-results-multiplication.xml'
                }
            }
        }
         stage('Test Division') {
            steps {
                script {
                    // Exécuter les tests de division
                    sh 'python3 -m unittest discover -s tests -p "test_div.py" --junit-xml=test-results-division.xml'
                }
            }
        }

        stage('Afficher les résultats des tests') {
            steps {
                // Rapport JUnit agrégeant tous les résultats des tests
                junit '**/test-results-*.xml'
            }
        }
    }

    post {
        success {
            echo 'Le pipeline a réussi!'
            // Ajouter des étapes pour le déploiement en production, etc.
        }

        failure {
            echo 'Le pipeline a échoué. Vérifiez les journaux pour plus d\'informations.'
        }
    }
}

