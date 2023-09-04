class DataTable {
  constructor(rootId, options) {
    this.root = document.getElementById(rootId)
    this.options = options
    this.currentPage = 1

    this.initialize()
    this.render()
  }

  // Initialize the DOM elements defining the table
  initialize() {
    const pagination = $(`<div class="pagination"></div>`)
    const table = $(`<table class="table"></table>`)
    const thead = $(`<thead></thead>`)
    const tbody = $(`<tbody></tbody>`)

    const tr = $(`<tr></tr>`)
    this.options.columns?.forEach(c => $(tr).append($(`<th>${c}</th>`)))

    $(thead).append(tr)
    $(table).append(thead)
    $(table).append(tbody)

    $(this.root).append(pagination)
    $(this.root).append(table)
  }

  // Render the data tbale
  async render() {
    const data = await this.fetchData()
    this.renderData(data)
    this.renderPagination(data)
  }

  // Render the table data
  async renderData(data) {
    const tbody = $(this.root).find("tbody").first()
    tbody.empty()

    data.results?.forEach(row => {
      const tr = $("<tr></tr>")
      Object.values(row).forEach(value => $(tr).append(`<td>${value}</td>`))
      $(tbody).append(tr)
    })
  }

  // Render the table pagination
  async renderPagination(data) { 
    const pagination = $(this.root).find(`div[class="pagination"]`)
    $(pagination).find("button").off("click")
    $(pagination).empty()

    const start = this.options.perPage * (this.currentPage - 1) + 1
    const end = Math.min(data.count, this.options.perPage * this.currentPage)
    $(pagination).append(`<span class="mr-2">Showing ${start} - ${end} of ${data.count}</span>`)
    
    const prevButton = $(`<button class="btn--icon"><span class="icon">chevron_left</span></button>`)
    $(prevButton).prop("disabled", !data.previous)
    $(prevButton).on("click", () => this.onPrevPage())
    $(pagination).append(prevButton)

    const nextButton = $(`<button class="btn--icon"><span class="icon">chevron_right</span></button>`)
    $(nextButton).prop("disabled", !data.next)
    $(nextButton).on("click", () => this.onNextPage())
    $(pagination).append(nextButton)
  }

  // Fetch the current page's data from the API
  async fetchData() {
    const pageUrl = new URL(this.options.url, window.location.origin)
    pageUrl.searchParams.set("page", this.currentPage)
    pageUrl.searchParams.set("per_page", this.options.perPage)

    const resp = await fetch(pageUrl)
    const data = await resp.json()

    return data
  }

  onPrevPage() {
    this.currentPage--
    this.render()
  }

  onNextPage() {
    this.currentPage++
    this.render()
  }
}
