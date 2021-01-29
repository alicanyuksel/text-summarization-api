let config;

if (process.env.NODE_ENV === "production") {
  config = {
    $api_url: "",
  };
} else {
  config = {
    $api_url: "http://localhost:5000/summary"
  };
}

export { config }