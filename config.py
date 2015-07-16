import locale, sys
### Editable globals that may improve your performance ###
locale.setlocale(locale.LC_ALL, "") # this can be changed to show currency formats differently.
currency_symbol = "$"

STOCK_EXCHANGE_LIST = ["nyse", "nasdaq"] #add "amex" if desired, non-american exchanges will not function at this point.

DEFAULT_STOCK_EXCHANGE_ATTRIBUTE = "Exchange_na"
SECONDARY_STOCK_EXCHANGE_ATTRIBUTE = "StockExchange_yf"

DEFAULT_COMMISSION = 10.00

DEFAULT_ENCRYPTION_HARDNESS_LEVEL = 8 # 1-24: i'm under the impression that 8 is the most secure hardness my processer can compute quickly

SCRAPE_CHUNK_LENGTH = 50
# Had errors with yql (yahoo query language) at greater numbers than 50

SCRAPE_SLEEP_TIME = 18
# this is a very important number
# approx 200 calls per hour (yql forums info)
# 3600 seconds in an hour
# 3600 / 200 = 18 seconds pause per query to stay under the 200/hour limit.
# Had ip banned for 24 hour periods scraping yql at a greater rate than this,
# however, their documentation says you can scrape at a faster rate.
# Note that i was banned for periods for scraping at the max rate they officially allow.
ADDITIONAL_DATA_SCRAPE_SLEEP_TIME = 2
# Less important, because the number of scraping functions you exicute multiplies this by site,
# but you should adjust this significantly if you get your ip banned.


ABORT_YQL_SCRAPE = False

ONE_DAY = 86400.

TIME_ALLOWED_FOR_BEFORE_RECENT_UPDATE_IS_STALE = ONE_DAY * 2 # 48 hours
# This is how long the program will reject rescraping stocks when looking for stocks that were not saved successfully.
TIME_ALLOWED_FOR_BEFORE_YQL_DATA_NO_LONGER_APPEARS_IN_STOCK_LIST = ONE_DAY * 15 # 15 days

PORTFOLIO_PRICE_REFRESH_TIME = ONE_DAY * 3 # 3 days

DEFAULT_ROWS_ON_SALE_PREP_PAGE = 9
DEFAULT_ROWS_ON_TRADE_PREP_PAGE_FOR_TICKERS = 6
# adjust these to your own preference

# these will depend on your preferred data sources
DEFAULT_LAST_TRADE_PRICE_ATTRIBUTE_NAME = "LastSale_na"
DEFAULT_AVERAGE_DAILY_VOLUME_ATTRIBUTE_NAME = "AverageDailyVolume_yf"
#--
SECONDARY_LAST_TRADE_PRICE_ATTRIBUTE_NAME = "LastTradePriceOnly_yf"
SECONDARY_AVERAGE_DAILY_VOLUME_ATTRIBUTE_NAME = ""
#---
TERTIARY_LAST_TRADE_PRICE_ATTRIBUTE_NAME = ""
TERTIARY_AVERAGE_DAILY_VOLUME_ATTRIBUTE_NAME = ""
#----
QUATERNARY_LAST_TRADE_PRICE_ATTRIBUTE_NAME = ""
QUATERNARY_AVERAGE_DAILY_VOLUME_ATTRIBUTE_NAME = ""
#-------------------------------------------------


IRRELEVANT_ATTRIBUTES = ["updated",
	"epoch",
	"created_epoch",
	"TrailingPE_ttm_Date_yf",
	"TradeDate_yf",
	"TwoHundreddayMovingAverage_yf",
	"TickerTrend_yf",
	"SharesOwned_yf",
	"SP50052_WeekChange_yf",
	"PricePaid_yf",
	"PercentChangeFromTwoHundreddayMovingAverage_yf",
	"PercentChangeFromFiftydayMovingAverage_yf",
	"PercentChange_yf",
	"PERatioRealtime_yf",
	"OrderBookRealtime_yf",
	"Notes_yf",
	"MostRecentQuarter_mrq_yf",
	"MoreInfo_yf",
	"MarketCapRealtime_yf",
	"LowLimit_yf",
	"LastTradeWithTime_yf",
	"LastTradeTime_yf",
	"LastTradeRealtimeWithTime_yf",
	"LastTradePriceOnly_yf",
	"LastTradeDate_yf",
	"HoldingsValueRealtime_yf",
	"HoldingsValue_yf",
	"HoldingsGainRealtime_yf",
	"HoldingsGainPercentRealtime_yf",
	"HoldingsGainPercent_yf",
	"HoldingsGain_yf",
	"HighLimit_yf",
	"ExDividendDate_yf",
	"DividendPayDate_yf",
	"DaysValueChangeRealtime_yf",
	"DaysValueChange_yf",
	"DaysRangeRealtime_yf",
	"DaysRange_yf",
	"DaysLow_yf",
	"DaysHigh_yf",
	"Commission_yf",
	"Change_PercentChange_yf",
	"ChangeRealtime_yf",
	"ChangePercentRealtime_yf",
	"ChangeFromTwoHundreddayMovingAverage_yf",
	"ChangeFromFiftydayMovingAverage_yf",
	"Change_yf",
	"ChangeinPercent_yf",
	"BidRealtime_yf",
	"Bid_yf",
	"AvgVol_3_month_yf",
	"AvgVol_10_day_yf",
	"AskRealtime_yf",
	"Ask_yf",
	"AnnualizedGain_yf",
	"AfterHoursChangeRealtime_yf",
	"p_52_WeekLow_Date_yf",
	"p_52_WeekLow_yf",
	"p_52_WeekHigh_Date_yf",
	"p_52_WeekHigh_yf",
	"p_52_WeekChange_yf",
	"p_50_DayMovingAverage_yf",
	"p_200_DayMovingAverage_yf"
	]
