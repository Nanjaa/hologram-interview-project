<template>
  <div class="hello">
    <h2>{{ title }}</h2>
    <p>This is a Vue component!</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    title: {
      type: String,
      default: 'Hello from Vue'
    }
  }
}
</script>

<style scoped>
.hello {
  font-family: Arial, sans-serif;
  color: #333;
}
</style>
