import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/Login.vue";
import RegisterView from "../views/Register.vue";
import LeaderboardView from "../views/Leaderboard.vue";
// import { useAuthStore } from "../stores/authStore.js";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/leaderboard",
      name: "leaderboard",
      component: LeaderboardView,
      meta: {
        requiresAuth: false,
      },
    },
  ],
});

// router.beforeEach((to, from, next) => {
//   const authStore = useAuthStore();

//   if (to.meta.requiresAuth) {
//     if (authStore.isAuthenticated) {
//       next();
//     } else {
//       next("/login");
//     }
//   } else {
//     next();
//   }
// });

export default router;
