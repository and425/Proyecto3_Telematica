#!/bin/bash

#SBATCH --job-name=Proyecto3_Telematica
#SBATCH --output=output.txt
#SBATCH --time=03:00:00
#SBATCH --partition=estudiantes
#SBATCH --ntasks=10

usage()
{
    echo "Help"
    echo "\t-h | --help"
    echo "\t-s | --serial"
    echo "\t-p | --parallel  Number of nodes"
    echo ""
}

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $2 | awk -F= '{print $2}'`
    case $PARAM in
        -h | --help)
            usage
            exit
            ;;
        -s | --serial)
            python ./SerialProject.py
            exit
            ;;
        -p | --parallel)
            NODES="$2"
            shift
            mpiexec -np $NODES python ./ParallelProject.py
            exit
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done
