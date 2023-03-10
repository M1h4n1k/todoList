<template>
    <div class="w-1/2 h-fit rounded border-2">
        <div class="pl-2 flex items-center h-10 bg-gray-100 rounded ">
            Add event
        </div>
        <div class="px-7 py-4 space-y-2">
            <input v-model="title" class="w-full h-8 indent-2.5 rounded border border-[#ddd]" type="text" placeholder="Task title">
            <textarea v-model="description" class="w-full h-24 indent-2.5 rounded border border-[#ddd]" placeholder="Task Description"></textarea>
            <input v-model="date" class="w-full h-8 indent-2.5 rounded border border-[#ddd]" type="date" placeholder="today">
            <button @click="createTask" class="bg-blue-400 px-4 py-1 rounded text-white mt-2 hover:bg-blue-500 active:bg-blue-600">
                Submit
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "TheTaskCreateWindow",
    data() {
        return {
            title: '',
            description: '',
            date: ''
        }
    },
    methods: {
        createTask(){
            this.$emit('createTask', {
                title: this.title,
                description: this.description,
                date: this.date
            });
            this.title = '';
            this.description = '';
            this.date = '';
        }
    }
}
</script>

<style scoped>

</style>