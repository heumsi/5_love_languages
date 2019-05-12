<template>
  <div>
    <b-navbar>
      <b-navbar-brand href="#">사랑의 5가지 언어</b-navbar-brand>
      <b-navbar-toggle target="nav_collapse"/>
      <b-collapse is-nav id="nav_collapse">
         <b-navbar-nav>
           <b-nav-item href="#">사랑의 언어 검사</b-nav-item>
           <b-nav-item href="#">사랑의 5가지 언어 유형</b-nav-item>
           <b-nav-item href="#">연락처</b-nav-item>
         </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
export default {
  name: "Header",
  data() {
    return {}
  }
}
</script>
