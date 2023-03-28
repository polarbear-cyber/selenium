from booking.booking import Booking

with Booking() as bot:
    bot.launchBrowser()
    bot.acceptCookie()
    bot.changeCurrency(currency='GBP')
    bot.placeStay('New York')
    bot.dateStay(check_in = '2021-05-16',
                 check_out = '2021-05-23')
    bot.numberPeople(adult=10)
    bot.submitSearch()