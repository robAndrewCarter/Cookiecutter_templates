make_image:
	sudo docker build -t {{cookiecutter.project_name}} .
	sudo docker tag {{cookiecutter.project_name}} gcr.io/bioskryb/{{cookiecutter.project_name}}
	sudo gcloud docker -- push gcr.io/bioskryb/{{cookiecutter.project_name}}
