<template>
  <button
    :type="buttonType"
    class="bg-chirpper-blue rounded-lg w-80 p-3 my-5 text-white hover:bg-chirpper-darkblue"
    @click="$emit('handleClick')"
  >
    <slot> </slot>
  </button>
</template>

<script setup>
defineProps({
  class: String,
  isClicked: Boolean,
  buttonType: String,
  name: {
    type: String,
    default: "Submit",
  },
});

defineEmits(["handleClick"]);
</script>
