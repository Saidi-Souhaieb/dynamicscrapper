# Dynamic Scrapper **STILL IN DEVELOPMENT**

## The Goal Of This Package:

The goal of this package is being able to **scrap any site given** and **gather any data** no matter they type/style of said site.

This project was a huge part of understanding webscrapping in general.

## How to use:

The package is equipped with a **CLICK CLI** to give the input needed to extract the data needed.

### **Steps:**
1. First step is giving the link of the site you want scrapped. (it can be either a page that contains a bunch of links to click and extract data from inside every link or one single page that you want data extracted from).
2. If the link you gave is of a page containing a bunch of links to get data from, write the class name of the <div> containing the "a" tag that contains these links (in most cases these links always have the same class name)**[LEAVE EMPTY IF IT'S A SINGLE PAGE EXTRACTION]**.
3. Choose the type of pagination used in said page to be able to extract data from all pages:
  - number: for sites with numbered pagination
  - see_more: for sites with a see more button that expands the rest of the information
  - none: incase of a single page or a infinite scrollp age 
4. Write the class name of the pagination class used according to:
  - number: write the class name of the button "next" or ">" that takes you to the next page
  - see_more: write the class name of the see_more button
  - none: leave empty
5. Choosing the items to scrap
This step is gonna look like this: 
  - Choose a name for the item 
  - Choose the type you want to use to extract said item:
            - tag-name: using html tag names
            - class-name: using class-names
            - id: using id
            - name: using name attribute
            - link-text: by giving the text inside a "a" tag
  - Choose the name of the type you specified before:
            - tag-name : the tag name you want to extract from (h1, h2, a ...)
            - class-name: the class name needed
            - id: the id needed
            - name: the name inside the attribute
            - link-text: the text inside the "a" tag 
  - **IF** you are trying to get the value inside an attribute of a tag, write the tag name   you want to get (for example you need img url inside an "img" tag, you write "src" to get the text inside the src)
  - Choose Y or N to continue adding items to scrap or stop.

## Tips for number 5:
  - use tag-name when there is only one tag of that kind (h1..)
  - class-name is the most used but make sure to take a unique name so you dont get other items by mistake.
  - be carefull when using id as an id can change from page to page of the same element.
          

