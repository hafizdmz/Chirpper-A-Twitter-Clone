<template>
    <div class="w-96 self-center mt-36">
        <Form class="flex flex-col">
            <h1 class="text-2xl text-center mb-10">Come, Join The Flocks!</h1>
            <Input id-input="usermame" label-name="Username" input-type="text" v-model="userData.username"/>
            <Input label-name="Email" input-type="email" v-model="userData.email"/>
            <Input label-name="Password" input-type="password" v-model="userData.password"/>
            <Input label-name="Reconfirm Password" input-type="password" v-model="confirmPass"/>
            <Button button-type="submit" @click="handleRegister" class=" w-36 self-center">Submit</Button>
            <RouterLink to="/login" class="text-blue-500 hover:underline mt-3 self-center" >Have an Account? Back to Login Page</RouterLink>
        </Form>
    </div>
</template>

<script setup>
import Form from '../components/Form.vue';
import Input from '../components/Input.vue';
import Button from '../components/Button.vue';

import {reactive, ref} from 'vue'
// import { useAuth } from '../composable/useAuth';
import {RouterLink} from 'vue-router'
const userData = reactive({
    username: '',
    password: '',
    email: '',

})


const confirmPass = ref('')


const success = ref(false)
const message = ref()


// const { tryAuth } = useAuth()

// const handleRegister = async () =>{
//     if(confirmPass.value = userData.password){
//         const result = await tryAuth(import.meta.env.VITE_API_BASEURL + '/api/auth/register', userData)
//         success.value = result.data.success
//         message.value = result.data.message
//     }
// }
</script>
