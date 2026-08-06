import scrapy

class BooksSpider(scrapy.Spider):
    name = "Books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    RATING_MAP = {
        "One": 1,"Two": 2,"Three": 3,"Four": 4,"Five": 5
    }
    Max_Books = 200
    Books_Queued = 0

    def parse(self, response):
        Book_Links = response.css("article.product_pod h3 a::attr(href)").getall()

        for link in Book_Links:
            if self.Books_Queued >= self.Max_Books:
                return

            self.Books_Queued += 1
            Book_url = response.urljoin(link)
            yield scrapy.Request(Book_url, callback=self.parse_book)

        if self.Books_Queued < self.Max_Books:
            next_page = response.css("li.next a::attr(href)").get()

            if next_page:
                next_url = response.urljoin(next_page)
                yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):
        Title = response.css("div.product_main h1::text").get()
        Category = response.css("ul.breadcrumb li:nth-child(3) a::text").get()
        Price = response.css("p.price_color::text").get()
        Rating_Class = response.css("p.star-rating::attr(class)").get()
        Rating_Word = Rating_Class.split()[-1] if Rating_Class else None
        Rating = self.RATING_MAP.get(Rating_Word)
        Availability_Text = response.css("p.instock.availability::text").getall()
        Availability = " ".join(t.strip() for t in Availability_Text if t.strip())
        Description = response.css("#product_description ~ p::text").get()
        Table_Headers = response.css("table.table.table-striped th::text").getall()
        Table_Values = response.css("table.table.table-striped td::text").getall()
        Table_Data = dict(zip(Table_Headers, Table_Values))

        yield {
            "Title": Title,
            "Category": Category,
            "Price": Price,
            "Rating": Rating,
            "Availability": Availability,
            "Description": Description,
            "UPC": Table_Data.get("UPC"),
            "Num_Reviews": Table_Data.get("Number of reviews"),
            "Product_url": response.url,
        }