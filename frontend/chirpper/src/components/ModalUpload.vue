<template>
  <Dialog :open="showModal" @close="$emit('toggleModal')">
      <div class="fixed inset-0 bg-black/50" aria-hidden="true" />
        <div class="fixed inset-0 flex w-screen items-center justify-center p-4">
          <DialogPanel class="w-96 h-96 bg-chirpper-gray rounded-lg p-5
            text-white">
            <DialogTitle class="text-2xl pb-5">
              Chirp what's on your mind
            </DialogTitle>
              <slot>

              </slot>
              <!-- <button @click="closeModal('deactivate')">Deactivate</button> -->
          </DialogPanel>
      </div>
  </Dialog>
</template>

<script setup>
defineProps(['modalTitle', 'modalDesc', 'showModal'])
defineEmits(['toggleModal'])
// import {
//   Dialog,
//   DialogPanel,
//   DialogTitle,
//   DialogDescription,
// } from '@headlessui/vue';


</script>