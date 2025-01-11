<template>
  
  <v-container>
    <v-card>
      <v-card-title>
        <span class="headline">Users</span>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="dialog = true">Create User</v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="users"
        item-key="username"
        class="elevation-1"
      >
        <template #item="{ item }">
          <router-link :to="`/user/${item.username}`">{{ item.username }}</router-link>
        </template>
        <template v-slot:#item="{ item }">
          <v-icon small @click="editUser(item)">mdi-pencil</v-icon>
          <v-icon small @click="confirmDeleteUser(item.username)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>
    <UserForm
      :dialog="dialog"
      :user="selectedUser"
      :isEdit="isEdit"
      @close="dialog = false"
      @save="fetchUsers"
    ></UserForm>
    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline">Are you sure?</v-card-title>
        <v-card-text>Do you really want to delete this user? This process cannot be undone.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" @click="deleteUser">Delete</v-btn>
          <v-btn @click="deleteDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { getUsers, deleteUser as deleteUserService, User } from '@/lib/userService';
import UserForm from '@/components/UserForm.vue';

export default defineComponent({
  components: {
    UserForm,
  },
  setup() {
    const dialog = ref(false);
    const deleteDialog = ref(false);
    const isEdit = ref(false);
    const selectedUser = ref<User | null>(null);
    const users = ref<User[]>([]);
    const headers = [
      { text: 'Username', value: 'username' },
      { text: 'Roles', value: 'roles' },
      { text: 'Timezone', value: 'preferences.timezone' },
      { text: 'Is Active?', value: 'active' },
      { text: 'Last Updated At', value: 'updated_at' },
      { text: 'Created At', value: 'created_ts' },
      { text: 'Actions', value: 'actions', sortable: false },
    ];
    const userToDelete = ref<string | null>(null);

    const fetchUsers = async () => {
      try {
        users.value = await getUsers();
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    const editUser = (user: User) => {
      selectedUser.value = user;
      isEdit.value = true;
      dialog.value = true;
    };

    const confirmDeleteUser = (username: string) => {
      userToDelete.value = username;
      deleteDialog.value = true;
    };

    const deleteUser = async () => {
      if (userToDelete.value) {
        try {
          await deleteUserService(userToDelete.value);
          fetchUsers();
        } catch (error) {
          console.error('Error deleting user:', error);
        } finally {
          deleteDialog.value = false;
        }
      }
    };

    onMounted(fetchUsers);

    return {
      dialog,
      deleteDialog,
      isEdit,
      selectedUser,
      users,
      headers,
      fetchUsers,
      editUser,
      confirmDeleteUser,
      deleteUser,
    };
  },
});
</script>

<style scoped>

</style>