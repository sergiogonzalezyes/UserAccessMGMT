// Utilities
import { defineStore } from 'pinia';

export const useAppStore = defineStore('app', {
  state: () => ({
    applications: [
      { id: 1, name: 'Github' },
      { id: 2, name: 'Outlook' },
      { id: 3, name: 'Google Workspace' },
    ],
    users: [
      {
        id: 1,
        firstName: 'John',
        lastName: 'Doe',
        phone: '123-456-7890',
        email: 'john.doe@company.com',
        hireDate: '2023-01-15',
        isActive: true,
        roleId: 1, // You can associate users with roles if needed
        applicationId: 1, // You can associate users with applications
      },
      {
        id: 2,
        firstName: 'Jane',
        lastName: 'Smith',
        phone: '987-654-3210',
        email: 'jane.smith@company.com',
        hireDate: '2022-11-20',
        isActive: true,
        roleId: 2,
        applicationId: 2,
      },
      {
        id: 3,
        firstName: 'Michael',
        lastName: 'Johnson',
        phone: '555-555-5555',
        email: 'michael.johnson@company.com',
        hireDate: '2023-02-10',
        isActive: false,
        roleId: 1,
        applicationId: 3,
      },
    ],
    roles: [
      { id: 1, name: 'Admin' },
      { id: 2, name: 'User' },
    ],
    user_applications: [
      { user_id: 1, application_id: 1, assigned_date: '2023-01-01', unassigned_date: null },
      { user_id: 1, application_id: 2, assigned_date: '2023-02-01', unassigned_date: null },
      { user_id: 2, application_id: 1, assigned_date: '2023-03-01', unassigned_date: '2023-03-15' },
    ],
    application_roles: [
      { application_id: 1, role_id: 1, role_assigned_date: '2023-01-01', role_unassigned_date: null },
      { application_id: 2, role_id: 2, role_assigned_date: '2023-02-01', role_unassigned_date: null },
    ],
    user_roles: [
      { user_id: 1, role_id: 1, application_id: 1, role_assigned_date: '2023-01-01', role_unassigned_date: null },
      { user_id: 1, role_id: 2, application_id: 2, role_assigned_date: '2023-02-01', role_unassigned_date: null },
    ],
  }),
});
