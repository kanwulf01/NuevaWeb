import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex);

/* idproducto: this.$route.params.idProducto*/

export const store = new Vuex.Store({
  state: {

    profile: { first_name: null, last_name: null, phone: null, cedula: null, direccion: null, passw: null },
    productos: { id_producto: null, nombre_producto: null, cantidad_producto: null, precio_unidad: null, descripcion: null, images: null },
    products: [],
    detalle: null,
    count:[],
   
  },
  getters: {
    profile: state => {
      return state.profile;
    },
    getProducts: state => {
      return state.products
    },
    getDetails: state => {
      return state.detalle
    },
    getCount: state => {
      return state.count
    },
    getProducts1: state => {
      return state.products1
    },
    
  }, plugins: [createPersistedState()],
  mutations: {
    setProfile: (state, pro) => {
      state.profile = pro;
    },
    setFieldProfilename: (state, field) => {
      state.profile.first_name = field;
    },
    setProfileCedula: (state,field) =>{
      state.profile.cedula = field;
    },
    setProducts: (state, field) => {
      state.products = field;
    },
    setDetalle: (state, field) => {
      state.detalle = field;
    },
    setCount: (state,field) =>{
      state.count = field;
    },
    setProducts1: (state, field) => {
      state.products1 = field;
    },
    setId:(state,field) =>{
      state.cedula = field;
    }
  },
  actions: {
    api_register: (context, credentials) => {
      return new Promise((resolve, reject) => {
        axios.post('http://localhost:8000/api/v1.0/clientes/', credentials)
          .then(res => {
            console.log(res.data);
            resolve(res);
          })
          .catch(err => {
            //console.log(err);
            reject(err);
          })
      })
    },
    setFieldProfile: (context) => {
      context.commit('setFieldProfile')
    },
    api_login: (context, credentials) => {

      return new Promise((resolve, reject) => {
        axios.get('http://localhost:8000/api/v1.0/busca/' + credentials.cedula + '/')
          .then(res => {
            resolve(res);

          })
      })
    },
    api_photos: (context, credentials) => {
      credentials.images = "../../static/"+credentials.images.name
      alert(credentials.images)
     axios.post('http://localhost:8000/api/v1.0/producto/', credentials)
        .then(res => {
          alert(res)
        }).catch(err => {
          console.log(err)
        })
        /*axios.post('http://localhost:8000/api/v1.0/Oferta/', credentials.id_producto)
        .then(res => {
          alert('Producto registrado Bien')
        }).catch(err=>{
          alert(err)
        })*/
    },

    api_oferta: (context, credentials) =>{
      axios.post('http://localhost:8000/api/v1.0/Oferta/', credentials)
      .then(res =>{
          alert('Registro finalizado')
      }).catch(err =>{
        alert(err)
      })
      
    },
    api_oferta1: (context, credentials) =>{

      axios.post('http://localhost:8000/api/v1.0/Oferta1/', credentials)
      .then(res =>{
        
      }).catch(err =>{
        
      })
      
    },
    api_trae: (context) =>{
      return new Promise((resolve, reject) => { 
        axios.get('http://localhost:8000/api/v1.0/listaproducto/')
      .then(res =>{
        resolve(res)})
        .catch(err => {
          console.log(err)
        })
      })

    }
    
  }
})