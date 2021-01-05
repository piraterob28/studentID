<template>
    <div>   
        <h1>Samsquatches School Of Mystery</h1>
        <ul id="appMenu">
            <li><router-link to="/">Home</router-link></li> 
            <li><router-link to="/student-list">Students</router-link></li>  
            <li><router-link to="/housing">Housing</router-link></li> 
            <li><router-link to="/departments">Departments</router-link></li> 
            <li><router-link to="/Student-add">Add Student</router-link></li> 
            <li><router-link to="/about">About</router-link></li>
        </ul> 
        <router-view/>
    </div>
    
</template>

<script>

export default {
    components: {
        
        
    }
    
}
</script>

<style scoped>
#appMenu {
    text-decoration-line: none;
    background-color: #1B4079;
    margin-inline-end: 5px 5px;
    text-align: center;
}
ul li{
    display: inline-block;
    background-color: #CBDF90;
    padding: 2px 5px;
    margin: 5px 5px;
    
    
}
ul li a{
    color: black; 
    text-decoration: none;  
}
a:hover {
  cursor: pointer;
}
#addButton {
    margin: 0px 100px;
    margin-right: 0px;
}
button:hover{
    cursor: pointer;
}
</style>