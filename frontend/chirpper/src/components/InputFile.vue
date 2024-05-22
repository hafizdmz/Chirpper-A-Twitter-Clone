<template>
    <div class="items-center">
        <label
        class=" bg-chirpper-blue hover:bg-chirpper-darkblue py-2 px-4 rounded cursor-pointer"
        >
        <span>{{ buttonText }}</span>
        <input
        :id="id"
          type="file"
          class="hidden"
          @change="handleFileChange"
          :value="modelValue"
        />
    </label>
      <span v-if="selectedFile">{{ selectedFile.name }}</span>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue';
  const { buttonText, id} = defineProps(['buttonText', 'id']);
  const emits = defineEmits(['update:modelValue']);
  
  const selectedFile = ref(null);
  
  function handleFileChange(event) {
    selectedFile.value = event.target.files[0];
    emits('update:modelValue', selectedFile.value);
    // You can emit an event or perform additional actions with the selected file here
  }
  </script>
  