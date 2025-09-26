<script setup>
import {onMounted, ref} from 'vue'
import DataTable from 'primevue/datatable';
import ProgressSpinner from 'primevue/progressspinner';
import Message from 'primevue/message';
import Column from 'primevue/column';
import axios from 'axios';

const cdrs = ref();
let showLoading = ref(false)
let showError = ref(false)
let showSuccess = ref(false)

onMounted(() => {
  axios.get('/cdr').then((response) => (cdrs.value = response['data']))
});

function uploadFile(event) {
  showError.value = false
  showSuccess.value = false
  let formData = new FormData();
  const file = event.target.files[0];
  formData.append('file', file);
  showLoading.value = true;

  axios.post('/cdr', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
      .then(function (response) {
        showLoading.value = false;
        showSuccess.value = true
        axios.get('/cdr').then((response) => (cdrs.value = response['data']))
      })
      .catch(function (error) {
        showLoading.value = false;
        showError.value = true
      });
}

</script>

<template>
  <div class="app">
    <div>
      <Message severity="error" v-if="showError">Something has gone wrong uploading your CDR! Oh no!</Message>
      <Message severity="success" v-if="showSuccess">Your CDR has successfully uploaded! Table will update momentarily.</Message>
      <h2>Upload new CDR</h2>
      <input v-if="!showLoading" id="file-input" type="file" @change="uploadFile($event)" />
      <ProgressSpinner v-if="showLoading" />
    </div>
    <div>
      <h2>Entries</h2>
      <DataTable :value="cdrs" tableStyle="min-width: 50rem">
          <Column field="id" header="ID"></Column>
          <Column field="mnc" header="MNC"></Column>
          <Column field="bytes_used" header="Bytes Used"></Column>
          <Column field="dmcc" header="DMCC"></Column>
          <Column field="cellid" header="Cell ID"></Column>
          <Column field="ip" header="IP"></Column>
      </DataTable>
    </div>
  </div>
</template>

<style scoped>
</style>
