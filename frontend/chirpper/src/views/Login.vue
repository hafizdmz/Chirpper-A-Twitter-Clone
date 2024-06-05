<template>
    <div class="w-96 self-center mt-56">
        <form @submit.prevent="handleLogin" class="flex flex-col">
            <h1 class="text-2xl text-center mb-10">Nestle in, Chirppers!</h1>
            <Input id-input="username" label-name="Username" input-type="text" v-model="userData.username"/>
            <Input id-input="password" label-name="Password" input-type="password" v-model="userData.password"/>
            <Button button-type="submit" @click="handleLogin" class=" w-36 self-center">Submit</Button>
            <h2 class="self-center mt-5">Don't have account?</h2>
            <RouterLink to="/register" class="text-blue-500 hover:underline underline-offset-4 self-center">Joint the nest here!</RouterLink>
        </form>
    </div>
</template>

<script setup>
import Form from '../components/Form.vue';
import Input from '../components/Input.vue';
import Button from '../components/Button.vue';

import {reactive, ref} from 'vue'
import { useRouter, RouterLink } from 'vue-router';
import { useAuth } from '@/composable/useAuth';
// import {useAuthStore} from '../stores/authStore'

// const {setToken} = useAuthStore()
const router = useRouter()

const tryLogin = useAuth
// const { tryLogin, success, accessToken, refreshToken} = useAuth()


const userData = reactive({
    username: '',
    password: ''
})
const handleLogin = async() => {
    await tryLogin(import.meta.env.VITE_API_BASEURL+'/api/auth/login', userData)
}
</script>

