const btn = document.querySelector('form');
const add_btn = document.querySelector('#add');
const data = {};
let formForNewUser = '';

btn.addEventListener('submit', function(e){
    let sent_block = document.querySelector('.wrapper');
     let flag = true;

    const forms = document.querySelectorAll('form');

    forms.forEach(function(item, i){

        let inputs = document.querySelectorAll('input');
        let comment = document.querySelector('textarea');
        if (comment.value[0] >= 'a' && 'z' <=  comment.value[0]) {
              comment.value = '';
            }
        for (let input of inputs){
            // проверка на язык
            if ((input.value[0] >= 'a' && 'z' <=  input.value[0]) ||
                (comment.value[0] >= 'a' && 'z' <=  comment.value[0])) {
                flag = false;
                e.preventDefault();
                const warn_text = document.querySelector('#warn_lang');
                warn_text.style.display = 'block';
            }
            // проверка на пустое поле
            if (input.value === '' || comment.value === ''){
                flag = false;
                e.preventDefault();
                const warn_empt = document.querySelector('#warn_empty');
                warn_empt.style.display = 'block';
            }
            if (input.value[0] != input.value[0].toUpperCase()){
                flag = false;
                e.preventDefault();
            }
        }

        if (flag){
        sent_block.style.display = 'block';
        }


        let formData = new FormData(item);
        let object = {};
            formData.forEach(function(value, key){
                object[key] = value;
            });
        data[i] = object;
    })
    postData(JSON.stringify(data));
})

add_btn.addEventListener('click', function(e){
    e.preventDefault();
    let new_form = document.createElement('div');

    const requestHTML = new XMLHttpRequest();
            requestHTML.open('GET', '/getHTML');
            requestHTML.send();

    requestHTML.addEventListener('load', function(){
        if (requestHTML.status === 200){
            console.log(typeof(requestHTML.responseText));
            formForNewUser = requestHTML.responseText;
            new_form.innerHTML += formForNewUser;
            document.querySelector('body').append(new_form);
        }
    })

})


function delete_user(btn){
    btn.parentElement.parentElement.style.display = 'none';
}


function postData(json){
    const request = new XMLHttpRequest();
            request.open('POST', '/postData');
            request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
            request.send(json);
}





