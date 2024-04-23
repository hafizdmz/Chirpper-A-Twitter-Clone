function get_data() {
    //GET TWEET FROM BACKEND
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/api/total_tweets"; //ganti nama file sesuai nama file json kalian
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        let tweets = JSON.parse(this.response);
        let no = 1;
        tweets["data"].forEach((item) => {
          const elTbody = document.getElementById("tbody");
          console.log(item);
          const elTr = document.createElement("tr");
          const elTh = document.createElement("th");
          const elTd_1 = document.createElement("td");
          const elTd_2 = document.createElement("td");
  
          elTd_1.innerHTML = item.username;
          elTd_2.innerHTML = item.total_tweet;
          elTh.innerHTML = no;
          elTr.append(elTh, elTd_1, elTd_2);
          elTbody.append(elTr);
          no += 1;
        });
      }
    };
    xhr.open("GET", url, true);
    xhr.send();
  }
  
  window.onload = function () {
    // cek apakah access_token &
    get_data();
  };
  