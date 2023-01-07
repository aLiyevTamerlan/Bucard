//This class have profile functions and will seperate this other file
class Profile {
  constructor() {
    this.index = 0;
  }
  //Account dropdown
  dropDown = () => {
    const btn = $("#drop-down");
    const menu = $("#drop-down-items");
    const icon = $("#drop-down-icon");

    btn.click(() => {
      menu.toggleClass("hidden");
      icon.toggleClass("rotate-180");
      icon.toggleClass("rotate-0");
    });
  };
  //Switch account
  activeProfile = () => {
    const profiles = $(".profile-tab");
    const dashboardTab = $(".dashboard_tab");
    const profileTab = $(".profile_content");
    const companyTab = $(".company_content");
    const activeBar = $(".profile-active");
    profiles.click((e) => {
      console.log(e.target);
      const profile = $(e.target).parent();
      const profileIndex = profile.index();
      activeBar.first().addClass("animate-fadeOutTab");
      activeBar.hide();
      activeBar.eq(profileIndex).show();
      dashboardTab.hide();
      profileTab.hide();
      if (profileIndex === 0) {
        dashboardTab.show();
      } else if (profileIndex === 1) {
        profileTab.show();
      } else {
        companyTab.show();
      }
    });
  };
  //Saved profiles boxes
  defaultBoxes = () => {
    const boxes = [
      {
        boxImg: "../assets/icons/box_1.svg",
        boxTitle: "Marketing",
        boxAdded: "5",
      },
      {
        boxImg: "../assets/icons/box_2.svg",
        boxTitle: "Developing",
        boxAdded: "5",
      },
      {
        boxImg: "../assets/icons/box_3.svg",
        boxTitle: "Design",
        boxAdded: "5",
      },
      {
        boxImg: "../assets/icons/box_4.svg",
        boxTitle: "Technology",
        boxAdded: "5",
      },
      {
        boxImg: "../assets/icons/box_5.svg",
        boxTitle: "Copywriting",
        boxAdded: "5",
      },
      {
        boxImg: "../assets/icons/box_6.svg",
        boxTitle: "Education",
        boxAdded: "5",
      },
    ];

    const allBoxes = $(".all-boxes");
    boxes.forEach((box) => {
      const img = box.boxImg;
      const title = box.boxTitle;
      const added = box.boxAdded;

      allBoxes.append(
        `<div class="profile-box">
              <div class="rounded-full bg-avatar w-14 h-14 flex justify-center items-center">
                <img src="${img}" alt="" />
              </div>
              <div class="flex justify-end">
                <a>
                  <img src="../assets/icons/more-horizontal.svg" alt="" />
                </a>
              </div>
              <div class=" flex items-end">
                <span>${title}</span>
              </div>
              <div class="flex justify-end gap-2 items-end">
                <div>
                  <img src="../assets/icons/group.svg" alt="" />
                </div>
                <span class="text-sm">${added}</span>
              </div>
            </div>
          `
      );
    });
  };
  //Desktop category
  boxCategory = () => {
    const categories = $(".sidebar-item");
    const categoryContainer = $(".sidebar-container");
    const categoryTitle = $(".sidebar-title");
    categories.removeClass("sidebar-active");
    categories.eq(this.index).addClass("sidebar-active");
    let title = categories.eq(this.index).text().trim();
    categoryTitle.text(title);
    categoryContainer.hide();
    categoryContainer.eq(this.index).show();
    categories.click(function () {
      const category = $(this);
      this.index = category.index();
      categories.removeClass("sidebar-active");
      category.addClass("sidebar-active");
      let title = categories.eq(this.index).text().trim();
      categoryTitle.text(title);
      categoryContainer.hide();
      categoryContainer.eq(this.index).show();
      this.mobFilter();
    });
  };
  //Mobile filter category
  mobFilter = () => {
    const filter = $(".filter-mob");
    const filterContainer = $(".filter-container");
    const filterClose = $(".filter-close");
    const filterAnimate = $(".filter-animate");
    const filterCategories = $(".sidebar-item-mob");
    const filterBtn = $(".filter-btn");
    const filterContent = $(".sidebar-container-mob");
    filterContent.hide();
    filterContent.eq(this.index).show();
    //open filter modal and add animate
    filter.click(() => {
      filterContainer.removeClass("hidden");
      filterAnimate.removeClass("animate-fadeOutModal");
      filterAnimate.addClass("animate-fadeInModal");
    });

    window.onclick = (e) => {
      if (e.target == $(".inset-0")[0]) {
        setTimeout(() => {
          filterContainer.addClass("hidden");
        }, 390);
        filterAnimate.addClass("animate-fadeOutModal");
      }
    };

    //close filter modal and add animate
    filterClose.click(() => {
      setTimeout(() => {
        filterContainer.addClass("hidden");
      }, 390);
      filterAnimate.removeClass("animate-fadeInModal");
      filterAnimate.addClass("animate-fadeOutModal");
    });

    //choose filter
    filterCategories.removeClass("sidebar-active");
    filterCategories.eq(this.index).addClass("sidebar-active");
    filterCategories.click((e) => {
      const category = $(e.target);
      this.index = category.index();
      filterCategories.removeClass("sidebar-active");
      category.addClass("sidebar-active");

      // categoryContainer.hide();
      // categoryContainer.eq(index).show();
    });

    filterBtn.click(() => {
      setTimeout(() => {
        filterContainer.addClass("hidden");
      }, 390);
      filterAnimate.addClass("animate-fadeOutModal");
      filterContent.hide();
      filterContent.eq(this.index).show();
      this.boxCategory();
    });
  };
  //Pro profile tab
  proTab = () => {
    const proTabs = $(".pro-tab");
    const proTabsMob = $(".pro-tab-mob");
    const proContainers = $(".profile-container");
    const companyContainers = $(".company-container");
    const proTabsMobActive = $(".pro-tab-mob-active");
    proTabs.click(function () {
      let tab = $(this);
      let tabIndex = tab.index();
      console.log(tabIndex);
      proTabs.removeClass("pro-active");
      tab.addClass("pro-active");
      proContainers.hide();
      companyContainers.hide();
      companyContainers.eq(tabIndex).show();
      proContainers.eq(tabIndex).show();
    });

    proTabsMob.click(function () {
      let tab = $(this);
      let tabIndex = tab.index();
      proTabsMobActive.addClass("hidden");
      proTabsMobActive.eq(tabIndex).removeClass("hidden ");
      proContainers.hide();
      proContainers.eq(tabIndex + 3).show();
    });
  };

