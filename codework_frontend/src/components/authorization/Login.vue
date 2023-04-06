<template>
    <section class="h-screen">
      <div class="h-full">
        <div
          class="g-6 flex h-full flex-wrap items-center justify-center align-middle">
          <div class="mb-12 md:mb-0 md:w-8/12 lg:w-5/12 xl:w-5/12">
            <form>
              <div
                class="flex flex-row items-center justify-center lg:justify-start">
                <p class="mb-0 mr-4 text-lg">Sign in with</p>
                <button
                  @click="login"
                  type="button"
                  data-te-ripple-init
                  data-te-ripple-color="light"
                  class="mx-1 h-9 w-9 rounded-full bg-primary uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)]">
                  <svg 
                    xmlns="http://www.w3.org/2000/svg"
                    class="mx-auto h-3.5 w-3.5 "
                    viewBox="0 0 488 512">
                    <path d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"/>
                  </svg>
                </button>
              </div>
  
              <div
                class="my-4 flex items-center before:mt-0.5 before:flex-1 before:border-t before:border-neutral-300 after:mt-0.5 after:flex-1 after:border-t after:border-neutral-300">
                <p
                  class="mx-4 mb-0 text-center font-semibold dark:text-white">
                  Or
                </p>
              </div>
  
              <!-- Email input -->
              <div class="mb-6">
                <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
                <input v-model="loginData.email" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Email" required>
              </div> 
  
              <!-- Password input -->
              <div class="mb-6">
                <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                <input v-model="loginData.password" type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Password" required>
              </div> 
  
              <p v-if="haveError" class="text-red mb-4">{{errorText}}</p>
  
              <div class="text-center lg:text-left">
                <button
                  v-on:click="loginUser"
                  type="submit"
                  class="inline-block rounded bg-[#1da1f2] px-7 pt-3 pb-2.5 text-sm font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)]"
                  data-te-ripple-init
                  data-te-ripple-color="light">
                  Login
                </button>
                <p class="mt-2 mb-0 pt-1 text-sm font-semibold">
                  New User?
                  <router-link
                    to="/register-user"
                    class="text-tahiti transition duration-150 ease-in-out hover:text-danger-600 focus:text-danger-600 active:text-danger-700"
                    >Sign In
                  </router-link>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
  </section>
</template>

<script setup >
import axios from 'axios';
import { googleTokenLogin } from "vue3-google-login"
import { useRouter } from 'vue-router';

  const router = useRouter()
  const login = () => {
    googleTokenLogin().then((response) => {
      const clientId = 'zneEsc6NrR4prHbMGcUoOPHxabFWH3BVgKtrYL8v'
      const clientSecret = '6zso7csDVAF8wfGmBxrCaWapivq5CZAJmNAa0DkXyflDvRHwowqQ1qFjTH6SUZ9X9Gup6REPCtdXEWl70X5QVMjODBSmVaTNRxQsi2KAX9Pn0GPHupXXi8nrpiBeFPfn'
      const getInfoUrl = 'https://www.googleapis.com/oauth2/v1/userinfo'
      const hostname = 'http://localhost:8000'
      if(response.access_token) {
        console.log(response)
        let data = JSON.stringify({
          token: response.access_token,
          backend: "google-oauth2",
          grant_type: "convert_token",
          client_id: clientId,
          client_secret: clientSecret
        })

        let user_data
        axios.get(`${getInfoUrl}?access_token=${response.access_token}`)
        .then(function (response) {
          console.log(response.data);
          user_data = response.data
        })

        axios.post(`${hostname}/api-auth/convert-token`, data, {
          headers: {
              'Content-Type': 'application/json'
            }
          }).then(function (response) {
            if(response.data.access_token){
              console.log(user_data)
              router.push({path:'/user-profile', query: {first_name: user_data.family_name, last_name: user_data.given_name, email: user_data.email}})
              console.log(response)
            }
          }).catch(function (error) {
            console.log(error.data);
        });        
      }
    })
  }

</script>

  
<script>
  export default {
    name: "LoginUser",
    data() {
      return {
        name: "abin",
        haveError: false,
        errorText: "",
        loginData: {}
      }
    },
    methods: {
      loginUser(){
        if(this.loginData.email && this.loginData.password){
          let data = JSON.stringify(this.loginData)
          console.log(data)
          axios.post(`${this.$hostname}/api-auth/login-user`, data, {
            headers: {
              'Content-Type': 'application/json'
            }
          }).then((response) => {
            console.log(response)
            if(response.data.access_token){
              this.$router.push({path:'/user-profile', query: {first_name: response.data.user_data.first_name, last_name: response.data.user_data.last_name, email: response.data.user_data.email}})
              console.log(response)
            }
          }).catch((error) => {
            console.log(error.response)
            this.haveError = true
            this.errorText = error.response.data.status_text
          });
        }
      }
    }
  }
</script>
