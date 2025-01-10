<template>
  <v-card>
    <v-card-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click="createUser">Create User</v-btn>
    </v-card-title>
    <v-data-table :headers="headers" :items="users" item-key="username">
      <template v-slot:item="{ item }">
        <router-link :to="`/user/${item.username}`">{{ item.username }}</router-link>
      </template>
      <template v-slot:actions="{ item }">
        <v-icon small @click="editUser(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteUser(item.username)">mdi-delete</v-icon>
      </template>
    </v-data-table>
    <UserForm :dialog="dialog" :user="selectedUser" :isEdit="isEdit" @close="dialog = false" @save="fetchUsers"></UserForm>
  </v-card>
</template>

<script>
import UserForm from './UserForm.vue';
import axios from 'axios';

export default {
  components: {
    UserForm
  },
  data() {
    return {
      dialog: false,
      isEdit: false,
      selectedUser: null,
      users: [],
      headers: [
        { text: 'Username', value: 'username' },
        { text: 'Roles', value: 'roles' },
        { text: 'Timezone', value: 'preferences.timezone' },
        { text: 'Is Active?', value: 'active' },
        { text: 'Last Updated At', value: 'updated_at' },
        { text: 'Created At', value: 'created_ts' },
        { text: 'Actions', value: 'actions', sortable: false }
      ]
    };
  },
  created() {
    this.fetchUsers();
  },
  methods: {
    fetchUsers() {
      axios.get('http://localhost:5000/api/users')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    createUser() {
      this.selectedUser = {
        username: '',
        password: '',
        roles: '',
        preferences: {
          timezone: ''
        },
        active: true
      };
      this.isEdit = false;
      this.dialog = true;
    },
    editUser(user) {
      this.selectedUser = user;
      this.isEdit = true;
      this.dialog = true;
    },
    deleteUser(username) {
      if (confirm('Are you sure you want to delete this user?')) {
        axios.delete(`http://localhost:5000/api/users/${username}`)
          .then(() => {
            this.fetchUsers();
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  }
};
</script>