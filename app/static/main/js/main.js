"use strict";
$(function () {
  /* WHY  BUCA & PRICING */
  const icon = $(".tab_link .trend_up");

  $(document).on("click", ".tab_link", function (e) {
    e.preventDefault();
    $(".tab_link").removeClass("active");
    $(".why_buca_tab_content").removeClass("active");
    $(".whyBuca__right").removeClass("active");
    $(".pricing__cards_sect").removeClass("active");
    $(this).addClass("active");
    let index = $(".tab_link.active").attr("data-index");
    $(`.pricing__switch_btns .tab_link[data-index="${index}"]`).addClass(
      "active"
    );
    $(`.why_buca_tab_btns .tab_link[data-index="${index}"]`).addClass("active");
    let currentTabWhyBuca = $(`.why_buca_tab_content[data-index="${index}"]`);
    let currentTabPricing = $(`.pricing__cards_sect[data-index="${index}"]`);
    let currentImg = $(`.whyBuca__right[data-index="${index}"]`);
    currentTabWhyBuca.addClass("active").fadeIn("3000");
    currentTabPricing.addClass("active");
    currentImg.addClass("active");
    $(this).attr("data-index") == 2
      ? icon.attr("src", "./assets/icons/trend-up-white.svg")
      : icon.attr("src", "./assets/icons/trend-up.svg");
  });

  $(".tab_link ").hover(
    function () {
      icon.attr("src", "./assets/icons/trend-up-white.svg");
    },
    function () {
      if ($(".tab_link.active").attr("data-index") == 1) {
        icon.attr("src", "./assets/icons/trend-up.svg");
      }
    }
  );

  /* PROFILE TABS */
  $(document).on("click", ".profile_nav_link", function () {
    $(".profile_nav_link").removeClass("active");
    $(".profile_section").removeClass("active");
    $(this).addClass("active");
    let index = $(".profile_nav_link.active").attr("data-index");
    let currentTab = $(`.profile_section[data-index="${index}"]`);
    currentTab.addClass("active");
  });

  /* REGISTER ACCOUNT TYPE */
  $(document).on("click", ".register__type", function (e) {
    $(this).children().removeClass("active");
    $(e.target).addClass("active");
  });

  /* PASSWORD */
  $(".password__eye").on("click", function () {
    $(".password__eye").toggleClass("hidden");
    const inpType = $("#password").attr("type");
    inpType === "password"
      ? $("#password").prop("type", "text")
      : $("#password").prop("type", "password");
  });
  /*lOGIN */

  /*SEARCH*/

  /*DASHBORD*/

  //qrcode
  $(document).on("click", ".qr_code", function () {
    $(".green_bg").toggle();
  });

  //nav
  $(document).on("click", ".nav .nav_tab", function () {
    $(".nav .nav_tab").removeClass("active");
    $(this).addClass("active");
  });

  $(document).on("click", ".nav_mobile .nav_tab", function () {
    $(".nav_mobile .nav_tab").removeClass("active");
    $(".mobile_dashboard_tab").removeClass("active");
    $(this).addClass("active");
    let index = $(".nav__mobile .nav_tab.active").attr("data-index");
    let mobileDashboardCurrentTab = $(
      `.mobile_dashboard_tab[data-index="${index}"]`
    );
    mobileDashboardCurrentTab.addClass("active");
  });

  // preRegister Home

  const btnPersonal = $(".btn-personal");
  const btnBusiness = $(".btn-business");
  const content = $(".whybucard-content");
  const img = $(".whybucad-img");
  const pricing = $(".pricing");

  btnPersonal.click(function () {
    btnPersonal.addClass("bg-primary text-white");
    btnPersonal.removeClass("bg-white text-primary");
    btnBusiness.removeClass("bg-primary text-white stroke-white");
    btnBusiness.addClass("bg-white text-primary stroke-primary");
    content.eq(1).addClass("hidden");
    content.eq(0).removeClass("hidden");
    img.eq(1).addClass("hidden");
    img.eq(3).addClass("hidden");
    img.eq(0).removeClass("hidden");
    img.eq(2).removeClass("hidden");
    pricing.eq(1).addClass("hidden");
    pricing.eq(0).removeClass("hidden");
  });

  btnBusiness.click(function () {
    btnBusiness.addClass("bg-primary text-white stroke-white");
    btnBusiness.removeClass("bg-white text-primary stroke-primary");
    btnPersonal.removeClass("bg-primary text-white");
    btnPersonal.addClass("bg-white text-primary");
    content.eq(0).addClass("hidden");
    content.eq(1).removeClass("hidden");
    img.eq(0).addClass("hidden");
    img.eq(2).addClass("hidden");
    img.eq(1).removeClass("hidden");
    img.eq(3).removeClass("hidden");
    pricing.eq(0).addClass("hidden");
    pricing.eq(1).removeClass("hidden");
  });
});
