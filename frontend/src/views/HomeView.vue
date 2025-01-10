<template>
  <div>
    <h1>Home</h1>
    <router-link to="/user/johndoe">Go to John Doe's User Page</router-link>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
});
</script>