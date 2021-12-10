import os
import subprocess
import sys

def read_output(stream,callback):
  mstr = ""
  for line in iter(stream.readline,b''):
    mstr += line.decode()
  return mstr

if __name__ == "__main__":
  print(sys.argv)
  p_c = sys.argv[1]
  print(f"Using `{p_c}`")
  print("Getting ALl Solutions")
  cwd = os.getcwd()
  file_list = []
  for item in os.listdir("."):
    if not "." in item and item.startswith("day"):
      for file in os.listdir(item):
        if file.endswith(".py"):
          file_list.append((int(item[-2:]),f"{cwd}/{item}", file))
  file_list.sort(key = lambda x: x[0])
  print(file_list)
  print("Initiating Run")
  for f in file_list:
    print(f'{33*"="} DAY {f[0]} {33*"="}')
    sequence = ["/bin/bash","-c",f"cd {f[1]} && {p_c} {f[2]}"]
    print(' '.join(sequence))
    process = subprocess.Popen(sequence, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = read_output(process.stdout,process.stderr)
    print(res)
  print(100 * "=")