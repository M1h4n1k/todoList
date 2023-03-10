<template>
    <div class="border w-full px-7 py-4 first:rounded-t last:rounded-b">
        <h3 class="text-xl font-semibold">
            {{taskInfo.title}}
        </h3>
        <h6 class="text-sm text-gray-400">
            {{taskInfo.date}}
        </h6>
        <p>
            {{taskInfo.description}}
        </p>
        <button @click="deleteTask" class="bg-red-500 px-4 py-1 rounded text-white mt-2 hover:bg-red-600 active:bg-red-700">
            Delete
        </button>
    </div>
</template>

<script>
export default {
    name: "TaskCard",
    props: {
        taskInfo: JSON
    },
    methods: {
        deleteTask() {
            this.$emit('deleteTask', this.taskInfo.id);
        }
    }
}
</script>

<style scoped>

</style>