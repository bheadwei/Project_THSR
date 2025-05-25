class BookingInfoParser:
    def __init__(self, driver):
        self.driver = driver

    def parse_info(self):
        info_card = self.driver.find_element("css selector", "div.ticket-card")
        return {
            "去/回程|direction": info_card.find_element("css selector", "span.direction").text.strip(),
            "出發日期|date": info_card.find_element("css selector", "span.date").text.strip(),
            "車次號碼|train_no": info_card.find_element("css selector", "p.train-no").text.strip(),
            "出發時間|departure time": info_card.find_element("css selector", "#setTrainDeparture0").text.strip(),
            "抵達時間|arrival time": info_card.find_element("css selector", "#setTrainArrival0").text.strip(),
            "出發站|dep_stn": info_card.find_element("css selector", ".departure-stn span").text.strip(),
            "抵達站|arr_stn": info_card.find_element("css selector", ".arrival-stn span").text.strip(),
            "車程時間|duration": info_card.find_element("css selector", "#InfoEstimatedTime0").text.strip(),
            "座位|seat": self.driver.find_element("css selector", "div.seat-label").text.strip(),
            "票卷|type": self.driver.find_element("css selector", "span.uk-leader-fill").text.strip(),
            "價錢|price": self.driver.find_element("css selector", "div#InfoPrice0").text.strip()
        }
