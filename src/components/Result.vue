<template>
  <div class="container">
    <div>
      <b-table :fixed="true" :borderless="false" 
      :items="values" :fields="fields"
       ></b-table>
    </div>
  </div>
</template>
<script>
export default {
  name: "Result",
  data() {
    const result = this.$route.params;

    var values = [];
    values.push(result);
    return {
      values: values,
      fields: [
        {
          key: "A",
          label: "인정하는 말"
        },
        {
          key: "B",
          label: "함께하는 시간"
        },
        {
          key: "C",
          label: "선물"
        },

        {
          key: "D",
          label: "봉사"
        },

        {
          key: "E",
          label: "스킨십"
        }
      ]
    };
  }
};
</script>
