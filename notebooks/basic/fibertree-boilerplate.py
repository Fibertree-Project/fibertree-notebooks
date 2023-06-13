\n
import os\n
\n
def run_prelude(**kwargs):\n
\n
  switches =  \" \".join([ f\"--{k}={v}\" for (k,v) in kwargs.items()])\n
\n
  for prelude_file in ['./prelude.py', '../prelude.py']:\n
    if os.path.exists(prelude_file):\n
      command=f\"{prelude_file} {switches}\"\n
      %run $command\n
      return\n
    \n
  print(\"Downloading prelude.py\")\n
  ! curl -LJOs https://raw.githubusercontent.com/Fibertree-Project/fibertree-notebooks/colab/notebooks/prelude.py\n
  command=f\"./prelude.py {switches}\"\n
  %run $command\n
\n
