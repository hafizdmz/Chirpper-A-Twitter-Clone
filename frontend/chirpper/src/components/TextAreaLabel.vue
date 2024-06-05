<template>
  <label :for="id" class="text-2md font-semibold">{{ label }}</label>
  <textarea
    :id="id"
    class="rounded-md bg-gray-300 focus:bg-white focus:outline-none focus:border-b-4 focus:border-blue-400 w-80 text-black"
    placeholder="Enter text here"
    :rows="row"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  ></textarea>
</template>

<script setup>
const props = defineProps(["label", "id", "modelValue", "row"]);
const emit = defineEmits(["update:modelValue"]);
</script>
