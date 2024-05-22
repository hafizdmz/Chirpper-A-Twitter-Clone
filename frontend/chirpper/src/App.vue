<template>
  <div class="flex flex-col min-h-screen bg-chirpper-dark">
    <Navbar />
    <RouterView />
  </div>
</template>

<script setup>
import {RouterView} from 'vue-router'
import Navbar from './components/Navbar.vue';
</script>