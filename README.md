
# learning-papermill
R&amp;D Papermill and Scrapbook to automate Jupyter Notebook workflows


# Introduction 

This is a project to experiment and play around with Papermill and 
Jupyter Notebook.  Inspired by
[Netflix's Notebook Driven Architecture.](https://blog.goodaudience.com/inside-netflixs-notebook-driven-architecture-aedded32145e) 



# Installation  

Clone repository then use either `make` or `pip`

From the `learning-papermill` directory use command 

`make install` 

or

`pip install .`


### Sanity check  

This example application also uses the [Click](https://click.palletsprojects.com/en/8.1.x/) framework for the 
Command-Line-Interface.  

The cli app has the name `paper`  

Issuing `paper` command will expose all the current available actions in the app.  


`paper hello` will echo `hello` is useful for sanity checks. 




---  
# References    

[Jupyter Notebooks in a Git Repo](https://mg.readthedocs.io/git-jupyter.html)  


Interesting note in papermill release notes:

```
0.19.0

DEPRECATION CHANGE The record, read_notebook, and read_notebooks functions are now officially deprecated and will be removed in papermill 1.0.
```