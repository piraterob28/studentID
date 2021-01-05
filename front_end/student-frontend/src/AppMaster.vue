<template>
  <div id="app">
    <img id="Bigfoot" src="..\Images\bigfoot.jpg">
    <AppMenu/>
    <HomePage/>
  </div>
</template>

<script>
import AppMenu from './components/AppMenu.vue'
import HomePage from './components/HomePage.vue'
export default {
  name: 'App',
  components: {
    AppMenu,
    HomePage
    
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

html {
  background-color: #8FAD88;
  min-height: 100%;
}
#Bigfoot{
  width: 355px;
  height: 250px;

}

</style>
