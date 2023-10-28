document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.getElementById('searchBar');
    const items = document.querySelectorAll('.item');
    const deleteButtons = document.querySelectorAll('.delete-button');

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

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const item = button.closest('.item');
            if (item) {
                item.remove();
            }
        });
    });

    $(document).on('click', '.card-link', function() {
        const bookId = $(this).data('book-id');
        const title = $(this).data('title');
        const author = $(this).data('author');
        const year = $(this).data('year');
        const genre = $(this).data('genre');
        const pages = $(this).data('pages');
        const description = $(this).data('description');
        const thumbnail = $(this).data('thumbnail');
        const ratings_avg = $(this).data('ratings_avg');
        const ratings_count = $(this).data('ratings_count');
        const isbn10 = $(this).data('isbn10');
        const isbn13 = $(this).data('isbn13');
        const source = $(this).data('source');

        // Now populate the modal with these values
        $("#modalBookTitle").text(title);
        $('#modalBookThumbnail').attr('src', thumbnail);
        $("#modalBookGenreYear").text(genre + " | " + year);
        $("#modalBookAuthor").text(author);
        $("#modalBookPages").text(pages);
        $("#modalBookDescription").text(description);
        $("#modalBookAvgRate").text(ratings_avg);
        $("#modalBookCountRate").text(ratings_count);
        $("#modalBookIsbn10").text(isbn10);
        $("#modalBookIsbn13").text(isbn13);
        
        // Buttons
        $('#buyOnAmazonButton').attr('href', `https://www.amazon.com/s?k=${isbn13}`);
        $('#borrowReadButton').data('book-id', bookId);

        // Check the source and adjust the button text
        if(source === 'library') {
            $('#borrowReadButton').text('Read');
            $('#borrowReadButton').attr('class', 'btn btn-primary');
        } else if(source === 'bookshelf') {
            $('#borrowReadButton').attr('class', 'btn btn-success');
            $('#borrowReadButton').text('Complete Reading');
        }

        // Finally, display the modal
        $("#bookDetailsModal").modal('show');
        $(document).on('click', '#borrowReadButton', function(event) {
            event.preventDefault();
            let bookId = $(this).data('book-id');
            $.ajax({
                url: '/booklibrary/borrow-book/', 
                method: 'POST',
                data: {
                    'book_id': bookId,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(response) {
                    if (response.status === 'success') {
                        showNotification();
                        $('#bookDetailsModal').modal('hide');
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function() {
                    alert('An error occurred. Please try again.');
                }
            });
    
            function showNotification() {
                $('#notification').show().delay(5000).fadeOut(); 
            }
        });
    });
});
