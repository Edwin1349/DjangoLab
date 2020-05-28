var list_items = [];

const list_element = document.getElementById('list');
const pagination_element = document.getElementById('pagination');

let current_page = 1;
let rows = 6;

function DisplayList (items, wrapper, rows_per_page, page) {
	wrapper.innerHTML = "";
	page--;

	let start = rows_per_page * page;
	let end = start + rows_per_page;
	let paginatedItems = items.slice(start, end);

	for (let i = 0; i < paginatedItems.length; i++) {
        let item = paginatedItems[i];
        
        //console.log(item.id_seance[0]);

        let item_element = document.createElement('div');
        item_element.classList.add('item');
		item_element.className = "performance_block";
        item_element.id = item.id_seance[0];
		item_element.innerHTML = document.getElementById('blockOfStuff').innerHTML;
		item_element.querySelector(".url").id = item.id_seance[0];
		item_element.querySelector(".url").href = item.id_seance[0];
        item_element.querySelector(".author").innerHTML = item.director[0];
        item_element.querySelector(".performance_name").innerHTML = item.performance_name[0];
        item_element.querySelector(".time").innerHTML = "початок о " + item.time[0];
        item_element.querySelector(".day_name").innerHTML = new Date(item.date[0]).toLocaleDateString('en-US', { weekday: 'long' });
        item_element.querySelector(".day_num").innerHTML = new Date(item.date[0]).toLocaleDateString('en-US', { day: 'numeric' });
        item_element.querySelector(".month_name").innerHTML = new Date(item.date[0]).toLocaleDateString('en-US', { month: 'long' });
    
        wrapper.appendChild(item_element);

	}
}

function SetupPagination (items, wrapper, rows_per_page) {
	wrapper.innerHTML = "";

	let page_count = Math.ceil(items.length / rows_per_page);
	for (let i = 1; i < page_count + 1; i++) {
		let btn = PaginationButton(i, items);
		wrapper.appendChild(btn);
	}
}

function PaginationButton (page, items) {
	let button = document.createElement('button');
	button.innerText = page;

	if (current_page == page) button.classList.add('active');

	button.addEventListener('click', function () {
		current_page = page;
		DisplayList(items, list_element, rows, current_page);

		let current_btn = document.querySelector('.pagenumbers button.active');
		current_btn.classList.remove('active');

		button.classList.add('active');
	});

	return button;
}

function Request() {
		let xhr = new XMLHttpRequest();
		var cmp = document.getElementById("name").value;
		console.log(cmp);
		xhr.open('POST', 'getEvents/');
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr.responseType = 'json';
		xhr.send("cmp="+cmp);
		xhr.onload = function() {
			list_items  = xhr.response;
			console.log(list_items);
			DisplayList(list_items, list_element, rows, current_page);
			SetupPagination(list_items, pagination_element, rows);
			
		};
}

document.getElementById("search_button").onclick = Request;
   



