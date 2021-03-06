def ModuleReload(modulename):
    import importlib
    importlib.reload(modulename)
    
import os
try:
    import gpustat
except:
    os.system("pip install gpustat")
    import gpustat
def taLibs_getBatch_ViaGPU_Size(B):
    s0=gpustat.new_query()
    GPU_GB=s0.gpus[0].memory_total//1000
    MB=list(B.keys())
    k=0;
    while(MB[k]<GPU_GB):k+=1
    return B[MB[k]]
    
# Uses: GPU Size: Batch Size ------------------
B={ 6 :16,
    8 :24,
    11:32,
    12:40,
    15:48,
    16:64,
    24:128}
batch_size=taLibs_getBatch_ViaGPU_Size(B) 

##  insert into cell in jupyter: -----------------------------------------------------------------
# url="https://github.com/holianh/Linux_DeepLearning_tools/raw/master/taLibs_getBatch_ViaGPU_Size.py"
# import urllib.request  
# filename, headers = urllib.request.urlretrieve(url,filename=url.split('/')[-1]) 

# import importlib
# import taLibs_getBatch_ViaGPU_Size as getBatch
# importlib.reload(getBatch)

# # GPU Size: Batch Size
# B={ 6 :16,
#     8 :24,
#     11:32,
#     12:40,
#     15:48,
#     16:64,
#     24:128}
# batch_size=getBatch.taLibs_getBatch_ViaGPU_Size(B)
# batch_size
