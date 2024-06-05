import axios from "axios";
import { ref } from "vue";

export function useAuth() {
    const accessToken = ref(null)
    const refreshToken = ref(null)

    const tryLogin = async (url, formData) => {
        try {
            const response = await axios.post(url, formData);
            console.log(response)
            return response
        } catch (e) {
            console.log(e)
        }
    }
    return{
        tryLogin
    }
}  