console.log("Script Connected")

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('plus-btn').forEach((button) => {
        button.addEventListener('click', () => {
            let productId = this.getAttribute('data-id')
            updatequantity(productId, 'plus')

            console.log(productId, "Clicked")
        })
    })

    document.querySelectorAll('minus-btn').forEach((button) => {
        button.addEventListener('click', ()=> {
            let productId = this.getAttribute('data-id')
            updatequantity(productId, 'minus')
        })
    })

    function updatequantity(productId, action){
        let xhr = new XMLHttpRequest()
        xhr.open('POST', '{% url "update_quantity" %}', true)
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}')
        xhr.onreadystatechange = function(){
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
                let response = JSON.parse(xhr.responseText)
                document.getElementById('quantity-' + productId).textContent = response.new_quantity;
            }
        }
        xhr.send("product_id = " + productId + '&action' + action)
    }
})