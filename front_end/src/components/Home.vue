<template>
    <div class="home">
      
            <Cartas></Cartas>
      
           <router-view/>
       
         
    </div>
   
</template>
<script>

import Cartas from '@/components/Cartas.vue'
import Navbar from '@/components/Navbar.vue'
import axios from "axios";

import { mapGetters, mapMutations} from 'vuex'

export default {
    
    name: 'home',
    components: {
        Cartas,Navbar
    },
    computed:{
        ...mapGetters([
            'getProducts'
        ]),
        traerProducts(){
            return this.getProducts
        }
    },
    methods:{
        ...mapMutations([
            'setProducts',
            'setCount'
        ]),
        getProductos(){
            const path =  'http://localhost:8000/api/v1.0/test1/'
            axios.get(path).then((response)=>{
               // this.setProductos(response.data)
                this.setProducts(response.data)
                alert(this.getProducts[0].productos.nombre_producto)
            }).catch((err)=>{
                console.log(err)
                
            })
        },
        getProducts2(){
            this.$store.dispatch('api_trae')
            .then(res =>{
                this.setCount(res.data)
              
            }).catch(err =>{
                alert(err)
            })
        }
    }, created(){
        this.getProductos(),
        this.getProducts2()
    }
}
</script>
<style>

</style>
