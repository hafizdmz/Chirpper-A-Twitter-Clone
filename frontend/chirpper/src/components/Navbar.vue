<template>
    <header class='sticky top-0 bg-chirpper-gray shadow-lg'>
        <nav class="flex flex-row mx-52 items-center text-white py-6">
            <div class="flex items-center gap-3 flex-1">
                <i class="fa-solid fa-feather fa-xl"></i>
                <p class=" text-2xl"> Chirpper</p>
            </div>
            <ul class="self-center space-x-5">
                <RouterLink to="/"  active-class="border-b-2 border-white" class="hover:border-b-4 hover:border-white p-1 rounded-sm">Home</RouterLink>
                <RouterLink to="/leaderboard"  active-class="border-b-2 border-white" class="hover:border-b-4 hover:border-white p-1 rounded-sm">Leaderboard</RouterLink>
                <button @click="handleLogout" class="hover:border-b-4 border-white">Logout</button>
            </ul>
        </nav>

    </header>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
