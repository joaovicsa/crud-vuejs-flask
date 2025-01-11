import { api } from './axios';

interface UserPreferences {
    timezone: string;
}

interface User {
    username: string;
    password: string;
    roles: string[];
    preferences: UserPreferences;
    created_ts: number;
    active: boolean;
}

// Get all users
export const getUsers = async (): Promise<User[]> => {
    const response = await api.get('/users');
    return response.data;
};

// Add a new user
export const addUser = async (userData: User): Promise<void> => {
    await api.post('/users', userData);
};

// Update a user
export const updateUser = async (username: string, userData: Partial<User>): Promise<void> => {
    await api.put(`/users/${username}`, userData);
};

// Delete a user
export const deleteUser = async (username: string): Promise<void> => {
    await api.delete(`/users/${username}`);
};