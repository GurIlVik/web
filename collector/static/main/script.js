function find_cat(my_obj) {
    let catalog = document.getElementById('list_global') //.innerHTML
    let letter = my_obj.value
    for (let item of catalog.children) {
        if (item.innerHTML.includes(letter)) {
            item.style.display = 'inline';
        } else { item.style.display = 'None';
         }
    }}
    

function menuPoint2() {
    let blok2 = document.getElementById('alternative_global_2').style.zIndex = '10';
}

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
        let div_object2 = document.getElementById('plusPredmet');
        let div_object = document.getElementById('q1');
        console.log('value kukuk156', object.id);
        div_object.value += object.id;
        list_object.push(object.id)
        console.log(list_object);
        find_cat('')

    } 
}

function menuPoint23() {
    console.log('efvevf');
    let blok2 = document.getElementById('alternative_global_2').style.zIndex = '10';
    console.log('efvevf');
    // console.log(object.id);
    let list_object = [];
    let value_list = document.getElementsByClassName("Child_main_menu2")
    for (let item of value_list) {
        list_object.push(item.textContent)
        }
    console.log(list_object);
    key = control_word (list_object, object.id)
    if (key == false) {
        let div_object2 = document.getElementById('plusPredmet');
        let div_object = document.getElementById('q1');
        console.log('value kukuk156', object.id);
        div_object.value += object.id;
        list_object.push(object.id)
        console.log(list_object);
        find_cat('')

    } 
}
    // let catalog = document.getElementById('list_global');
    // catalog.style.display = 'flex'
    // catalog.style.flexDirection = 'row';
    // catalog.style.alignContent = 'space-around';
    // for (let item of catalog.children) {
    //     item.style.display = 'flex'
    //     }








// function menuPoint20(object) {
//     // let catalog = document.getElementById('list_global')
//     // let list_global = []
//     // for (elem of catalog.children) {
//     //     list_global.push(elem.innerHTML);

//     // }

//     console.log(object.id);
//     let list_object = [];
//     let value_list = document.getElementsByClassName("Child_main_menu2")
//     for (let item of value_list) {
//         list_object.push(item.textContent)
//         }
//     console.log(list_object);
//     key = control_word (list_object, object.id)
//     if (key == false) {
//         let div_object = document.getElementById('plusPredmet');
//         let div_object2 = document.getElementById('q1');
//         // let div_object = document.getElementById('q1');
//         div_object.innerHTML += `<p><span>&ensp;&ensp;</span><span class="Child_main_menu2">${object.id}</span><span>,</span></p> `
//         // div_object2.innerText += '${object.id}'
//         list_object.push(object.id)
//         div_object2.pole = object.id

//         console.log(list_object);

//         find_cat('')
//     } 
// }