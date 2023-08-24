document.addEventListener('DOMContentLoaded', function() {
    var readMoreDivs = document.querySelectorAll('.read-more');

    readMoreDivs.forEach(function(readMoreDiv) {
        readMoreDiv.addEventListener('click', function() {
            var personContainer = this.closest('.person-container');
            var shortInfo = personContainer.querySelector('.person-info-short');
            var fullInfo = personContainer.querySelector('.person-info');

            if (shortInfo.style.display === 'none') {
                shortInfo.style.display = 'block';
                fullInfo.style.display = 'none';
                this.textContent = 'read more';
            } else {
                shortInfo.style.display = 'none';
                fullInfo.style.display = 'block';
                this.textContent = 'read less';
            }
        });
    });
});
