 
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cloud.r-project.org", lib = "./rEnv")

.libPaths(c('./rEnv',.libPaths()))
BiocManager::install("limma", lib = "./rEnv")