# these attributes will not show up on most spreadsheets
CLASS_ATTRIBUTES = ["testing_reset_fields",
	"nasdaq_symbol",
	"aaii_symbol",
	"yahoo_symbol",
	"morningstar_symbol",
	"yql_ticker",
	"epoch",
	"created_epoch",
	"updated",
	"ticker_relevant",
	"last_yql_basic_scrape_update",
	"last_balance_sheet_update_yf",
	"last_balance_sheet_update_ms",
	"last_cash_flow_update_yf",
	"last_cash_flow_update_ms",
	"last_income_statement_update_yf",
	"last_income_statement_update_ms",
	"last_key_ratios_update_ms",
	"last_aaii_update_aa",
	"held_list"
	]

NUMBER_OF_DEAD_TICKERS_THAT_SIGNALS_AN_ERROR = 100
# when downloading tickers, if more than this number of tickers appear to have fallen off the exchange
# it is probably the case that something went wrong, rather than it being a legitimate number.


STOCK_SCRAPE_UPDATE_ATTRIBUTES = ["last_yql_basic_scrape_update",

	"last_balance_sheet_update_yf",
	"last_cash_flow_update_yf",
	"last_income_statement_update_yf",

	"last_balance_sheet_update_ms",
	"last_cash_flow_update_ms",
	"last_income_statement_update_ms",

	"last_key_ratios_update_ms",


	]

HELD_STOCK_COLOR_HEX = "#FAEFCF"
NEGATIVE_SPREADSHEET_VALUE_COLOR_HEX = "#8A0002"

NUMBER_OF_DEFAULT_PORTFOLIOS = 3

FULL_SPREADSHEET_SIZE_POSITION_TUPLE = ((980,637),(0,50)) # size=(width, height), pos=(x-axis, y-axis)
RANK_PAGE_SPREADSHEET_SIZE_POSITION_TUPLE = ((980,625),(0,60))
RANK_PAGE_ATTRIBUTES_THAT_DO_NOT_SORT_REVERSED = ["symbol", "firm_name"]
PORTFOLIO_PAGE_SPREADSHEET_SIZE_POSITION_TUPLE = ((960,580),(0,50))
CUSTOM_ANALYSIS_SPREADSHEET_SIZE_POSITION_TUPLE = ((855,578),(105,58))

###################################################################################################
################# Do not edit below, all are reset to saved values on startup #####################
###################################################################################################
GLOBAL_PAGES_DICT = {}

