$(document).ready(() => {
  const { origin, pathname } = window.location;
  let activeLink = null

  $(`nav a[class="nav-item"]`).each((_, link) => {
    const path = $(link).prop("href").replace(origin, "")

    if (path === "/" && origin === pathname) {
      activeLink = link
      break
    }

    if (pathname.startsWith(path)) {
      activeLink = link;
    }
  })

  if (!!activeLink) {
    $(activeLink).addClass("active");
  }
})
