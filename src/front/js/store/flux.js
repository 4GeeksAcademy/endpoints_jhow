
const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			movie: {},
			results: [], 
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMovie: () => {
				console.log("Hola desde flux");
				const options = {
					method: 'GET',
					headers: {
						accept: 'application/json',
						Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5M2ZhNzNkZjUyZTYyNWQ5NGQ1NzMyNGI1YTFlNDgzYSIsInN1YiI6IjY1OTQwNzAwY2U0ZGRjNmQzODdmMDIzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNQabtAWxQcVNGg9_oMH8JWkdoAHIrOkmlBiwpj1oG8'
					}
				};
			
				return fetch('https://api.themoviedb.org/3/movie/500?language=es-ES', options)
					.then(response => response.json())
					.then(response => {
						console.log("Respuesta de la API:", response);
						setStore({ movie: response });
						return response; 
					})
					.catch(err => {
						console.error(err);
						throw err;
					});
			},

			getMovieList: () => {
				console.log("Lista desde Flux");
				const options = {
					method: 'GET',
					headers: {
						accept: 'application/json',
						Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5M2ZhNzNkZjUyZTYyNWQ5NGQ1NzMyNGI1YTFlNDgzYSIsInN1YiI6IjY1OTQwNzAwY2U0ZGRjNmQzODdmMDIzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNQabtAWxQcVNGg9_oMH8JWkdoAHIrOkmlBiwpj1oG8'
					}
				};
				
				fetch('https://api.themoviedb.org/3/movie/top_rated?language=es-ES&page=1', options)
					.then(response => response.json())
					.then(data => {
						console.log(data)
						setStore({ results: data.results });
					})
					.catch(err => console.error(err));
			},

			


			getMessage: async () => {
				try{
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
