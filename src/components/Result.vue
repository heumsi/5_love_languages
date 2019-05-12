<template>
  <div class="container">
    <div>
      <b-table :fixed="true" :borderless="false" 
      :items="values" :fields="fields"
       ></b-table>
    </div>
    <div class="type_outter_box">
      <div v-for="(type, index) in top" :key="index" class="type_item_box">
        <h2> {{index + 1}}순위. {{type.name}} </h2>
        <p>{{type.desc}}</p>
      </div>
    </div>
  </div>
</template>
<script>
import type_name from '@/assets/type_name.json'

export default {
  name: "Result",
  data() {
    const result = this.$route.params;

    var values = [];
    values.push(result);

    let type_name_sorted = Object.keys(result);
    type_name_sorted.sort((a, b) => {return result[b] - result[a]});
    
    let top = type_name_sorted.slice(0, 3)
    var top_name = []
    for (var i in top) {
      top_name.push(type_name[top[i]])
    }

    return {
      values: values,
      fields: [
        {
          key: "A",
          label: type_name["A"].name,
        },
        {
          key: "B",
          label: type_name["B"].name
        },
        {
          key: "C",
          label: type_name["C"].name
        },
        {
          key: "D",
          label: type_name["D"].name
        },
        {
          key: "E",
          label: type_name["E"].name
        }
      ],
      top: top_name
    };
  }
};
</script>

<style scoped>
.type_item_box {
  margin: 30px 0;
}
</style>

