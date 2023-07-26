import java.text.SimpleDateFormat
import java.util.Date

pipeline {
	agent any
	environment {
		DOCKER_REGISTRY = '190109388255.dkr.ecr.ap-south-1.amazonaws.com/ami-automate-latest' // applicaton image(frontend app)
		NGINX_IMAGE_REG = '190109388255.dkr.ecr.ap-south-1.amazonaws.com/ami-nginx' //(base image:- nginx)
		DOCKERFILE_PATH = 'Dockerfile'
		AWS_REGION = 'ap-south-1'
		APPLICATION_BASE_IMAGE = 'latest'

		AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
		AWS_SESSION_TOKEN = credentials('AWS_SESSION_TOKEN')

	}

	stages {

		stage('SCM Checkout') {
			steps {
				git branch: 'main', // Specify the branch name here
					credentialsId: 'Srijan-altimetrik',
					url: 'https://github.com/srijan-altimetrik-2023/automatic-ecs-update.git'
			}
		}

		stage('Scan latest Base App Image') {
			steps {
				script {

					sh 'pip3 install boto3'
					sh 'pip3 install datetime'
					def imageTagsWithTimestamps = sh(script: "python3 getImgCreationDtFromECR.py", returnStdout: true).trim()
					println "timestamp: ${imageTagsWithTimestamps}"
					def lastDeployTime = readFile('lastDeployTime.txt')

					// def lastDeployTime = "2023-06-22"
					def dateFormat = new SimpleDateFormat("yyyy-MM-dd")
					def testLastDeployDate = dateFormat.parse(lastDeployTime)
					println "testLastDeployDate: ${testLastDeployDate}"

					// Replace the FROM tag with the desired value using sed
					if (dateFormat.parse(lastDeployTime).after(dateFormat.parse(imageTagsWithTimestamps))) {
						echo "new image is not available"
						error("New base image is not available, Terminating the pipeline execution")

					} else if (dateFormat.parse(lastDeployTime).before(dateFormat.parse(imageTagsWithTimestamps))) {
						echo "New Image Available"

						sh "sed -i 's/IMG_NUM/${APPLICATION_BASE_IMAGE}/g' ${DOCKERFILE_PATH}"
						sh 'touch lastDeployTime.txt'
						writeFile file: 'lastDeployTime.txt', text: imageTagsWithTimestamps
						sh 'git add lastDeployTime.txt'
						sh "git commit -m 'testing'"
						withCredentials([gitUsernamePassword(credentialsId: 'Srijan-altimetrik', gitToolName: 'Default')]) {
							sh 'git push --set-upstream origin main'
						}
					} else {
						error("last deploy_date & image creation_date are same, Skipping the pipeline execution")
					}
				}
			}

		}

		stage('Build Application Image') {
			steps {
				sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 190109388255.dkr.ecr.ap-south-1.amazonaws.com'
				sh 'docker build -t ${DOCKER_REGISTRY}:${BUILD_NUMBER} -t  ${DOCKER_REGISTRY}:latest -f ${DOCKERFILE_PATH} .'
			}
		}

		stage('ECR Push') {
			steps {
				sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 190109388255.dkr.ecr.ap-south-1.amazonaws.com'
				sh 'docker push ${DOCKER_REGISTRY}:${BUILD_NUMBER}'
				sh 'docker push ${DOCKER_REGISTRY}:latest'

			}
		}

		stage('App Deploy') {
			steps {
				sh 'terraform init -migrate-state '
				sh 'terraform taint aws_ecs_task_definition.hello_world'
				sh 'terraform plan  -out tfplan'
				sh 'terraform show -no-color tfplan > tfplan.txt'
				sh "terraform apply tfplan"
				script {
					emailext body: 'Test Message',
						subject: 'Test Subject',
						to: 'munichandra.nageti@gmail.com'
				}
				// sh "terraform apply -replace='aws_ecs_task_definition.hello_world' "
			}
		}
	}
}
