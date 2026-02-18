const todoForm = document.getElementById('todo-form');
const taskInput = document.getElementById('new-task');
const taskList = document.getElementById('task-list');

let tasks = loadTasks();

function renderTasks() {
  
  taskList.innerHTML = '';
  if (tasks.length === 0) {
    const emptyMsg = document.createElement('p');
    emptyMsg.className = 'empty-msg';
    emptyMsg.textContent = 'Нет задач — добавьте первую!';
    taskList.appendChild(emptyMsg);
    return;  
  }
  
  tasks.forEach((task) => {
    const li = document.createElement('li');

    li.className = task.done ? 'task-item done' : 'task-item';
    
    li.dataset.id = task.id;
    

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.done;  
    checkbox.setAttribute('aria-label', `Отметить "${task.text}" как выполненную`);

    checkbox.addEventListener('change', () => {
      toggleTask(task.id);  
    });
    

    const label = document.createElement('label');
    label.className = 'task-label';
    label.textContent = task.text; 
    
    label.addEventListener('click', () => {
      checkbox.checked = !checkbox.checked; 
      toggleTask(task.id);
    });
    
    
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.innerHTML = '🗑';  
    deleteBtn.setAttribute('aria-label', `Удалить задачу: ${task.text}`);
    
    deleteBtn.addEventListener('click', () => {
      deleteTask(task.id, li);  
    });
    
    
    li.appendChild(checkbox);
    li.appendChild(label);
    li.appendChild(deleteBtn);
    
    taskList.appendChild(li);
  });
}

function addTask(text) {

  const trimmedText = text.trim();
  
  if (!trimmedText) return;
  const newTask = {
    id: Date.now(),      
    text: trimmedText,
    done: false         
  };

  tasks.push(newTask);

  saveTasks();
  
  renderTasks();
}


function toggleTask(id) {
  
  tasks = tasks.map((task) =>
    task.id === id 
      ? { ...task, done: !task.done }  
      : task                           
  );

  
  saveTasks();
  renderTasks();
}


function deleteTask(id, listItem) {
  
  listItem.classList.add('removing');

  listItem.addEventListener('transitionend', () => {
    
    tasks = tasks.filter((task) => task.id !== id);
    
    saveTasks();
    renderTasks();
    
  }, { once: true }); 
}


function saveTasks() {
  localStorage.setItem('todo-tasks', JSON.stringify(tasks));
}



function loadTasks() {
  const stored = localStorage.getItem('todo-tasks');
  
  return stored ? JSON.parse(stored) : [];
  
}




todoForm.addEventListener('submit', (event) => {
  
  event.preventDefault();
  addTask(taskInput.value);

  taskInput.value = '';
  
  taskInput.focus();
});


renderTasks();
