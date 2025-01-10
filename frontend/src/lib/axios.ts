import axios from 'axios';

export const api = axios.create({
    baseURL: 'http://localhost:5000/api/users/crud', // Ensure this URL matches your backend
});