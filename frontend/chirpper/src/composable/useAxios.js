import axios from "axios";
import { ref } from "vue";

export function useAxios() {
  const tryFetch = async (url, accessToken) => {
    try {
      const response = await axios.get(url, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      return response;
    } catch (error) {
      return null;
    }
  };

  return {
    tryFetch,
  };
}
