# Menu
This is all Header in this file:
1. Linux DeepLearning tools
2. Linux system
3. Check Envs for Deep Learning, [view](#check-envs-for-deep-learning)
4. Install Deeplearning Libraries
5. Python functions List
6. Keras funcs list


# 1. Linux DeepLearning tools
These are some useful tools to use with Linux (focus on Ubuntu) when working with Deep Learning.

# 2. Linux system
Useful linux command
  - __htop__: to view in %CPU uses by threads, %RAM: kill thread, filter, search,...
  - __ncdu__: to view files/folders size over local or ssh
  - __find -type f -name "*libcudnn.so*"__ : find file/folder in Linux, [more](ubuntu_commands.sh#L14)
  - __rm -fdr <dir_name>__: Remove a dir with contents, [more](ubuntu_commands.sh#L2)
  - __sudo lshw -class disk -short__ : List Physical Hardisk in Ubuntu, [view](ubuntu_commands.sh#L21)
# 3. Check Envs for Deep Learning
  - nvidia-smi
  - nvcc -V
  - find -type f -name "*libcudnn.so*"
  - nvidia-smi --format=csv,noheader --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics, [more](ubuntu_commands.sh#L6)

  # 4. Install Deeplearning Libraries
  - pipreqs /path/to/project: PYTHON - AUTO GENERATE REQUIREMENTS.TXT, [more](ubuntu_commands.sh#L33)
  - pip install python-levenshtein
  - 
  
  # 5. Python functions List
   - def LastNlines\(NLs=15,LineContainKey="Key to Fine"\), [view](python_funcs_codes.py#L7)
   -  Plot history and accuray when training with Keras to PDF, [view](python_funcs_codes.py#L38)
   - Save data to json file, [view](python_funcs_codes.py#L113) 
   - Files_2csv_inDir: Find and Add All wav & label files to *.CSV, [view](python_funcs_codes.py#L130)
   - Timing: Calculate running time, [view](python_funcs_codes.py#L174) 
   - Get date time, month, day, hour, minute,...[view](python_funcs_codes.py#L272)
   - Post (upload) file/string to PHP webpage, [view](python_funcs_codes.py#L195)
   - Run a system Ubuntu command, [view](python_funcs_codes.py#L223) 
   - Substring: Copy contends from txt file, add string of time, add ... [view](python_funcs_codes.py#L229)
   - []() 
   - []()

   
   # 6. Keras funcs list
   this is all useful Keras functions, can be directly use
   - Keras: save model + weight to files, [here](Keras_funcs.py#L2)
   - Keras: load model + weight from files to numpy array, [here](Keras_funcs.py#L17)
   
   
   
   
   
   
   
   
   
