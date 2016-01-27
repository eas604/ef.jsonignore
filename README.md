# ef.jsonignore
Add [Newtonsoft.Json.JsonIgnore] to EF navigation properties so they serialize correctly.

## usage
Place in the same directory as your Entity Framework model `.cs` files, then run from the command prompt.

## todo
Currently uses `cwd` for the path to search. Should be modified to take a path as a param.
