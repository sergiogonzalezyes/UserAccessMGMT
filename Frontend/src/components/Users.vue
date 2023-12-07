<template>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-text-field v-model="searchQuery" label="Search" clearable></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-select v-model="selectedRole" :items="roleOptions" label="Role" clearable item-text="text"></v-select>
        <p>Selected Role: {{ getRoleName(selectedRole) }}</p>
      </v-col>

      <v-col cols="12" sm="6" md="4">
        <v-select v-model="selectedApplication" :items="applicationOptions" label="Application" clearable item-text="text"></v-select>
        <p>Selected Application: {{ getApplicationName(selectedApplication) }}</p>
      </v-col>
    </v-row>
    
    <v-data-table :headers="headers" :items="filteredUsers" >
      <template v-slot:item.role="{ item }">
        {{ getRoleName(item.roleId) }}
      </template>
      <template v-slot:item.application="{ item }">
        {{ getApplicationName(item.applicationId) }}
      </template>
      
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Users</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ props }">
              <v-btn color="primary" dark class="mb-2" v-bind="props">New User</v-btn>
            </template>
            <v-card>
              <v-card-title><span class="text-h5">{{ formTitle }}</span></v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.id" label="Id"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.firstName" label="First Name"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.lastName" label="Last Name"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.phone" label="Phone"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.email" label="Email"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.hireDate" label="Hire Date"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-checkbox v-model="editedItem.isActive" label="Active"></v-checkbox>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="close">Cancel</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      
      <template v-slot:item.actions="{ item }">
        <v-icon size="small" class="me-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon size="small" @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
      
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
</template>
  

<script setup>
import { ref, computed } from 'vue';
import { useAppStore } from '@/store/app';

const store = useAppStore();


const searchQuery = ref('');
const selectedRole = ref('');
const selectedApplication = ref('');

const roleOptions = computed(() => {
  const options = store.roles.map((role) => ({ title: role.name, value: role.id }));
  console.log('hello', typeof(options[0].text));
  return options;
});


const applicationOptions = computed(() => {
  console.log(store.applications.map((app) => ({ title: app.name, value: app.id })));
  return store.applications.map((app) => ({ title: app.name, value: app.id }));
});

const filteredUsers = computed(() => {
  let filtered = store.users.filter((user) =>
    user.firstName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    user.lastName.toLowerCase().includes(searchQuery.value.toLowerCase()),
    console.log(filteredUsers)
  );

  if (selectedRole.value) {
    filtered = filtered.filter((user) => user.roleId === selectedRole.value);
  }

  if (selectedApplication.value) {
    filtered = filtered.filter((user) => user.applicationId === selectedApplication.value);
  }

  return filtered;
});

const dialog = ref(false);
const dialogDelete = ref(false);
const editedIndex = ref(-1);

const editedItem = ref({
  id: '',
  firstName: '',
  lastName: '',
  phone: '',
  email: '',
  hireDate: '',
  isActive: false,
  roleId: null,
  applicationId: null,
});

const defaultItem = {
  id: '',
  firstName: '',
  lastName: '',
  phone: '',
  email: '',
  hireDate: '',
  isActive: false,
  roleId: null,
  applicationId: null,
};

const formTitle = computed(() => (editedIndex.value === -1 ? 'New Employee' : 'Edit Employee'));

const headers = [
  { title: 'Id', key: 'id' },
  { title: 'First Name', key: 'firstName' },
  { title: 'Last Name', key: 'lastName' },
  { title: 'Phone', key: 'phone' },
  { title: 'Email', key: 'email' },
  { title: 'Hire Date', key: 'hireDate' },
  { title: 'Active', key: 'isActive' },
  { title: 'Role', key: 'role' },
  { title: 'Application', key: 'application' },
  { title: 'Actions', key: 'actions', sortable: false },
];

const getRoleName = (roleId) => {
  const role = store.roles.find((r) => r.id === roleId);
  return role ? role.name : '';
};

const getApplicationName = (applicationId) => {
  const app = store.applications.find((a) => a.id === applicationId);
  return app ? app.name : '';
};

const initialize = () => {
  // No need to initialize users here; data is fetched from the store.
};

const editItem = (item) => {
  editedIndex.value = store.users.indexOf(item);
  editedItem.value = { ...item };
  dialog.value = true;
};

const close = () => {
  dialog.value = false;
  editedItem.value = { ...defaultItem };
  editedIndex.value = -1;
};

const save = () => {
  if (editedIndex.value > -1) {
    Object.assign(store.users[editedIndex.value], editedItem.value);
  } else {
    store.users.push(editedItem.value);
  }
  close();
};

const deleteItem = (item) => {
  editedIndex.value = store.users.indexOf(item);
  editedItem.value = { ...item };
  dialogDelete.value = true;
};

const deleteItemConfirm = () => {
  store.users.splice(editedIndex.value, 1);
  closeDelete();
};

const closeDelete = () => {
  dialogDelete.value = false;
  editedItem.value = { ...defaultItem };
  editedIndex.value = -1;
};
</script>