  proPortfolio = () => {
    const projectsData = [
      {
        id: 1,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 2,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 3,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 4,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 5,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 6,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 7,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 8,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 9,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 10,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 11,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
      {
        id: 12,
        name: "Project Name",
        img: "../assets/images/project_1.svg",
        view: 12,
        createdAt: "15 minutes age",
      },
    ];

    const projects = $(".projects");

    projectsData.map((project) =>
      projects.append(`<div class="project">
      <div class="flex flex-col items-center h-full justify-center gap-4">
        <div class="w-full">
          <!-- image -->
          <img class="rounded-sm w-full bg-cover" src=${project.img} alt="">
        </div>
        <div class="flex w-full justify-between">
          <div class="flex gap-3">
            <div>
              <div class="bg-primary bg-opacity-[12%] p-1 rounded-sm">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <mask id="mask0_1662_20790" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0"
                    width="16" height="16">
                    <rect width="16" height="16" fill="#D9D9D9" />
                  </mask>
                  <g mask="url(#mask0_1662_20790)">
                    <path
                      d="M10.6673 5.5987L4.75059 11.532C4.61725 11.6654 4.45881 11.732 4.27525 11.732C4.09214 11.732 3.93392 11.6654 3.80059 11.532C3.66725 11.3987 3.60059 11.2403 3.60059 11.0567C3.60059 10.8736 3.66725 10.7154 3.80059 10.582L9.73392 4.66536H4.66725C4.47836 4.66536 4.31992 4.60159 4.19192 4.47403C4.06436 4.34603 4.00059 4.18759 4.00059 3.9987C4.00059 3.80981 4.06436 3.65136 4.19192 3.52336C4.31992 3.39581 4.47836 3.33203 4.66725 3.33203H11.3339C11.5228 3.33203 11.681 3.39581 11.8086 3.52336C11.9366 3.65136 12.0006 3.80981 12.0006 3.9987V10.6654C12.0006 10.8543 11.9366 11.0125 11.8086 11.14C11.681 11.268 11.5228 11.332 11.3339 11.332C11.145 11.332 10.9868 11.268 10.8593 11.14C10.7313 11.0125 10.6673 10.8543 10.6673 10.6654V5.5987Z"
                      fill="#115EED" />
                  </g>
                </svg>
              </div>
            </div>
            <div>
            <!-- Project detail -->
              <p class="text-secondary">${project.name}</p>
              <span class="text-secondary font-normal text-sm text-opacity-50">${project.createdAt}</span>
            </div>
          </div>
          <div>
            <div class="flex gap-1.5 items-center pb-1">
              <span>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <mask id="mask0_1662_20813" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0"
                    width="16" height="16">
                    <rect width="16" height="16" fill="#D9D9D9" />
                  </mask>
                  <g mask="url(#mask0_1662_20813)">
                    <path
                      d="M8.00008 10.668C8.83342 10.668 9.54186 10.3764 10.1254 9.7933C10.7085 9.20975 11.0001 8.5013 11.0001 7.66797C11.0001 6.83464 10.7085 6.12619 10.1254 5.54264C9.54186 4.95952 8.83342 4.66797 8.00008 4.66797C7.16675 4.66797 6.4583 4.95952 5.87475 5.54264C5.29164 6.12619 5.00008 6.83464 5.00008 7.66797C5.00008 8.5013 5.29164 9.20975 5.87475 9.7933C6.4583 10.3764 7.16675 10.668 8.00008 10.668ZM8.00008 9.46797C7.50008 9.46797 7.07519 9.29286 6.72542 8.94264C6.37519 8.59286 6.20008 8.16797 6.20008 7.66797C6.20008 7.16797 6.37519 6.74286 6.72542 6.39264C7.07519 6.04286 7.50008 5.86797 8.00008 5.86797C8.50008 5.86797 8.92519 6.04286 9.27542 6.39264C9.62519 6.74286 9.80008 7.16797 9.80008 7.66797C9.80008 8.16797 9.62519 8.59286 9.27542 8.94264C8.92519 9.29286 8.50008 9.46797 8.00008 9.46797ZM8.00008 12.668C6.37786 12.668 4.90008 12.2151 3.56675 11.3093C2.23341 10.404 1.26675 9.19019 0.666748 7.66797C1.26675 6.14575 2.23341 4.93175 3.56675 4.02597C4.90008 3.12064 6.37786 2.66797 8.00008 2.66797C9.6223 2.66797 11.1001 3.12064 12.4334 4.02597C13.7667 4.93175 14.7334 6.14575 15.3334 7.66797C14.7334 9.19019 13.7667 10.404 12.4334 11.3093C11.1001 12.2151 9.6223 12.668 8.00008 12.668ZM8.00008 11.3346C9.25564 11.3346 10.4085 11.004 11.4587 10.3426C12.5085 9.68175 13.3112 8.79019 13.8667 7.66797C13.3112 6.54575 12.5085 5.65397 11.4587 4.99264C10.4085 4.33175 9.25564 4.0013 8.00008 4.0013C6.74453 4.0013 5.59164 4.33175 4.54141 4.99264C3.49164 5.65397 2.68897 6.54575 2.13341 7.66797C2.68897 8.79019 3.49164 9.68175 4.54141 10.3426C5.59164 11.004 6.74453 11.3346 8.00008 11.3346Z"
                      fill="#B9C5CF" />
                  </g>
                </svg></span>
                <!-- View count -->
              <span>${project.view}</span>
            </div>
          </div>
        </div>
      </div>
    </div>`)
    );
  };

  userSavedKeywords = () => {
    const savedKeywordsData = [
      {
        id: 1,
        keyword: "User-Centered Design",
      },
      {
        id: 2,
        keyword: "Facilitation",
      },
      {
        id: 3,
        keyword: "User Experience Design",
      },
      {
        id: 4,
        keyword: "Digital",
      },
      {
        id: 5,
        keyword: "Interaction Design",
      },
      {
        id: 6,
        keyword: "User Experience",
      },
      {
        id: 7,
        keyword: "UX Design",
      },
    ];
    const savedKeywords = $(".savedKeywords");
    savedKeywordsData.map((saveKeyword) =>
      savedKeywords.append(`<div class="savedKeyword ">
      <p class="font-normal text-secondary">${saveKeyword.keyword}</p>
    </div>`)
    );
    savedKeywords.append(`<div class="addKeyword">
      <div class="max-w-fit cursor-pointer text-primary flex gap-2 items-center">
        <span>
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M9 16.5C13.125 16.5 16.5 13.125 16.5 9C16.5 4.875 13.125 1.5 9 1.5C4.875 1.5 1.5 4.875 1.5 9C1.5 13.125 4.875 16.5 9 16.5Z"
              stroke="#115EED" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M6.87744 11.1239L11.1224 6.87891" stroke="#115EED" stroke-width="1.5"
              stroke-linecap="round" stroke-linejoin="round" />
            <path d="M11.1224 11.1239L6.87744 6.87891" stroke="#115EED" stroke-width="1.5"
              stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </span>
        <span>Add new keyword</span></div>
    </div>`);
  };
}

class PreRegister {
  homePage = () => {
    // //header
    // const logo = $(".logo");
    // const navLink = $("nav ul");

    // data.navLinks.map((item) => {
    //   if (item.id === "logo") {
    //     logo.append(`<img src=${item.title} alt="">`);
    //   } else if (item.id === "lang") {
    //     navLink.append(
    //       `<li class="cursor-pointer"><img src="${item.title[0].title}"/></li>`
    //     );
    //   } else {
    //     navLink.append(`
    //     <li class=" hidden md:block">
    //       <a href="#${item.id}">${item.title}</a>
    //     </li>
    //   `);
    //   }
    // });

    // //hero
    // const hero = data.hero;
    // let title = $("#hero .title");
    // let content = $("#hero .heroContent");
    // let button = $("#hero .btn");
    // let featuresContent = $("#hero .features .content");
    // let featuresImages = $("#hero .features .images");
    // title.append(`${hero.title}`);
    // content.append(`${hero.content}`);

    // const contentBtn = hero.button.content.split("/");
    // button.append(
    //   `${contentBtn[0]} / <span class="font-medium italic">${contentBtn[1]}</span>`
    // );
    // featuresContent.append(hero.features.content);

    // featuresImages.append(`<img src=${hero.features.links[0].image} alt="Download App Store" />
    // <img src=${hero.features.links[1].image} alt="Download Google Play" />`);

    // // whyBuca
    // const whyBuca = data.whyBuca;
    // title = $("#whyBuca .title");

    // title.append(whyBuca.title);
    // console.log(data);

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
      img.eq(0).removeClass("hidden");
      pricing.eq(1).addClass("hidden");
      pricing.eq(1).removeClass("grid");
      pricing.eq(0).removeClass("hidden");
      pricing.eq(0).addClass("grid");
    });

