<template>
  <div>
    <h1>User: {{ username }}</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRoute } from 'vue-router';

export default defineComponent({
  name: 'UserView',
  setup() {
    const route = useRoute();
    const username = route.params.username as string;

    return { username };
  }
});
</script>