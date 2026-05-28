def generate_slurm(tool, cpus, ram, runtime):

    script = f"""#!/bin/bash
#SBATCH --job-name={tool}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task={cpus}
#SBATCH --mem={ram}G
#SBATCH --time={int(runtime)+2}:00:00

echo "Running {tool}"
"""

    return script