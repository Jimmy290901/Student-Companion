var update_buttons = document.querySelectorAll('.update_task')
const close_modal = document.getElementById('close_modal')
const modal_container = document.getElementById('modal_container')

const task_desc = document.querySelector(".box_modal #id_task_desc");
task_desc.id = "update_task_desc_id";
const rem_d_and_t = document.querySelector(".box_modal #id_rem_d_and_t");
rem_d_and_t.id = "update_rem_id";

function fillUpdateDetails(desc, url, completed, rem) {
    
    task_desc.value = desc;
    console.log(task_desc.value);

    if (rem !== "None") {
        rem_d_and_t.value = rem;
    }
    else {
        rem_d_and_t.value = '';
        rem_d_and_t.placeholder = "Reminder";
    }
    console.log(rem_d_and_t.value);

    const checkbox = document.querySelector(".box_modal #id_completed");
    if (completed === 'True') {
        checkbox.checked = true;
    }
    else {
        checkbox.checked = false;
    }
    console.log(checkbox.checked);

    const updateForm = document.querySelector(".box_modal form");
    updateForm.action = url;
    console.log(updateForm);

    modal_container.classList.add('modal_show');
}


// update_buttons.forEach(item => {
//         item.addEventListener('click',(desc, url , completed, rem) => {
//         modal_container.classList.add('modal_show');
//     })
// });

close_modal.addEventListener('click', () => {
    modal_container.classList.remove('modal_show');
})