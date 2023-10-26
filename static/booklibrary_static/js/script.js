// CSRF PROTECTION
$.ajaxSetup({
    headers: { "X-CSRFToken": $('input[name=csrfmiddlewaretoken]').val() }
});

// LIBRARY TAB
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
    // Finally, display the modal
    $("#bookDetailsModal").modal('show');
});

// BOOKSHELF TAB
$(document).ready(function() {
    $("#bookshelfLink").click(function(event) {
        event.preventDefault();
        $("#library").hide();
        $.ajax({
        url: '/booklibrary/get-user-bookshelf/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            var content = '';
            $.each(data, function(index, book) {
                content += `
                    <a href="#" class="card-link">
                        <div class="card item">
                            <img src="${book.thumbnail}" class="card-img-top" alt="a book">
                            <div class="card-body">
                                <h5 class="card-title">${book.title}</h5>
                                <p class="card-text">Status: ${book.status}</p>
                            </div>
                            <ul class="list-group list-group-flush" style="border: 1px solid blue; height:auto;">
                                <li class="list-group-item">${book.genre}</li>
                                <li class="list-group-item">Rating: ${book.ratings_avg}/5</li>
                                <li class="list-group-item">Rating Counts: ${book.ratings_count}</li>
                            </ul>
                        </div>
                    </a>`;
            });
            $("#bookshelf").html(content).show();
        },
        error: function(error) {
            console.error("Error fetching bookshelf:", error);
        }
    });
    });

    $("#libraryLink").click(function(event) {
        event.preventDefault();
        $("#bookshelf").hide();
        $("#library").show();
    });
});

// BORROW/READ FEATURE
// function loadUserBookshelf() {
//     $.ajax({
//         url: '/booklibrary/get-user-bookshelf/',
//         method: 'GET',
//         success: function(data) {
//             $('#bookshelf').empty();
//             $.each(data, function(index, book) {
//                 content += `
//                     <a href="#" class="card-link">
//                         <div class="card item">
//                             <img src="${book.thumbnail}" class="card-img-top" alt="a book">
//                             <div class="card-body">
//                                 <h5 class="card-title">${book.title}</h5>
//                                 <p class="card-text">Status: ${book.status}</p>
//                             </div>
//                             <ul class="list-group list-group-flush" style="border: 1px solid blue; height:auto;">
//                                 <li class="list-group-item">${book.genre}</li>
//                                 <li class="list-group-item">Rating: ${book.ratings_avg}/5</li>
//                                 <li class="list-group-item">Rating Counts: ${book.ratings_count}</li>
//                             </ul>
//                         </div>
//                     </a>`;
//             });
//         },
//         error: function() {
//             alert('Failed to load bookshelf. Please try again.');
//         }
//     });
// }

// $(document).on('click', '#borrowReadButton', function(event) {
//     event.preventDefault();
//     let bookId = $(this).data('book-id');
//     $.ajax({
//         url: '/booklibrary/borrow-book/', // Update the URL based on your Django URL structure
//         method: 'POST',
//         data: {
//             'book_id': bookId,
//             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 $('#bookDetailsModal').modal('hide');
//                 alert('Book added to your shelf successfully!');

//                 // Optional: Reload the bookshelf tab or use AJAX to dynamically update it
//                 // loadUserBookshelf(); 
//             } else {
//                 alert('Error: ' + response.message);
//             }
//         },
//         error: function() {
//             alert('An error occurred. Please try again.');
//         }
//     });
// });
