# Agrupación de textos

### Para la ejecución de este proyecto:
    1. Descargue el proyecto.
    2. Ingrese a la carpeta del proyecto y cree una carpeta llamada txt, en esta carpeta ponga los archivos que desee agrupar.
    3. Para correr el programa se puede usar los siguientes comandos 
        * Serial
            ```
            $ python SerialProject.py
            ```
        * Paralelo 
            ```
            mpiexec -np "# nucleos" python ./ParallelProject.py
            ```
    También puede hacer uso del archivo clustering.sh el cual sería:
        * Serial
            ```
            $ ./clustering.sh -s
            ```
        * Paralelo
            ```
            $ ./clustering.sh -p "# nucleos"
            ```
    4. Posteriormente los resultados de agrupación y el tiempo que tomo el proceso serán impresos en su terminal.


Nota: Para la implementación serial de este proyecto se tomó como referencia el proyecto de sergeio en github, https://github.com/sergeio/text_clustering.git Se realizaron algunos cambios para adaptarlo a nuestras necesidades y se realizó la paralelización del mismo en algunos de sus archivos, creando unos nuevos con el prefijo P.
