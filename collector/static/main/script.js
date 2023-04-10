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
        console.log(list_object[i]);
        console.log(typeof(list_object[i]));
        console.log(object);
        console.log(typeof(object));
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
    let value_list4 = document.getElementsByClassName("info_blok_1");
    let value_list3 = document.getElementsByClassName("display_none");
    for (var i = value_list3.length - 1; i >= 0; i--) {
        let a = value_list3[i].innerHTML.trim();
        let b = value_list4[i];
        if (a == as) {
            value_list4[i].style.display = "flex";
        } else {
            value_list4[i].style.display = "none";
        }
    }
}




// function Comment_authentic_comment_not_register() {
//     let modal_not_register = document.getElementById('modal_not_register_id');
//     console.log(modal_not_register)
//     modal_not_register.style.display = "inline";
//     console.log('3')
// }

// function close_modal_not_register() {
//     let modal_not_register = document.getElementById('modal_not_register_id');
//     modal_not_register.style.display = "none";
// }

// window.onclick = function(event) {
//     let button_not_register = document.getElementById('not_register');
//     let modal_not_register = document.getElementById ('modal_not_register_id');
//     let modal_not_register1 = document.getElementById ('modal_not_register_id2');
//     let modal_not_register2 = document.getElementById ('modal_not_register_id3');
//     let modal_not_register3 = document.getElementById ('modal_not_register_id3');
//     if (event.target != button_not_register) {
//         if (event.target != modal_not_register 
//             && event.target != modal_not_register1 
//             && event.target != modal_not_register2
//             && event.target != modal_not_register3
//             ) {
//             close_modal_not_register()
//         }
//     } else {
//         console.log('6')
//     }
// }

function comment_for_comment(i) {
    console.log(i)
    console.log(typeof(i))
    console.log('perjnvepirgjbn')
    // let field = document.getElementsByClassName('info_blok_7').innerHTML;
    // let field = document.getElementsByClassName('info_blok_7').textContent;
    // let field = document.getElementsByClassName('info_blok_7')

    let field_comm_comment = document.getElementById(i)
    
    field_comm_comment.style.display = 'inline'
    console.log(field_comm_comment)

    for (var j = field.length - 1; j>=0; j-=1) {
            console.log(field[j].innerHTML)
            console.log(field[j].value)
        }
    // let f = document.querySelectorAll('info_blok_7');
    // for (var j = f.length -1; i>=0; i--) {
    //     console.log(f[j])
    // }
    
    // let f = document.getElementsByClassName('info_blok_73')
    // f.style.display = 'inline';
    // let field_input = document.getElementById('comment2_id');
    // let field_p = document.getElementById('comment2_id_p');
    // let a = field_p.textContent;
    // console.log(a);
}


// <button class='fd2' id='not_register' onclick="Comment_authentic_comment_not_register()">Комментировать</button>
// <div class= 'modal_not_register_class' id='modal_not_register_id'>
//     <div class= 'modal_not_register_contetnt_class'>
//         <button class='close_modal_not_register' onclick='close_modal_not_register()'>&times;</button>
//         <p class='close_modal_not_register2'>Вы не прошли регистрацию</p>
//         <a class='close_modal_not_register2' href="/"><button class='fd2'>Регистрация/ВХОД</button></a></div>
//     </div>
