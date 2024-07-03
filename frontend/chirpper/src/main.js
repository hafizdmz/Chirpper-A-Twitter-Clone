import { createApp } from "vue";
// import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router/index.js";
import "./assets/tailwind.css";

//fontawesome logo
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faFeather } from "@fortawesome/free-solid-svg-icons";
import { faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import { faThumbsDown } from "@fortawesome/free-solid-svg-icons";
import { faComment } from "@fortawesome/free-regular-svg-icons";

library.add(faFeather);
library.add(faThumbsUp);
library.add(faThumbsDown);
library.add(faComment);

const app = createApp(App);
// const pinia = createPinia();
app.component("font-awesome-icon", FontAwesomeIcon);

app.use(router);
// app.use(pinia);
app.mount("#app");
