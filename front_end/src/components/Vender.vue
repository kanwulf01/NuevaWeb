<template>
     <div class="container">
       <form v-on:submit.prevent="register2">
           <fieldset>
               <legend>Especifique lo que desea vender</legend>
               <table style="margin: 0 auto;">
                 <tr>
                   <td><label> Código:</label></td>
                   <td><input required type="number" v-model="dat.id_producto" ></td>
                 </tr>
                 <tr>
                   <td><label>Nombre:</label></td>
                   <td><input required  type="text" v-model="dat.nombre_producto" placeholder="Nombre Claro del Producto"></td>
                 </tr>
                 <tr>
                   <td><label>Cantidad del Producto:</label></td>
                   <td><input  required  placeholder="Cantidad" type="number" v-model="dat.cantidad_producto"></td>
                 </tr>
                 <tr>
                   <td><label >Precio:</label></td>
                   <td><input  required  placeholder="$Valor$" type="number" v-model="dat.precio_unidad"></td>
                 </tr>
                 <tr>
                   <td><label>Categoría: </label></td>
                   <td>
                      <b-form-select v-model="dat.categoria_id" :options="this.categorias"   class="nav-item">
                        <!-- This slot appears above the options from 'options' prop -->
                        <template slot="first">
                          <option :value="null" disabled>Seleccione...</option>
                        </template>
                      </b-form-select>
                   </td>
                 </tr>
               </table>    
             
               <br>           
               
               <label>Descripcion</label>
               <b-form-textarea
                  id="textarea"
                  placeholder="Caracteristicas del articulo..."
                  rows="3"
                  max-rows="3"
                  v-model="dat.descripcion"
                ></b-form-textarea>
               <b-form-file
                v-model="dat.images"
                :state="Boolean(dat.images)"
                placeholder="Choose a file..."
                drop-placeholder="Drop file here..."
              ></b-form-file>
              <div class="mt-3">Selected file: {{ dat.images ? dat.images.name : '' }}</div>
           </fieldset>
            <button btn btn-primary>Registrar Producto</button>
       </form>
    </div>
</template>
<script>
import { mapGetters} from 'vuex'
import axios from "axios";
export default { 
  data() {
    return {
      dat:{
          id_producto:null,
          nombre_producto:null,
          cantidad_producto:null,
          precio_unidad:null,
          descripcion:null,
          images: null, 
          categoria_id:null  
      },
      oferta:{
        vendedor:null,
        productos:null,
      },
      categorias:[],
      selected: null
    }
  },
  computed:{
    ...mapGetters([
         'profile',
         'getProducts'
       ]),
  },
  methods:{
    getCategorias(){
        const path =  'http://localhost:8000/api/v1.0/categoria/'
        axios.get(path).then((response)=>{
            this.categorias = [];             
            
            for (var i = response.data.length - 1; i >= 0; i--) {
              var categoria = { value: response.data[i].id_categoria, text: response.data[i].nombre_categoria };
              this.categorias.push(categoria);
            }
            console.log(this.categorias)
        }).catch((err)=>{
            console.log(err)
            
        })
    },       
     register2(){
      this.$store.dispatch('api_photos',this.dat)
      .then(response =>{
          if(response){
            this.registraOferta()
          }        
        })

       
         
     },
     registraOferta(){
      this.oferta.productos = this.dat.id_producto
      this.oferta.vendedor = this.profile.cedula
      alert(this.oferta.vendedor + this.oferta.productos)
      this.$store.dispatch('api_oferta',this.oferta)
      .then(response =>{
        alert('Se registro todo bien')
      })

     },
     registra1(){
       this.$store.dispatch('api_oferta1',this.oferta.booleano)
       .then(res =>{

       })
     }
  },
  created(){
    this.getCategorias()
  }
  
  }
 

</script>
<style>

</style>
