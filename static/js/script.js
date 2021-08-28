const btn = document.querySelector('form');


btn.addEventListener('submit', function(e){
    const inputs = document.querySelectorAll('input');
    const sent_block = document.querySelector('.wrapper');
    const comment = document.querySelector('textarea');
    if (comment.value[0] >= 'a' && 'z' <=  comment.value[0]) {
          comment.value = '';
        }
    let flag = true;
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
    }
    if (flag){
        sent_block.style.display = 'block';
    }
})

