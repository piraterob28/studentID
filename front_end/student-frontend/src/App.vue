<template>
  <div id="app">
    <img id="Bigfoot" src=".\Images\bigfoot.jpg">
    <AppMenu/>
    
  </div>
</template>

<script>
import AppMenu from './components/AppMenu.vue'

export default {
  name: 'App',
  components: {
    AppMenu,
    
    
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
html {
  background-color: #8FAD88;
  min-height: 100%;
}
#Bigfoot{
  width: 355px;
  height: 250px;
  text-align: center;

}
</style>
