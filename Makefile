ENV_NAME=final-group20

.PHONY: env all clean

env:
	mamba env update -f environment.yml -n $(ENV_NAME)

all:
	jupyter nbconvert --to notebook --execute eda.ipynb --output eda.ipynb
	jupyter nbconvert --to notebook --execute ml.ipynb --output ml.ipynb
	jupyter nbconvert --to notebook --execute main.ipynb --output main.ipynb

clean:
	rm -rf _build
