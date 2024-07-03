import axios from "axios";

const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASEURL,
  timeout: 100000,
  headers: { "X-Custom-Header": "foobar" },
});



export default axiosInstance