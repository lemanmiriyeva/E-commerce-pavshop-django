function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken);
const addProduct = {
    addToWishlist(ProductID) {
        return fetch('http://localhost:8000/en/api/wishlist/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                // 'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}
const addCart = {
    addProductCart(ProductID, Quantity) {
        return fetch('http://localhost:8000/en/api/basket/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                // 'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product':ProductID,
                'quantity':Quantity
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}
const deleteProduct = {
    deleteFromWishlist(ProductID) {
        return fetch('http://localhost:8000/en/api/wishlist/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                // 'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}
const deleteBasket = {
    deleteProductBasket(ProductID) {
        return fetch('http://localhost:8000/en/api/basket/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                // 'Authorization': `Bearer ${localStorage.getItem('user-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}
function functionAddToWishlist(ProductID) {
    addProduct.addToWishlist(ProductID);
}
function AddToBasket(ProductID) {
    const quantity = 1;
    addCart.addProductCart(ProductID, quantity);
    deleteProduct.deleteFromWishlist(ProductID);
}
function AddToBasketinDetail(ProductID) {
    const quantity = parseInt(document.getElementById('detail-qty').value);
    addCart.addProductCart(ProductID, quantity);
    deleteProduct.deleteFromWishlist(ProductID);
}
function removeWishlist(ProductID) {
    deleteProduct.deleteFromWishlist(ProductID)
}
function removeBasket(ProductID) {
    deleteBasket.deleteProductBasket(ProductID)
}
const subscribe_form = document.getElementById('mc-embedded-subscribe-form')
subscribe_form.addEventListener('submit', function (event) {
    let e_mail = document.getElementById('mce-EMAIL')
    console.log(e_mail);
    console.log(e_mail.value);
    const data = {
        email: e_mail.value
    };
    fetch('http://localhost:8000/en/api/subscribe/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (response.ok){
               alert('Successfully registered !')
            } else {
                alert('Error')
            }
        })
        .then((data) => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});