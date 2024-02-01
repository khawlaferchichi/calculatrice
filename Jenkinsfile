
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
                    sh 'python3 calculatrice.py <choix> <nombre1> <nombre2>'
                }
            }
        }

         stage('Test Addition') {
            steps {
                script {
                    // Exécuter les tests d'addition
                   sh 'pytest -v tests/test_add.py | tee resultats_tests.txt'
                }
            }
        }

        stage('Test Soustraction') {
            steps {
                script {
                    // Exécuter les tests de soustraction
                    sh 'pytest -v tests/test_sous.py | tee resultats_tests.txt'
                    
                }
            }
        }

        stage('Test Multiplication') {
            steps {
                script {
                    // Exécuter les tests de multiplication
                  sh 'pytest -v tests/test_mult.py | tee resultats_tests.txt'
                }
            }
        }
         stage('Test Division') {
            steps {
                script {
                    // Exécuter les tests de division
                     sh 'pytest -v tests/test_div.py | tee resultats_tests.txt'
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

