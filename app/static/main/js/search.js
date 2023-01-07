const keywords = [
  "New Startup in on way!",
  "Creative",
  "UX Design",
  "UI Design",
  "Product Des",
  "Creative",
  "UX Design",
  "UI Design",
  "Product Des",
  "Azerbaijan",
];

class TagInput {
  constructor() {
    this.tagList = [];
  }

  add = (tag) => {
    tag = tag.trim();
    tag &&
      (this.tagList.length !== 0
        ? this.tagList.includes(tag)
          ? null
          : this.tagList.push(tag)
        : this.tagList.push(tag));
  };

  remove = (tag) => {
    this.tagList = this.tagList.filter((item) => item != tag);
  };
}

for (const i of keywords) {
  $(".keywords-container").append(`<button class="keyword">${i}</button>`);
}

const tagInput = new TagInput();

const showTags = () => {
  tagList = tagInput.tagList;
  $(".input-keywords").empty();
  for (const tag of tagList) {
    $(".input-keywords").append(
      `<span class="keyword-selected d-flex">${tag}<img onclick="" class="keyword-delete" src="/assets/icons/close.svg" alt=""
/></span>`
    );
  }
};

$(document).ready(() => {
  $("#search").keyup((e) => {
    if (e.which === 13) {
      if (tagInput.tagList.length < 3) tagInput.add(e.target.value);
      showTags();
      e.target.value = "";
    }
  });

  $(document).on("click", ".keyword-delete", (e) => {
    $(e.target).parent().remove();
    tagInput.remove($(e.target).parent().text());
  });

  $(document).on("click", ".keyword", (e) => {
    if (tagInput.tagList.length < 3) {
      tagInput.add($(e.target).text());
      showTags();
    }
  });
});
