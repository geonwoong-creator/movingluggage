<!-- src/components/Home.vue -->
<template>
    <div>
      <h1>Reservation Page</h1>
      <button @click="sendReservation">Send Reservation</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'HomePage',
    methods: {
      async sendReservation() {
        const reservationData = {
          name: "John Doe",
          date: "2024-11-04",
          time: "14:00",
          pickupLocation: "Seoul",
          destination: "Incheon Airport"
        };
        
        try {
          const response = await axios.post('http://127.0.0.1:5000/reserve', reservationData);
          console.log("Reservation Response:", response.data);
        } catch (error) {
          console.error("Error sending reservation:", error);
        }
      }
    }
  }
  </script>
  