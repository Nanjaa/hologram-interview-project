<script setup>
import axios from 'axios';

function uploadFile() {
  console.log('hello')
  axios.post('/cdr', {})
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}
</script>

<template>
  <div class="upload">
    <h2>Upload File</h2>
    <p>This is where we'll upload our files</p>

    <input id="file-upload" type="file" @change="uploadFile" />
  </div>
</template>

<style scoped>
</style>
