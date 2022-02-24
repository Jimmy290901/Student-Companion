const close_modal = document.getElementById('close_modal')
const modal_container = document.getElementById('modal_container')

const task_desc = document.querySelector(".box_modal #id_task_desc");
const rem_d_and_t = document.querySelector(".box_modal #id_rem_d_and_t");

function fillUpdateDetails(desc, url, completed, rem) {
    
    task_desc.value = desc;

    if (rem !== "None") {
        rem_d_and_t.value = rem;
    }
    else {
        rem_d_and_t.value = '';
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

close_modal.addEventListener('click', () => {
    modal_container.classList.remove('modal_show');
});

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}

$(".fa-plus-circle").on("click", () => {
    $(".todo_form").slideToggle(500);
});

$(".submit-update-form").on("click", () => {
    $(".update-form").submit();
});