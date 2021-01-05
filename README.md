# Student Id Table 

## Description
This application was created in order to get a better understanding of a *Full Stack* web application as well as to farmiliarize myself with a modern javascript framework: Vue. The front-end of the application was built to display different pages using Vue's router. Vue components were used to encapsulate different functions of the application. A local database was created using SQLite to persist student information. Additional information can be added via the *Add Student* menu and displayed on the *Student Table* . The front-end application communicates with the FastAPI backend application over HTTP requests using JSON. Additional pages such as *Housing* and *Departments* were added to further solidify navigation with routers. 

## How to Run 

### Front End 
```cmd
npm install
npm run serve 
```
### Back End 
```cmd
pip install fastapi uvicorn sqlite3
uvicorn main:app --reload 
```

the application is available on http://localhost:8080
