<template>
    <div class="student-list">
        <Search :value="search" @input="onSearch"/>
        <StudentTable :search="search"/>
    </div>
</template>

<script>
import StudentTable from '@/components/StudentTable.vue'
import Search from '@/components/Search.vue'
export default {
    components: {
        StudentTable, 
        Search
    },
    data () {
        return {
            search: ""
        }
    },
    methods: {
        onSearch (s) {
            this.search = s;
        }
    }
}
</script>
<style>
</style>