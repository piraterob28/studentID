<template>
    <div>
        <h1> Enter Student Information </h1>
        <form id="student-add" @submit.prevent> 
        <ul>
            <li v-for="e of errors" :key="e">{{e}}</li>
        </ul>
        <ul>
            <li> Student Name <input type="text" id= "studentname" v-model="studentAddForm.studentname" ></li>
            <li> Student ID <input type="text" id= "studentid" v-model="studentAddForm.studentid" required> </li>
            <li> Housing Building <input type="text" id= "building" v-model="studentAddForm.building" ></li>
            <li> Departent <input type="text" id= "department" v-model="studentAddForm.department" ></li>
            <li> Year Progression <input type="text" id= "year" v-model="studentAddForm.year" ></li>
        </ul> 
        <button @click="subAddList">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data () { return {
        studentAddForm: {
            studentname: '',
            studentid: '',
            building: '',
            department: '',
            year: '',
        },
        errors: []
    }},
    methods: {
        async subAddList () {
            this.errors = []
            for (const f of Object.keys(this.studentAddForm)) {
                if (!this.studentAddForm[f]) {
                    this.errors.push(`Field ${f} is Empty`)
                }
            }
            if (this.errors.length !== 0) {
                return 
            }
            await fetch('http://127.0.0.1:8000/students',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.studentAddForm)
        })

        }
    }   
}
</script>

<style>
ul li {
    text-align: right;
    padding-right: 600px;
}
button {
    margin-left: 250px;
    padding: 3px 10px;
    background-color: #1B4079;
    color: white;
}
</style>