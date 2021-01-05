<template>
    <button>{{text}}</button>
</template>

<script>
export default {
    props: {
        text: String
    }
}
</script>

<style>

button {
    padding: 3px 10px;
    background-color: #1B4079;
    color: white;
}
 
</style>