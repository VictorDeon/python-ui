venv:
	# Cria o ambiente virtual
	python3 -m venv venv


start:
	# Ativa o ambiente virtual
	source venv/bin/activate

end:
	# Sai do ambiente virtual
	deactivate
