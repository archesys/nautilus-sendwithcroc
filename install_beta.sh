#!/bin/bash
#######################################
# Vérification de la présence de Croc #
#######################################
if [ -f "/bin/croc" ];then
	echo "croc se trouve bien en /bin/croc";
   	CROC="/bin/croc"
else
	if [ -f "/usr/local/bin/croc" ];then
		echo "croc se trouve bien en /usr/local/bin/croc";
		CROC="/usr/local/bin/croc"
	else
		echo "croc est absent veuillez l'installer";
	fi
fi
#########################################
# Vérification de la présence de Python #
#########################################
if [ -f "/bin/python" ];then
        echo "python se trouve bien en /bin/python";
        PYTHON="/bin/python"
else
        if [ -f "/usr/local/bin/python" ];then
                echo "python se trouve bien en /usr/local/bin/python";
                PYTHON="/usr/local/bin/python"
        else
                echo "python est absent veuillez l'installer";
        fi
fi
###########################################
# Vérification de la présence de Nautilus #
###########################################
if [ -f "/bin/nautilus" ];then
        echo "nautilus se trouve bien en /bin/nautilus";
        NAUTILUS="/bin/nautilus"
else
        if [ -f "/usr/local/bin/nautilus" ];then
                echo "nautilus se trouve bien en /usr/local/bin/nautilus";
                NAUTILUS="/usr/local/bin/nautilus"
        else
                echo "nautilus est absent veuillez l'installer";
        fi
fi
if [ ! -z "$NAUTILUS" ];then
    echo "Nautilus Présent";
    if [ -d "~/.local/share/nautilus/scripts" ];then
        echo "Le dossier nautilus scripts existe !";
    fi
fi
#######################################
# Vérification de la présence de Nemo #
#######################################
if [ -f "/bin/nemo" ];then
        echo "nemo se trouve bien en /bin/nemo";
        NEMO="/bin/nemo"
else
        if [ -f "/usr/local/bin/nemo" ];then
                echo "nemo se trouve bien en /usr/local/bin/nemo";
                NEMO="/usr/local/bin/nemo"
        else
                echo "nemo est absent veuillez l'installer";
        fi
fi
if  [ ! -z "$NEMO" ];then
    echo "Nemo Présent";
    if [ -d "~/.local/share/nemo/scripts" ];then
        echo "Le dossier nemo scripts existe !";
    fi
fi
exit 0 
