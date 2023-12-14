<template>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-text-field v-model="searchQuery" label="Search" clearable></v-text-field>
      </v-col>
    </v-row>
    
    <v-data-table :headers="headers" :items="filteredUsers" >      
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
        <v-icon size="small" class="me-2" @click="editItem(item)" style="background-color: red;">mdi-pencil</v-icon>
        <v-icon size="small" @click="deleteItem(item)" style="background-color: red;">mdi-delete</v-icon>
      </template>
      
    </v-data-table>
</template>
  

<script setup>
import { ref, onMounted } from 'vue';

const searchQuery = ref('');
const filteredUsers = ref([]);
const dialog = ref(false);
const dialogDelete = ref(false);
const editedIndex = ref(-1);

const editedItem = ref({
  id: '',
  firstName: '',
  lastName: '',
  phone: '',
  email: '',
});

const defaultItem = {
  id: '',
  firstName: '',
  lastName: '',
  phone: '',
  email: '',
};

const headers = [
  { title: 'Id', key: 'id' },
  { title: 'First Name', key: 'firstName' },
  { title: 'Last Name', key: 'lastName' },
  { title: 'Phone', key: 'phone' },
  { title: 'Email', key: 'email' },
];


const editItem = (item) => {
  editedIndex.value = filteredUsers.value.indexOf(item);
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
    Object.assign(filteredUsers.value[editedIndex.value], editedItem.value);
  } else {
    filteredUsers.value.push(editedItem.value);
  }
  close();
};

const deleteItem = (item) => {
  editedIndex.value = filteredUsers.value.indexOf(item);
  editedItem.value = { ...item };
  dialogDelete.value = true;
};

const deleteItemConfirm = () => {
  filteredUsers.value.splice(editedIndex.value, 1);
  closeDelete();
};

const closeDelete = () => {
  dialogDelete.value = false;
  editedItem.value = { ...defaultItem };
  editedIndex.value = -1;
};

// Fetch user data from the database on component mount
onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/employees');
    const data = await response.json();

      const employeesArray = Object.keys(data).map(key => ({
        id: key,
        ...data[key]
      }));


    filteredUsers.value = employeesArray;
    console.log('User data fetched:', employeesArray)
  } catch (error) {
    console.error('Error fetching user data:', error);
  }
});
</script>

<style scoped>



</style>