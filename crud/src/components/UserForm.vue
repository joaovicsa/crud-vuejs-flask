<template>
  <v-dialog  max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">{{ isEdit ? 'Edit User' : 'Create User' }}</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form">
          <v-text-field v-model="localUser.username" label="Username" :disabled="isEdit" required></v-text-field>
          <v-text-field v-model="localUser.password" label="Password" type="password" required></v-text-field>
          <v-text-field v-model="localUser.roles" label="Roles (comma separated)" required></v-text-field>
          <v-text-field v-model="localUser.preferences.timezone" label="Timezone" required></v-text-field>
          <v-switch v-model="localUser.active" label="Is Active?"></v-switch>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="submit">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    user: {
      type: Object,
      default: () => ({
        username: '',
        password: '',
        roles: '',
        preferences: {
          timezone: ''
        },
        active: true
      })
    },
    isEdit: {
      type: Boolean,
      default: false
    },
    dialog: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      localUser: JSON.parse(JSON.stringify(this.user))
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    submit() {
      if (this.isEdit) {
        axios.put(`http://localhost:5000/api/users/${this.localUser.username}`, this.localUser)
          .then(() => {
            this.$emit('save');
          })
          .catch(error => {
            console.error(error);
          });
      } else {
        axios.post('http://localhost:5000/api/users', this.localUser)
          .then(() => {
            this.$emit('save');
          })
          .catch(error => {
            console.error(error);
          });
      }
      this.close();
    }
  },
  watch: {
    user: {
      handler(newVal) {
        this.localUser = JSON.parse(JSON.stringify(newVal));
      },
      deep: true
    }
  }
};
</script>