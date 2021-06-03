

import data_get
import data_wordcloud
import data_map

data_dict = data_get.init()
data_get.china_total_data(data_dict)
data_get.global_total_data(data_dict)
data_get.china_daily_data(data_dict)
data_get.foreign_daily_data(data_dict)

data_wordcloud.china_wordcloud()
data_wordcloud.global_wordcloud()

data_map.all_map()
