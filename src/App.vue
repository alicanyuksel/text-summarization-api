<template>
	<section>
		<header><h1>Text Summarization</h1></header>

		<div id="inputText">
			<ul>
				<li>
					<h2>Input Text</h2>
					<ul>
						<textarea
							v-model="inputText"
							id="text"
							name="text_name"
							rows="15"
							cols="70"
						/>
					</ul>
					<button @click="sendToSummerizer">Summarize</button>
				</li>
			</ul>

			<ul v-if="isRequestSended">
				<li>
					<h2>Summary</h2>
					<div class="loader" v-if="loading"></div>
					<p>{{ summaryText }}</p>
				</li>
			</ul>
		</div>
	</section>
</template>


<script>
import axios from "axios";
import { config } from "./config.js";

export default {
	data() {
		return {
			inputText: "",
			summaryText: "",
			loading: false,
			isRequestSended: false,
		};
	},
	watch: {
		summaryText(value) {
			if (value.length > 0) {
				this.loading = false;
			}
		},
  },
	methods: {
		sendToSummerizer() {
      this.isRequestSended = true;
      this.loading = !this.loading;
      this.summaryText = "";
      
			var inputJson = {
				text: this.inputText,
			};

			axios
				.post(config.$api_url, inputJson)
				.then((response) => (this.summaryText = response.data.summary_text));
		},
	},
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Jost&display=swap");

* {
	box-sizing: border-box;
}

html {
	font-family: "Jost", sans-serif;
}

body {
	margin: 0;
}

header {
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
	margin: 3rem auto;
	border-radius: 10px;
	padding: 1rem;
	background-color: #58004d;
	color: white;
	text-align: center;
	width: 90%;
	max-width: 40rem;
}

#app ul {
	margin: 0;
	padding: 0;
	list-style: none;
}

#app li {
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
	margin: 1rem auto;
	border-radius: 10px;
	padding: 1rem;
	text-align: center;
	width: 100%;
	max-width: 40rem;
}

#app h2 {
	font-size: 2rem;
	border-bottom: 4px solid #ccc;
	color: #58004d;
	margin: 0 0 1rem 0;
}

#app button {
	font: inherit;
	cursor: pointer;
	border: 1px solid #ff0077;
	background-color: #ff0077;
	color: white;
	padding: 0.05rem 1rem;
	box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.26);
}

#app button:hover,
#app button:active {
	background-color: #ec3169;
	border-color: #ec3169;
	box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.26);
}

.loader {
	margin: auto;
	border: 16px solid #f3f3f3; /* Light grey */
	border-top: 16px solid #3498db; /* Blue */
	border-radius: 50%;
	width: 80px;
	height: 80px;
	animation: spin 2s linear infinite;
}

@keyframes spin {
	0% {
		transform: rotate(0deg);
	}
	100% {
		transform: rotate(360deg);
	}
}
</style>