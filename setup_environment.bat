py "-m" "venv" "%CD%\pythonEnv"
call pythonEnv\Scripts\activate.bat
py "-V"
where "python"
py "-m" "pip" "install" "-r" "requirements.txt"
Rscript "%CD%\R_packages\limmaPkg.R"
echo "Done setting up R and Python environments"
