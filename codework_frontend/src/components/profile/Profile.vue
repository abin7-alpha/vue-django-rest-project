<template>
  <section class="pt-16 bg-blueGray-50">
    <div class="w-full lg:w-4/12 px-4 mx-auto">
      <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16">
        <div class="px-6">
          <div class="text-center mt-12">
            <h3 class="text-xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
              {{query.first_name}} {{query.last_name}}
            </h3>
            <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold">
              <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
              Email: {{query.email}}
            </div>
          </div>
          <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
            <div class="flex flex-wrap justify-center">
              <div class="w-full lg:w-9/12 px-4">
                <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
                  An artist of considerable range, Jenna the name taken
                  by Melbourne-raised, Brooklyn-based Nick Murphy
                  writes, performs and records all of his own music,
                  giving it a warm, intimate feel with a solid groove
                  structure. An artist of considerable range.
                </p>
                <a href="javascript:void(0);" class="font-normal text-pink-500">
                  Show more
                </a>
              </div>
            </div>
          </div>
          <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
            <button class="inline-block rounded bg-midnight px-7 pt-3 pb-2.5 text-sm font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)]">
              <router-link
                to="/login-user"
                class="text-tahiti transition duration-150 ease-in-out hover:text-danger-600 focus:text-danger-600 active:text-danger-700"
                >Logout
              </router-link>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "UserProfile",
    props: ['query'],
  }
</script>