    btnBusiness.click(function () {
      btnBusiness.addClass("bg-primary text-white stroke-white");
      btnBusiness.removeClass("bg-white text-primary stroke-primary");
      btnPersonal.removeClass("bg-primary text-white");
      btnPersonal.addClass("bg-white text-primary");
      content.eq(0).addClass("hidden");
      content.eq(1).removeClass("hidden");
      img.eq(0).addClass("hidden");
      img.eq(1).removeClass("hidden");
      pricing.eq(0).addClass("hidden");
      pricing.eq(0).removeClass("grid");
      pricing.eq(1).removeClass("hidden");
      pricing.eq(1).addClass("grid");
    });
  };

  register = () => {
    const getPreRegisterList = async (api) => {
      const res = await axios.get(api);
      const data = await res.data;

      return data;
    };

    const data = [];
    const preRegisterListDataApi = "/api/v1/preCategory";

    getPreRegisterList(preRegisterListDataApi).then((data) => {
      for (keyword of data) {
        data.push(keyword);
      }
    });

    const activeKeyword = () => {
      const keyword = $(".keyword");

      keyword.click((e) => {
        const value = $(e.target).html();
        keywordSelected.html(value);
        dropDownList.addClass("hidden");
        keywordSearch.val("");
        listArrowIcon.toggleClass("rotate-180");
      });
    };

    const dropDownLang = $(".lang-dropdown");
    const langBtn = $(".lang-btn");
    langBtn.click(() => {
      dropDownLang.toggleClass("hidden");
    });

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

    let filterData = [...data];

    const keywordList = $(".keyword-list");
    const keywordSelected = $(".keyword-selected");
    const keywordSearch = $(".keyword-search");
    filterData.map((keyword) =>
      keywordList.append(
        `<li class="py-1 cursor-pointer transition-all hover:pl-4 w-64 keyword">${keyword}</li>`
      )
    );

    keywordSearch.keyup((e) => {
      const value = $(e.target).val();
      keywordList.empty();

      filterData
        .filter((keyword) =>
          keyword.toLocaleLowerCase().startsWith(value.toLocaleLowerCase())
        )
        .map((keyword) =>
          keywordList.append(
            `<li class="py-1 cursor-pointer transition-all hover:pl-4 w-64 keyword">${keyword}</li>`
          )
        );

      activeKeyword();
    });

    activeKeyword();
  };
}

