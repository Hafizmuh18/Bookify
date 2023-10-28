document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.getElementById('searchBar');
    const items = document.querySelectorAll('.item');

    searchBar.addEventListener('input', function() {
        const searchQuery = searchBar.value.toLowerCase();

        items.forEach(item => {
            const title = item.querySelector('#title').textContent.toLowerCase();

            if (title.includes(searchQuery)) {
                item.style.display = 'block'; 
            } else {
                item.style.display = 'none'; 
            }
        });
    });

    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = button.closest('.item');
            const bookId = card.getAttribute('data-book-id');

            // Kirim permintaan AJAX ke server untuk menghapus bookmark berdasarkan bookId
            fetch('/delete-bookmark/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // Pastikan CSRF token disertakan dalam permintaan
                },
                body: JSON.stringify({ bookmark_id: bookId })
            })
            .then(response => {
                if (response.status === 200) {
                    card.remove(); // Hapus elemen card jika penghapusan bookmark berhasil
                } else {
                    console.log('Gagal menghapus bookmark.');
                }
            })
            .catch(error => {
                console.error(error);
            });
        });
    });

    // Fungsi untuk mendapatkan CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
