.libPaths(c('./rEnv',.libPaths()))

library(limma)
rdata <- read.csv('./GC_allcodes/gc_exnonc.csv',row.names='ID')
exdata <- data.frame(rdata)
# print(exdata['nc_sub_115'])

rdata1 <- read.csv('./GC_allcodes/gc_exdata_design.csv',row.names='index')
design <- data.frame(rdata1)
# print(design)

cont_matrix <- makeContrasts(NCvsC = nc-c, levels=design)
# print(cont_matrix)

# Fit the expression matrix to a linear model
fit <- lmFit(exdata, design)

# Compute contrast
fit_contrast <- contrasts.fit(fit, cont_matrix)

# Bayes statistics of differential expression
# *There are several options to tweak!*
fit_contrast <- eBayes(fit_contrast)

# Generate a list of top differentially expressed genes
top_genes <- topTable(fit_contrast, number = 2550, adjust = "BH")
# print(top_genes)

# Summary of results (number of differentially expressed genes)
result <- decideTests(fit_contrast)
summary(result)

# Write CSV
write.csv(top_genes, "./GC_allcodes/gc_ex2550.csv")
