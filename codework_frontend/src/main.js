import { createApp } from 'vue'
import App from './App.vue'
import RegisterUser from './components/authorization/Registration.vue'
import LoginUser from './components/authorization/Login.vue'
import UserProfile from './components/profile/Profile.vue'
import './assets/style.css'
import { createRouter, createWebHashHistory } from 'vue-router'
import vue3GoogleLogin from 'vue3-google-login'

const routes = [
  { path: '/', component: LoginUser, redirect: '/login-user'},
  { path: '/register-user', component: RegisterUser},
  { path: '/login-user', component: LoginUser},
  { path: '/user-profile', component: UserProfile, props: route => ({ query: route.query })},
]

const router = createRouter({
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

const app = createApp(App)

app.config.globalProperties.$hostname = 'http://localhost:8000'
app.config.globalProperties.$clientId = '82t4uuErHesipU0iIcfo3EwdVdHLzBb3dJnIJa9N'
app.config.globalProperties.$clientSecret = 'HjqdfMDu7ln4ypRjEqJ3gjlu24Ll1nbIKdnyROeLoG3yGLpXIvocMwv83NVvFIlMkh2o5b9LnJijaPIZCiAm04TjitcRAK2e2GTaNWui1HAEW1Nt4AjvacXmavgektJb'

app.use(router)
app.use(vue3GoogleLogin, {
  clientId: '****************************.apps.googleusercontent.com'
})

app.mount('#app')

