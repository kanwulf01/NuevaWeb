<template >
<div id="navbarx">
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="/">NEUROMARKET</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      
      <li class="nav-item dropdown">
       <b-form-select v-model="selected" :options="this.categorias"  @change = "getCateProducts()" class="nav-item">
                  <!-- This slot appears above the options from 'options' prop -->
                  <template slot="first">
                    <option :value="null" disabled>CATEGORIAS</option>
                  </template>
                </b-form-select>   
      </li>
       <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Que estas buscando?" aria-label="">
      <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Buscar</button>
    </form>
     
       <li class="nav-item">
        
        
      </li>
       <li class="nav-item right" v-if="this.TraeNombre">
        <a></a>
      
      </li>
      <li class="nav-item" v-else>
          <a class="nav-link" href="r" >Registrarse</a>
      </li>
     
     
       <li class="nav-item right" v-if="this.TraeNombre">
        
        <a class="nav-link" href="profile" >{{profile.first_name}}</a>
      </li>
      <li class="nav-item" v-if="this.TraeNombre">
        <a class="nav-link" href="vende">Vender</a>
      </li>
      <li class="nav-item" v-if="this.TraeNombre">
        <button class="nav-link btn btn-primary" @click="deleteUser()">logout</button>
      </li>
      <li class="nav-item" v-else>
        <a class="nav-link" href="login" >Login</a>
      </li>
     
    </ul>
   
  </div>
    

</nav>

</div>


</template>

<script>


import Cartas from '@/components/Cartas.vue'
import axios from "axios";
import sawl from 'sweetalert'
import { mapGetters, mapMutations} from 'vuex'
export default {

  data(){
    return{
      categorias:[],
      selected: null
    }
  },
components:{
  'cartas':Cartas
},methods:{
  ...mapMutations([
    'setFieldProfilename',
    'setCategorias',
    'setProducts'
  ]),
  getCategorias(){
      const path =  'http://localhost:8000/api/v1.0/categoria/'
      axios.get(path).then((response)=>{
          this.categorias = [];             
          this.setCategorias(response.data)
          for (var i = response.data.length - 1; i >= 0; i--) {
            var categoria = { value: response.data[i].id_categoria, text: response.data[i].nombre_categoria };
            this.categorias.push(categoria);
          }
          console.log(this.categorias)
          
      }).catch((err)=>{
          console.log(err)
          
      })
  },
  getCateProducts(){
    
    if(this.selected){
      this.$store.dispatch('api_productoCategoria', this.selected)
        .then(response => {
          console.log(response)
          this.setProducts(response.data)
        })
        .catch(err => {
          console.log(this.err);
          
       

        });      
    }
    
  },
  deleteUser: function(){
    this.setFieldProfilename("");
    sawl('Usted cerro su sesion','','success')
    this.$router.push({path: '/'});
  }
},
created(){
  this.getCategorias()
},
computed:{
  ...mapGetters([
    'profile',

  ]),
  TraeNombre(){
    if(this.profile.first_name==""){
      return false
    }else{return true}
    
  }
}
}

</script>

<style scoped>

#navbarx{
    position: fixed;
    top: 0%;
    left: 0;
    width: 100%;
}
/* adds some margin below the link sets  */
.navbar .dropdown-menu div[class*="col"] {
   margin-bottom:1rem;
}

.navbar .dropdown-menu {
  border:none;
  background-color:#48D1CC!important;
}

/* breakpoint and up - mega dropdown styles */
@media screen and (min-width: 600px) {
  
  /* remove the padding from the navbar so the dropdown hover state is not broken */
.navbar {
  padding-top:0px;
  padding-bottom:0px;
}

/* remove the padding from the nav-item and add some margin to give some breathing room on hovers */
.navbar .nav-item {
  padding:.5rem .5rem;
  margin:0 .25rem;
  color:blue
}

/* makes the dropdown full width  */
.navbar .dropdown {position:static;}

.navbar .dropdown-menu {
  width:100%;
  left:0;
  right:0;
/*  height of nav-item  */
  top:45px;
  
  display:block;
  visibility: hidden;
  opacity: 0.9;
  transition: visibility 0s, opacity 0.3s linear;
  
}
  
 

  
  /* shows the dropdown menu on hover */
.navbar .dropdown:hover .dropdown-menu, .navbar .dropdown .dropdown-menu:hover {
  display:block;
  visibility: visible;
  opacity: 2;
  transition: visibility 0s, opacity 0.3s linear;
}
  
  .navbar .dropdown-menu {
    border: 1px solid rgba(0,0,0,.15);
    background-color: #fff;
  }

}

a{
color:blue
}



</style>
