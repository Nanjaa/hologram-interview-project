<script setup>
import {onMounted, ref} from 'vue'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import axios from 'axios';

const cdrs = ref();

onMounted(() => {
  console.log('this is a test')
  axios.get('/cdr').then((data) => (cdrs.value = data))
});

function uploadFile(event) {
  let formData = new FormData();
  const file = event.target.files[0];
  formData.append('file', file);

  axios.post('/cdr', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

</script>

<template>
  <div class="app">
    <div>
      <input id="file-input" type="file" @change="uploadFile($event)" />
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
