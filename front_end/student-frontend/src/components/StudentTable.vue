<template>
     <table style="width:100%" id ="StudentTable">
                <tr class="header">
                    <th>Student Name</th>
                    <th>Student ID</th>
                    <th>Housing Building</th>
                    <th>Academic Department</th>
                    <th>Education Stage</th>
                </tr>
                <tr v-for="s in filteredStudents" :key="s.id">
                    <td>{{s.Student}}</td>
                    <td>{{s.Student_ID}}</td>
                    <td>{{s.Housing}}</td>
                    <td>{{s.Department}}</td>
                    <td>{{s.Year}}</td>
                    
                </tr>
      </table> 
      
</template>

<script>
export default {
  props: [
      "search"
  ],
  data () {
      return {
          students: []
      }
  },
  created () {
    fetch('http://127.0.0.1:8000/students')
      .then(response => response.json())
      .then(json => {
        this.students = json;
        console.log(this.filteredStudents)
      })
  },
  computed: {
    filteredStudents () {
      return this.students.filter(s => {
        return s.Student.toUpperCase().includes(this.search.toUpperCase())
      })
    }
  }
}
</script>

<style>
#StudentTable {
  border-collapse: collapse; /* Collapse borders */
  width: 100%; /* Full-width */
  border: 3px solid #4D7C8A; /* Add a grey border */
  font-size: 18px; /* Increase font-size */
}

#StudentTable tr {
  /* Add a bottom border to all table rows */
  border-bottom: 1px solid black;
}
 
#StudentTable tr.header, #StudentTable tr:hover {
  /* Add a grey background color to the table header and on hover */
  background-color:#4D7C8A;
  color: #CBDF90;
} 
</style>