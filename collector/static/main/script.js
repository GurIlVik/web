// очистка поля с коллекциями
function find_cat(my_obj) {
    let catalog = document.getElementById('list_global') //.innerHTML
    let letter = my_obj.value
    for (let item of catalog.children) {
        if (item.innerHTML.includes(letter)) {
            item.style.display = 'inline';
        } else { item.style.display = 'None';
         }
    }}
    
// Открывашка окна скрипта
function menuPoint2() {
    let blok2 = document.getElementById('alternative_global_2').style.zIndex = '10';
}

// проверка на дублирование во втором меню
function control_word (list_object, object) {
    let lis_ob_li = list_object.length;
    key = false;
    for (let i = 0; i <= lis_ob_li; i +=1) {
        if (list_object[i] == object) {
            key = true;
            return key
        } 
    }
    return key
}

// разрисовывание функции объектов
function menuPoint20(object) {
    console.log(object.id);
    let list_object = [];
    let value_list = document.getElementsByClassName("Child_main_menu2")
    for (let item of value_list) {
        list_object.push(item.textContent)
        }
    console.log(list_object);
    key = control_word (list_object, object.id)
    if (key == false) {
        let div_object = document.getElementById('plusPredmet');
        let div_object2 = document.getElementById('q1');
        div_object2.style.zIndex = '-1000'
        div_object.innerHTML += `<p><span>&ensp;&ensp;</span><span class="Child_main_menu2">${object.id}</span><span>,</span></p> `
        div_object2.innerText += '${object.id}'
        list_object.push(object.id)
        console.log(list_object);
        let object_id2 = object.id + ', '
        console.log('value kukuk156', object.id);
        div_object2.value += object_id2;
        console.log(list_object);
        // find_cat('')
    } 
}

// сброс выбранных параметров во 2 меню
function menuPoint25() {
    let value_list = document.getElementById('plusPredmet');
    value_list.innerHTML = `<p>Предмет коллекционирования:</p>`
    console.log(value_list.innerText)
    let div_object2 = document.getElementById('q1');
    div_object2.value = ''
    div_object2.style.zIndex = '-10'
    console.log(div_object2.value);
}

// ввод меню для добавления элемента
function menuPoint23() {
    menuPoint2();
    let catalog = document.getElementById('list_global');
    catalog.style.display = 'flex'
    catalog.style.flexDirection = 'row';
    catalog.style.alignContent = 'space-around';
    for (let item of catalog.children) {
        item.style.display = 'flex'
        }
}

// функция отображения по интересу пользователя.
function menuPoint3(as) {
    console.log('value_list4')
    let value_list4 = document.getElementsByClassName("info_blok_grid_main");
    let value_list3 = document.getElementsByClassName("display_none");
    let value_list2 = document.getElementsByClassName("display_none2");
    console.log(as)
    console.log(value_list3)
    for (var i = value_list3.length - 1; i >= 0; i--) {
        let a = value_list3[i].innerHTML.trim();
        let b = value_list2[i].innerHTML.trim();
        console.log(a)
        console.log('ntgthm ,')
        console.log(b)
        if (a == 2 && as == 5 || as == 1 && as == b || as == 2 && as == b || as ==3 && as == b) {
            value_list4[i].style.display = "grid";
        } else {
            value_list4[i].style.display = "none";
            }
        }
    }


// функция комментирования комментатора
function comment_for_comment(i) {
    console.log(12);
    let field_comm_comment = document.getElementById(i);
    field_comm_comment.style.display = 'inline';
    console.log(i);
    let string = 'comment2_id_i_'+i;
    console.log(string);
    let p_id_articl = document.getElementById(string);
    p_id_articl.value = i;
    console.log(p_id_articl);
}

function comment_for_comment2(i, author) {
    console.log(12);
    console.log(i);
    console.log(author);
    let string = 'comm_comm_' + i
    console.log(string)
    let field_comm_comment = document.getElementById(string);
    field_comm_comment.style.display = 'inline';
    console.log(field_comm_comment);
    string = 'comment2_id_i_' + i;
    let field_comm_comment2 = document.getElementById(string);
    field_comm_comment2.value= i;
    string = 'author_comment_' + i;
    let field_comm_comment3 = document.getElementById(string);
    field_comm_comment3.value= author;
    console.log(12);
    console.log(field_comm_comment2.value);
    console.log(field_comm_comment3.value);
}

function fun_foto(param) {
    console.log(param);
    let block = param;
    console.log(param.src);
    let block2 = document.getElementById('info_blok_90');
    console.log(block2);
    block2.style.display = 'block';
    block2.innerHTML = '';
    let block3 = document.getElementById('info_blok_91');
    block3.style.display = 'block';
    console.log('lwrjbhglkwrjtbgwlrijb');
    console.log(param.src);
    let block5 = document.createElement('img');
    block5['src'] = param.src;
    block2.appendChild(block5);
    console.log(block2)
}

function clouse_photo() {
    let block2 = document.getElementById('info_blok_90');
    let block3 = document.getElementById('info_blok_91');
    block2.style.display = 'none';
    block3.style.display = 'none';
}

document.addEventListener('click', (e) => { // Вешаем обработчик на весь документ
    let popupBg = document.getElementById('info_blok_91');
    let popupBg2 = document.getElementsByClassName('img_for_arts')
    console.log(e.target)
    let count = 0
    let string = ''
    for (let item of popupBg2) {
        if (e.target == item) { count = 1; string = item}
    }
    if (count != 0) {   
        console.log(count);
        console.log(string);
        console.log(popupBg) 
    } else { clouse_photo(); }
    }
    )

function countsInt(symbol, number, key) {
    let string = 'form_count_' + key;
    let popupBg = document.getElementById(string);
    popupBg.style.display = 'block';
    string = 'count_text_1_' + key;
    console.log(string)
    let popupInput = document.getElementById(string);
    popupInput.value = symbol + '&' + key;
    console.log(popupInput.value)
}

function holl(key, strin){
    let string = strin + key;
    let popupBg = document.getElementById(string);
    popupBg.style.display = 'block';
}

function write_autor(symbol, key) {
    let string = 'id_write_' + key;
    let popupBg = document.getElementById(string);
    popupBg.style.display = 'block';
    string = 'write_id_' + key;
    let popupBg2 = document.getElementById(string);
    popupBg2.value = key
}