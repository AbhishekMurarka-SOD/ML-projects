def scrap_image_url(driver):
    images=driver.find_elements_by_xpath("//img[@class='a-section aok-relative s-image-tall-aspect']")

    product_data = {}
    product_data['image_urls'] = []

    for image in images:
        source= image.get_attribute('src')
        product_data['image_urls'].append(source)

    return product_data