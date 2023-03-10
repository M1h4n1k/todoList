<script setup>
import Header from "@/components/TheHeader.vue";
import TheBanner from "@/components/TheBanner.vue";
import TheTaskCreateWindow from "@/components/TheTaskCreateWindow.vue";
import TaskCard from "@/components/TaskCard.vue";
</script>

<template>
    <header>
        <Header/>
    </header>

    <div class="w-full flex items-center justify-center">
        <div class="w-9/12">
            <TheBanner/>
            <div class="flex mt-8 w-full space-x-20">
                <TheTaskCreateWindow @createTask="createTask"/>
                <div class="w-1/2">
                    <TaskCard v-for="task in sortedTasks" :key="task.id" :taskInfo="task" @deleteTask="deleteTask"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'App',
    data() {
        return {
            tasks: []
        }
    },
    created() {
        fetch('/tasks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: "include"
        }).then(response => response.json())
            .then(data => {
                this.tasks = data;
            })
    },
    methods: {
        deleteTask(id) {
            fetch(`/tasks/${id}`, {
                method: 'DELETE',
                credentials: "include"
            })
                .then(response => response.json())
                .then(data => {
                    this.tasks = this.tasks.filter(task => task.id !== id);
                })
        },
        createTask(task){
            fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(task),
                credentials: "include"
            })
                .then(response => response.json())
                .then(data => {
                    task['id'] = data['id'];
                    this.tasks.push(task);
                })
        }
    },
    computed: {
        sortedTasks() {
            return this.tasks.sort(function (a, b) {
                return new Date(a.date) - new Date(b.date);
            });
        }
    }
}
</script>

<style scoped>

</style>
