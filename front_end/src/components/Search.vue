<template>
    <input 
        type="text" 
        id="Search"
        :value="search"
        @input="onSearch($event.target.value)"
        placeholder="Search">
</template>

<script>
export default {
    props: [
        "search"
    ],
    methods: {
        onSearch(s) {
            this.$emit('input', s);
        }
    }
}


</script>

<style>
#Search {
    background-image: url('/css/searchicon.png');
    background-position: 10px 12px; /* Position the search icon */
    background-repeat: no-repeat; /* Do not repeat the icon image */
    width: 40%; /* Full-width */
    font-size: 16px; /* Increase font-size */
    padding: 12px 20px 12px 40px; /* Add some padding */
    border: 1px solid #ddd; /* Add a grey border */
    margin-bottom: 12px; /* Add some space below the input */

}
</style>