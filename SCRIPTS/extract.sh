#!/bin/bash
#SBATCH  --output=/srv/beegfs02/scratch/aegis_guardian/data/rosbags/SA_amalitech/%j.out
#SBATCH  --nodes=4
#SBATCH  --ntasks=4
#SBATCH  --mem=50G



USERID=$1
RIDEID=$2


singularity exec -B /srv/beegfs02/scratch/aegis_guardian/data /scratch_net/hispalensis/aegis-extract.simg bash /home/gahiadzi/ETH-AWS/SCRIPTS/extraction.sh $USERID $RIDEID