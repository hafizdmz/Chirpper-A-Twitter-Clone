<template>
    <label :for="idInput" class="mt-3">{{ labelName }}</label>
    <input :type="inputType" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="rounded-md bg-gray-300 focus:bg-white focus:outline-none focus:border-b-4 focus:border-blue-400 h-10"/>
</template>

<script setup>
defineProps(['labelName', 'inputType', 'modelValue', 'idInput' ])
defineEmits(['update:modelValue'])
</script>