<template>
      <button class="bg-chirpper-blue rounded-lg w-80 p-3 my-5 text-white hover:bg-chirpper-darkblue" @click=" $emit('handleClick')">
        <slot>
        </slot>
      </button>
</template>

<script setup>
defineProps(['name'])
defineEmits(['handleClick'])

</script>
