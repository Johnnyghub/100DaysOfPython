from apt_data_bot import AptDataBot

# Remade the apartment data bot to work on June 18 2022, as it stopped working due to chrome and site updates

bot = AptDataBot()
bot.get_apt_data()  # gets the data from the site
bot.enter_data_to_form()  # enters said data into custom google form
