let categoryContent = 'category-content'
let categoryContentHidden = 'category-content--hidden'
let card = "card"
let cardSelected = "card--selected"
let cardContent = "card-content"
let cardContentHidden = "card-content--hidden"

function toggleCard($card) {
    let $content = $card.next()

    // Make sure card category is visible
    $card.parent().removeClass(categoryContentHidden).addClass(categoryContent)

    // Hide all visible card-content and deselect cards
    $(".card-content").removeClass(cardContent).addClass(cardContentHidden)
    $(".card--selected").removeClass(cardSelected).addClass(card)

    // Select Card and show Content
    $card.removeClass(card).addClass(cardSelected)
    $content.removeClass(cardContentHidden).addClass(cardContent)

    // Go to card
    $(window).scrollTop($card.offset().top)
    // Go to card after load position change
    setTimeout(function () {
        $(window).scrollTop($card.offset().top)
    }, 1)
}

function removeHash () {
    var scrollV, scrollH, loc = window.location;
    if ("pushState" in history)
        history.pushState("", document.title, loc.pathname + loc.search);
    else {
        // Prevent scrolling by storing the page's current scroll offset
        scrollV = document.body.scrollTop;
        scrollH = document.body.scrollLeft;

        loc.hash = "";

        // Restore the scroll offset, should be flicker free
        document.body.scrollTop = scrollV;
        document.body.scrollLeft = scrollH;
    }
}

function updateHash($card) {
    if (window.location.hash !== "#" + $card.attr("id")) {
        window.location.hash = "#" + $card.attr("id")
    } else {
        removeHash()
    }
}

function leftArrowPressed() {
    let $selectedCard = $(".card--selected")
    if ($selectedCard.length > 0) {
        // With a card selected
        let $previousCard = $selectedCard.prev().prev()
        if ($previousCard.length > 0) {
            // With a card before
            updateHash($previousCard)
        } else {
            // Without a card before
            let $previousCategory = $selectedCard.parent().prev().prev()
            if ($previousCategory.length > 0) {
                // Go to last card in previous category
                updateHash($previousCategory.children(".card").last())
            }
        }
    } else {
        // Go to first card
        updateHash($(".card").first())
    }
}

function rightArrowPressed() {
    let $selectedCard = $(".card--selected")
    if ($selectedCard.length > 0) {
        // With a card selected
        let $nextCard = $selectedCard.next().next()
        if ($nextCard.length > 0) {
            // With a card after
            updateHash($nextCard)
        } else {
            // Without a card after
            let $nextCategory = $selectedCard.parent().next().next()
            if ($nextCategory.length > 0) {
                // Go to first card in next category
                updateHash($nextCategory.children(".card").first())
            }
        }
    } else {
        // Without a card selected
        updateHash($(".card").first())
    }
}

$(window).on('hashchange', function () {
    // Toggle card when hash is changed
    if (window.location.hash) {
        toggleCard($(window.location.hash))
    }
})

$(window).on('load', function () {
    // Toggle card on load or reload of page
    if (window.location.hash) {
        toggleCard($(window.location.hash))
    }
})

$(document).ready(function () {
    $(".category").click(function () {
        let $content = $(this).next()
        if ($content.hasClass(categoryContent)) {
            // Hide category content
            $content.removeClass(categoryContent).addClass(categoryContentHidden)
        } else {
            // Reveal category content and hide card content
            $content.removeClass(categoryContentHidden).addClass(categoryContent)
            $content.children(".card-content").removeClass(cardContent).addClass(cardContentHidden)
        }
    });


    $(".card").click(function () {
        // Hide all visible card-content and deselect cards before updateHash()
        $(".card-content").removeClass(cardContent).addClass(cardContentHidden)
        $(".card--selected").removeClass(cardSelected).addClass(card)
        updateHash($(this))
    });

    $(".card--selected").click(function () {
        // Hide all visible card-content and deselect cards before updateHash()
        $(".card-content").removeClass(cardContent).addClass(cardContentHidden)
        $(".card--selected").removeClass(cardSelected).addClass(card)
        updateHash($(this))
    })

    $("html").keydown(function (e) {
        if (e.keyCode === 37) {
            leftArrowPressed()
        } else if (e.keyCode === 39) {
            rightArrowPressed()
        }
    })
});

