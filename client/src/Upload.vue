<script setup>
import axios from 'axios';

function uploadFile(event) {
  let formData = new FormData();
  const file = event.target.files[0];
  formData.append( 'file', file );

  axios.post('/cdr', formData, {headers: {
        'Authorization': 'Bearer '+this.token,
        'Content-Type': 'multipart/form-data'
    }})
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

    <input id="file-input" type="file" @change="uploadFile($event)" />
  </div>
</template>

<style scoped>
</style>