# unique ids
# top level tabs
#
WELCOME_PAGE_UNIQUE_ID 			= "w"
GET_DATA_PAGE_UNIQUE_ID 		= "g"
#
# ## second level tabs
TICKER_PAGE_UNIQUE_ID				= "g_ti"
YQL_SCRAPE_PAGE_UNIQUE_ID			= "g_yq"
SPREADSHEET_IMPORT_PAGE_UNIQUE_ID	= "g_sp"
# ## ### third level tabs
XLS_IMPORT_PAGE_UNIQUE_ID 				= "g_sp_xls"
CSV_IMPORT_PAGE_UNIQUE_ID 				= "g_sp_csv"
# ## ###
# ##
#
PORTFOLIO_PAGE_UNIQUE_ID 		= "p"
VIEW_DATA_PAGE_UNIQUE_ID 		= "v"
#
# ##
ALL_STOCKS_PAGE_UNIQUE_ID 			= "v_al"
STOCK_DATA_PAGE_UNIQUE_ID 			= "v_st"
# ##
#
ANALYSE_PAGE_UNIQUE_ID 			= "a"
#
# ##
SCREEN_PAGE_UNIQUE_ID 				= "a_sc"
SAVED_SCREEN_PAGE_UNIQUE_ID 		= "a_sa"
RANK_PAGE_UNIQUE_ID 				= "a_ra"
CUSTOM_ANALYSE_META_PAGE_UNIQUE_ID= "a_pe"
# ##
#
SALE_PREP_PAGE_UNIQUE_ID 		= "s"
TRADE_PAGE_UNIQUE_ID 			= "t"
USER_FUNCTIONS_PAGE_UNIQUE_ID 	= "u"
#
# ##
USER_CREATED_TESTS_UNIQUE_ID 			 = "u_cr"
USER_RANKING_FUNCTIONS_UNIQUE_ID 		 = "u_ra"
USER_CSV_IMPORT_FUNCTIONS_UNIQUE_ID 	 = "u_cs"
USER_XLS_IMPORT_FUNCTIONS_UNIQUE_ID 	 = "u_xl"
USER_PORTFOLIO_IMPORT_FUNCTIONS_UNIQUE_ID= "u_po"
USER_CUSTOM_ANALYSIS_FUNCTIONS_UNIQUE_ID = "u_cu"
# ##
#
GLOBAL_UNIQUE_ID_LIST = [
	WELCOME_PAGE_UNIQUE_ID,
	GET_DATA_PAGE_UNIQUE_ID,
	TICKER_PAGE_UNIQUE_ID,
	YQL_SCRAPE_PAGE_UNIQUE_ID,
	SPREADSHEET_IMPORT_PAGE_UNIQUE_ID,
	XLS_IMPORT_PAGE_UNIQUE_ID,
	CSV_IMPORT_PAGE_UNIQUE_ID,
	PORTFOLIO_PAGE_UNIQUE_ID,
	VIEW_DATA_PAGE_UNIQUE_ID,
	ALL_STOCKS_PAGE_UNIQUE_ID,
	STOCK_DATA_PAGE_UNIQUE_ID,
	ANALYSE_PAGE_UNIQUE_ID,
	SCREEN_PAGE_UNIQUE_ID,
	SAVED_SCREEN_PAGE_UNIQUE_ID,
	RANK_PAGE_UNIQUE_ID,
	CUSTOM_ANALYSE_META_PAGE_UNIQUE_ID,
	SALE_PREP_PAGE_UNIQUE_ID,
	TRADE_PAGE_UNIQUE_ID,
	USER_FUNCTIONS_PAGE_UNIQUE_ID,
	USER_CREATED_TESTS_UNIQUE_ID,
	USER_RANKING_FUNCTIONS_UNIQUE_ID,
	USER_CSV_IMPORT_FUNCTIONS_UNIQUE_ID,
	USER_XLS_IMPORT_FUNCTIONS_UNIQUE_ID,
	USER_PORTFOLIO_IMPORT_FUNCTIONS_UNIQUE_ID,
	USER_CUSTOM_ANALYSIS_FUNCTIONS_UNIQUE_ID,
	]
if len(GLOBAL_UNIQUE_ID_LIST) != len(set(GLOBAL_UNIQUE_ID_LIST)):
	# one of the ids is not unique
	print "Error: GLOBAL_UNIQUE_ID_LIST has duplicates"
	dummy_list = []
	duplicates = []
	for u_id in GLOBAL_UNIQUE_ID_LIST:
		if u_id not in dummy_list:
			dummy_list.append(u_id)
		else:
			duplicates.append(u_id)
	print duplicates
	sys.exit()

GLOBAL_TABS_DICT = {}

GLOBAL_STOCK_DICT = {}

GLOBAL_TICKER_LIST = []

GLOBAL_ATTRIBUTE_SET = set([])

ENCRYPTION_POSSIBLE = None
ENCRYPTION_HARDNESS_LEVEL = None

# Portfolio globals
PASSWORD = None

DATA_ABOUT_PORTFOLIOS = [NUMBER_OF_DEFAULT_PORTFOLIOS,[]]
# Structure of this variable below,
# see "wxStocks_db_functions.load_DATA_ABOUT_PORTFOLIOS" for more info about loading.

# DATA_ABOUT_PORTFOLIOS = 	[
#								NUMBER_OF_PORTFOLIOS (this will be an integer),
#								[
#									"Portfolio Name" (this will be a string),
#									etc...
#								]
#							]
DEFAULT_DATA_ABOUT_PORTFOLIOS = [NUMBER_OF_DEFAULT_PORTFOLIOS, []]

# Default name is "Primary"
NUMBER_OF_PORTFOLIOS = 0
PORTFOLIO_NAMES = []

PORTFOLIO_OBJECTS_DICT = {}
###

# Screen globals
GLOBAL_STOCK_SCREEN_DICT = {}
SCREEN_NAME_AND_TIME_CREATED_TUPLE_LIST = []
CURRENT_SCREEN_LIST = []
CURRENT_SAVED_SCREEN_LIST = []
RANK_PAGE_ALL_RELEVANT_STOCKS = []
###

SALE_PREP_PORTFOLIOS_AND_SALE_CANDIDATES_TUPLE = [[],[]] # description below
# [[relevant portfolios list], [sale ticker|#shares tuple list]]

TICKER_AND_ATTRIBUTE_TO_UPDATE_TUPLE_LIST = []

HELD_STOCK_TICKER_LIST = []

CURRENT_EXCHANGE_FOR_NASDAQ_SCRAPE = None