const profile = new Profile();

profile.dropDown();
profile.activeProfile();
profile.defaultBoxes();
profile.boxCategory();
profile.mobFilter();
profile.proTab();
profile.proPortfolio();
profile.userSavedKeywords();

const preRegister = new PreRegister();

preRegister.homePage();
preRegister.register();

// axios
//     .post("http://127.0.0.1:8000/api/v1/preRegister/", {
//       email: $(".form-control").val(),
//       category: selected,
//     })
//     .then(function (response) {
//       $("#alert-success").fadeIn("slow");
//     })
//     .catch((er) => {
//       const emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
//       let inpVal = $(".form-control").val();
//       if (inpVal == "") {
//         $(".form-control").addClass("error-input");
//         $(".invalid-feedback").html("Email daxil edin");
//         $(".invalid-feedback").show();
//       } else if (!emailReg.test(inpVal)) {
//         $(".form-control").addClass("error-input");
//         $(".invalid-feedback").html("Email düzgün daxil edilməyib");
//         $(".invalid-feedback").show();
//       } else {
//         $(".form-control").addClass("error-input");
//         $(".invalid-feedback").html("Bu email artıq qeydiyyatdan keçib");
//         $(".invalid-feedback").show();
//       }
//     });

// const getField = async (URL) => {
//   let res = await fetch(URL);
//   let data = await res.json();
//   return data;
// };

// const lists = document.getElementById("fields");
// const inp = document.getElementById("field");

// const fetchUrl = "/api/v1/preCategory";
// getField(fetchUrl).then(function (value) {
//   for (const item of value) {
//     data.push(item.name);
//   }
// });
