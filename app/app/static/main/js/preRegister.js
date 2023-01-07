const dropDownLang = $(".lang-dropdown");
const langBtn = $(".lang-btn");
langBtn.click(() => {
  dropDownLang.toggleClass("hidden");
});

let langIcon = $(".lang-btn img");
const currentLang = location.pathname.substring(0, 3).replaceAll("/", "");

langIcon.attr("src", langIcon.attr("src").replace("az", currentLang));

$(function changelang() {
  $(".language a").click(function (e) {
    const selectedLanguage = $(this).attr("data-language");

    const currentContent = location.pathname.substring(
      location.pathname.indexOf("/", 1) + 1,
      location.pathname.length
    );

    window.location.href = "/" + selectedLanguage + "/" + currentContent;
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie("csrftoken");

console.log("Hey");

const listArrowIcon = $(".list-arrow");
let isOpen = 0;
const dropDownList = $(".list-dropdown");
const listField = $(".list-field");
listField.click(() => {
  dropDownList.toggleClass("hidden");
  listArrowIcon.toggleClass("rotate-180");
  keywordSearch.focus();
  isOpen++;
});

$(window).click((e) => {
  const target = $(e.target);

  if (
    !(
      target.hasClass("list-dropdown") ||
      target.parents(".list-dropdown").length !== 0
    ) &&
    !(
      target.hasClass("list-field") ||
      target.parents(".list-field").length !== 0
    ) &&
    !dropDownList.hasClass("hidden")
  ) {
    dropDownList.addClass("hidden");
    listArrowIcon.toggleClass("rotate-180");
  }
});

let filterData = $(".keyword").map((i, e) => {
  return $(e).html();
});

const keywordList = $(".keyword-list");
const keywordSelected = $(".keyword-selected");
const keywordSearch = $(".keyword-search");

const activeKeyword = () => {
  const keyword = $(".keyword");

  keyword.click((e) => {
    const value = $(e.target).html().trim();
    keywordSelected.val(value);
    dropDownList.addClass("hidden");
    keywordSearch.val("");
    listArrowIcon.toggleClass("rotate-180");
  });
};

keywordSearch.keyup((e) => {
  const value = $(e.target).val();
  keywordList.empty();

  filterData
    .filter((index, keyword) => {
      return keyword.toLowerCase().startWith(value.toLowerCase());
    })
    .map((index, keyword) =>
      keywordList.append(
        `<li class="py-1 cursor-pointer transition-all hover:pl-4 w-64 keyword">${keyword}</li>`
      )
    );

  activeKeyword();
});

activeKeyword();
$("input[name=email]").keyup(function () {
  $(this).val()
    ? $("#btnSubmit").removeClass("bg-opacity-50")
    : $("#btnSubmit").addClass("bg-opacity-50");
});

$("#preRegistrationForm").submit((e) => {
  e.preventDefault();
  let email = $("#email").val() ? $("#email").val() : null;
  let category = $("#category").val();
  $(".error-section").addClass("hidden");

  let data = {
    email: email,
    category: category,
  };

  $.ajax({
    type: "POST",
    url: "/api/v1/core/pre-registration/",
    data: data,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {
      $("#email").val("");
      $("#field").val("");

      $(".success-section").removeClass("hidden");
      $("#success-message").text(response.message);
      $(".success-section").fadeOut(5000);
    },
    error: function (response) {
      $(".error-section").removeClass("hidden");
      $("#error-message").text(response.responseJSON.message);
    },
  });
});
