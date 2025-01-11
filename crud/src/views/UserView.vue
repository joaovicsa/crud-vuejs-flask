<template>
  <div>
    <h1>User: {{ username }}</h1>
    <div v-if="user">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Roles:</strong> {{ user.roles.join(', ') }}</p>
      <p><strong>Timezone:</strong> {{ user.preferences.timezone }}</p>
      <p><strong>Created At:</strong> {{ new Date(user.created_ts * 1000).toLocaleString() }}</p>
      <p><strong>Active:</strong> {{ user.active ? 'Yes' : 'No' }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getUser } from '@/lib/userService';

export default defineComponent({
  name: 'UserView',
  setup() {
    const route = useRoute();
    const username = route.params.username as string;
    interface User {
      username: string;
      roles: string[];
      preferences: {
        timezone: string;
      };
      created_ts: number;
      active: boolean;
    }

    const user = ref<User | null>(null);

    onMounted(async () => {
      user.value = await getUser(username);
    });

    return { username, user };
  }
});
</script>