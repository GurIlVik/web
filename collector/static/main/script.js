function find_cat(my_obj) {
    let catalog = document.getElementById('list_global') //.innerHTML
    //for (let i of catalog) {
    //    console.log(i)
    //}
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
    // let catalog = document.getElementById('list_global')
    // let list_global = []
    // for (elem of catalog.children) {
    //     list_global.push(elem.innerHTML);

    // }

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
        div_object.innerHTML += `<p><span>&ensp;&ensp;</span><span class="Child_main_menu2">${object.id}</span><span>,</span></p> `
        list_object.push(object.id)
        console.log(list_object);
        find_cat('')

    } 
}

function menuPoint23() {
    let catalog = document.getElementById('list_global')
    for (let item of catalog.children) {
        item.style.display = 'inline'
        }
}