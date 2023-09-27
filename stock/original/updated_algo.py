# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:45:38 2020

@author: dhruv
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:20:26 2020

@author: dhruvit "lashdk" kothari


"""
import datetime
import pandas as pd
import yfinance as yf
import copy
import matplotlib.pyplot as plt
import math


# @BCP - Follow PEP8 for class naming convention
# Doc string should be split up to individual methods
class Stock_Lot_Long(object):
    """
    An object of type Stock_Lot_Long used to create stock_lot of the type "LONG"
    Input parameters:
        stock= Name of the stock(String)
        buy_price=The price at which the stock is bought(Float)
        quantity=The amount of stock bought(Int)
        date= The date at which the stock was bought
        stop_loss=The stop loss price of the stock_lot(Float)
        target=the target price of the stock_lot(Float)



    class variable "tag" is used to assign unique idenifiers to stock_lot. (Helps to differentiate stock_lots)




    Functions:
        __init__ : Intialises all the variables. Also updates "tag" by 1.
            self.stock= Used to store stock
            self.date=Used to store date
            self.buy_price=Used to store buy_price
            self.stop_loss=Used to store stop_loss.If stop_loss not given assigns a default value.
            self.target=Used to store target.If target not given assigns a default value.

        get_stock_name() : Returns self.stock

        get_stock_quantity() : Returns self.quantity

        get_stock_buy_price(): Returns self.buy_price

        get_stock_stop_loss(): Returns self.stop_loss

        get_stock_target(): Returns self.target

        get_stock_face_value(): Returns the amount spent to buy the respective stock_lot

        get_stock_tag(): Returns identifier "tag"

        get_stock_date(): Returns self.date

        set_stock_stop_loss(stop_loss): Sets self.stop_loss to a particular value(Float)

        set_stock_target(target) : Sets self.target to a particular value(Float)


        __str__() : Prints basic information about the stock lot. Eg quantity,date,buy_price

    """

    # @BCP - The above documentation states that the tag class attribute is used as a unique identifier.
    # However, using tag as a class attribute defeats the uniqueness objective - demonstrate via class_attr_example.py
    tag = 1

    # @BCP - Don't convert argument underneath the hood.  Force the user to do it beforehand.
    def __init__(self, stock, buy_price, quantity, date, stop_loss=None, target=None):
        self.stock = str(stock)
        self.date = date
        self.quantity = int(quantity)
        self.buy_price = float(buy_price)
        Stock_Lot_Long.tag += 1

        # @BCP - should be if stop_loss is None
        if stop_loss == None:
            # @BCP - magic number
            self.stop_loss = 0.90 * buy_price
        else:
            self.stop_loss = stop_loss

        # @BCP - same issues as above
        if target == None:
            self.target = 1.05 * buy_price
        else:
            self.target = target

    # The get methods (except get_face_value) listed below are repetitive - just call the attribute
    def get_stock_name(self):
        return self.stock

    def get_stock_quantity(self):
        return self.quantity

    def get_stock_buy_price(self):
        return self.buy_price

    def get_stock_stop_loss(self):
        return self.stop_loss

    def get_stock_target(self):
        return self.target

    def get_face_value(self):
        return self.buy_price * self.quantity

    # @BCP - In the __init__() method, stop_loss can be None; in fact, that is the default value.
    # However, this method gives a conflicting story, since passing None will raise an Exception when calling float(None)
    # Why does the stop_loss have to be a float?  Why can't it also be an integer considering we are talking about prices?
    def set_stock_stop_loss(self, stop_loss):
        self.stop_loss = float(stop_loss)

    # @BCP - In the __init__() method, target can be None; in fact, that is the default value.
    # However, this method gives a conflicting story, since passing None will raise an Exception when calling float(None)
    # Why does the target have to be a float?  Why can't it also be an integer considering we are talking about prices?
    def set_stock_target(self, target):
        self.target = float(target)

    def get_stock_tag(self):
        return Stock_Lot_Long.tag

    def get_stock_date(self):
        return self.date

    # @BCP - This should be an f-string
    def __str__(self):
        result = self.get_stock_name() + ":" + " Number of shares:" + str(
            self.get_stock_quantity()) + "  bought at:" + str(self.get_stock_buy_price())
        result += " Buy Date:" + str(self.get_stock_date())
        return result


# @BCP - This class is almost a repeat of Stock_Lot_Long.  The only things that are different is the multipliers in the
# __init__ and the __str__
class Stock_Lot_Short(object):
    """
    An object of type Stock_Lot_Short used to create stock_lot of the type "SHORT"
    Input parameters:
        stock= Name of the stock(String)
        sell_price=The price at which the stock was sold(Float)
        quantity=The amount of stock sold(Int)
        date= The date at which the stock was sold
        stop_loss=The stop loss price of the stock_lot(Float)
        target=the target price of the stock_lot(Float)



    class variable "tag" is used to assign unique identifiers to stock_lot. (Helps to differentiate stock_lots)




    Functions:
        __init__ : Intialises all the variables. Also updates "tag" by 1.
            self.stock= Used to store stock
            self.date=Used to store date
            self.sell_price=Used to store sell_price
            self.stop_loss=Used to store stop_loss.If stop_loss not given assigns a default value.
            self.target=Used to store target.If target not given assigns a default value.

        get_stock_name() : Returns self.stock

        get_stock_quantity() : Returns self.quantity

        get_stock_sell_price(): Returns self.sell_price

        get_stock_stop_loss(): Returns self.stop_loss

        get_stock_target(): Returns self.target

        get_stock_face_value(): Returns the amount gained after selling the respective stock_lot

        get_stock_tag(): Returns identifier "tag"

        get_stock_date(): Returns self.date

        set_stock_stop_loss(stop_loss): Sets self.stop_loss to a particular value(Float)

        set_stock_target(target) : Sets self.target to a particular value(Float)


        __str__() : Print basic information about the stock lot. Eg quantity,date,sell_price



    """

    tag = 1

    def __init__(self, stock, sell_price, quantity, date, stop_loss=None, target=None):
        self.stock = str(stock)
        self.date = date
        self.quantity = int(quantity)
        self.sell_price = float(sell_price)
        Stock_Lot_Short.tag += 1

        if stop_loss == None:
            self.stop_loss = 1.05 * sell_price
        else:
            self.stop_loss = stop_loss

        if target == None:
            self.target = 0.98 * sell_price
        else:
            self.target = target

    def get_stock_name(self):
        return self.stock

    def get_stock_quantity(self):
        return self.quantity

    def get_stock_sell_price(self):
        return self.sell_price

    def get_stock_stop_loss(self):
        return self.stop_loss

    def get_stock_target(self):
        return self.target

    def get_face_value(self):
        return self.sell_price * self.quantity

    def set_stock_stop_loss(self, stop_loss):
        self.stop_loss = float(stop_loss)

    def set_stock_target(self, target):
        self.target = float(target)

    def get_stock_tag(self):
        return Stock_Lot_Short.tag

    def get_stock_date(self):
        return self.date

    def __str__(self):
        result = self.get_stock_name() + ":" + " Number of shares:" + str(
            self.get_stock_quantity()) + "  Short at:" + str(self.get_stock_sell_price())
        result += " Buy Date:" + str(self.get_stock_date())
        return result


# @BCP - not sure if this is a good case to use inheritance.  There is only one extra argument (ema) and the
# get_stock_ema() method just retrieves the ema attribute.
class Stock_Lot_EMA(Stock_Lot_Long):
    """


    Parameters
    ----------
    Parent class : Stock_Lot_Long
    Inherits all the functions of the parent class. eg get_stock_buy_price(), get_stock_quantity() etc



    Stock_Lot_Long : TYPE

    Additonal input parameters:

        ema = A TUPLE OF "2" DAYS(INT) to indicate entry and exit position.Eg ema=(50,100)
            DESCRIPTION. EMA STOCK LOT LONG OBJECT. WILL ONLY EXIT IF value ema[1]<ema[2]

    Additonal variables:
        self.ema_shorter : Used to store ema[1] (Int)
        self.ema_longer : Ued to store ema[2] (Int)

    Additonal functions:
        get_stock_ema(): Returns self.ema_shorter,self.ema_longer . Eg  Returns (50,100)



    """

    def __init__(self, stock, buy_price, quantity, date, ema, stop_loss=None, target=None):
        # @BCP - should be using the super().__init__()
        # Additionally, the stop_loss and target arguments in the __init__() method will never get passed into the
        # super().__init__()
        Stock_Lot_Long.__init__(self, stock, buy_price, quantity, date, stop_loss=None, target=None)
        self.ema_shorter, self.ema_longer = ema

    def get_stock_ema(self):
        return (self.ema_shorter, self.ema_longer)

# @BCP - The commented out code blocks should be removed - especially in a script that just defines things.

# tsla_long=Stock_Lot_Long("tsla",22,100,"20180101")
# tsla_short=Stock_Lot_Short("tsla", 22, 100, "20180101")
# print(tsla_short)


# stocks=["MSFT","IDEA.NS","HDFCBANK.NS"]
# period="6mo"

# @BCP - Follow PEP8
# @BCP - For period, there's too much chance for error.  There should be more stringent error checking.
# What happens if the user accidentally passed in a negative value?

# @BCP - Consideration - would you ever want the capability to pass in different periods for different stocks?

# @BCP - this should return an output and not export it directly.
def Create_Data(stocks, period):
    """

    A function used to create stock data in the format ".xlsx"
    Input parameters:
        stocks= A list of stock names(tickers)[Strings] for which you want the stock data. Eg.["MSFT","TSLA","IDEA.NS"]
        period= The time period for which you want the stock data for. Eg. 1 year,5 year, 1 week= "1y","5y","1w" (String)


    The ".xlsx" file contain the stock data with the columns :"Date","Open","High","Close","Low","Volume"
    The file is stored in the programme directory.



    """
    for stock in stocks:
        name = str(stock)

        ticker = yf.Ticker(name)
        data = ticker.history(period=period)
        data = data[["Open", 'High', "Close", "Low", "Volume"]]
        # @BCP - This export does not tell the user the destination directory and will force them to go search for it.
        data.to_excel(name + ".xlsx")


def Load_Data(stocks):
    """ Input a list of string of stocks,  Output a Dictionary of DataFrame objects of different stocks.

    The function searches for the stock_name.xlsx file in the programme directory to load the data.

    The function also calculates different indicator which are to be used during analysis.
    Eg. Exponential Moving averages for 9,21,25,50,100,200 days(EMA50,EMA100,EMA25)
        Moving Averages Convergence Divergence (MACD,EMA_MACD)
        Simple Moving Averages (SMA)
        Bollinger Bands(BOl_UP,BOL_LOW)
        Average Volume(AVG_VOLUME)

    All the indicators are stored in the stock_DataFrame.


    Input parameters:
        stocks=A list of stock names(tickers)[Strings] for which you want the stock data. Eg.["MSFT","TSLA","IDEA.NS"]


    Returns : An Dictionary of type DataFrame objects of different stocks with key as the stock_name.Eg {"MSFT":dataframe,"TSLA":dataframe}





    """
    # @BCP - This code is misleading because you aren't returning back a dataframe; in actuality, the code is
    # returning back a dict of dataframes.  Avoid Hungarian notation.
    stocks_data_frame = {}

    for stock in stocks:
        # name=str(stock)
        # if "." in name:
        #     name=name[0:name.index(".")]

        data = pd.read_excel(stock + ".xlsx", index_col=0)
        # @BCP - Repeated code blocks.
        # @BCP - Inconsistent code - EMA_MACD has underscore separating EMA.  However, the other ones do not have
        # underscores - ex. EMA50, EMA100, etc.
        data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()
        data["EMA100"] = data["Close"].ewm(span=100, adjust=False).mean()
        data['EMA9'] = data["Close"].ewm(span=9, adjust=False).mean()
        data['EMA21'] = data['Close'].ewm(span=21, adjust=False).mean()
        data['EMA200'] = data["Close"].ewm(span=200, adjust=False).mean()
        data['EMA25'] = data['Close'].ewm(span=25, adjust=False).mean()
        data["MACD"] = (data["Close"].ewm(span=12, adjust=False).mean()) - (
            data["Close"].ewm(span=26, adjust=False).mean())
        data["EMA_MACD"] = data["MACD"].ewm(span=9, adjust=False).mean()
        data["SMA20"] = data["Close"].rolling(window=20).mean()
        data["STD20"] = data["Close"].rolling(window=20).std()
        data["BOL_UP"] = data["SMA20"] + (2 * data["STD20"])
        data["BOL_LOW"] = data["SMA20"] - (2 * data["STD20"])
        # @BCP - Inconsistent code "Volume" vs "VOLUME"
        data["AVG_VOLUME"] = data["Volume"].rolling(window=10).mean()

        # @BCP - Inconsistent code.  The dataset should have the same column name with the stock.  This seems to be
        # duplicated since there is a key in the stocks_data_frame.
        data[str(stock)] = stock

        stocks_data_frame[str(stock)] = data

    return stocks_data_frame


# @BCP - This is a bad function name - it's too vague.
def Slice_Dataframe(dataframe, date):
    """


    Parameters
    ----------
    dataframe : TYPE DataFrame

    date : TYPE : Index(int)
        DESCRIPTION. Index of the date you want to the slice the data to.

    Returns
    -------
    A sliced DataFrame object with 15 days previous data from date. (Date also included in data)

    """
    # @BCP - the 15 days should not be hardcoded in.  It should be an argument passed into the function with a default
    # of 15 days.
    slice_data = dataframe.iloc[date - 15:date + 1, :]

    return slice_data


# Create_Data(stocks, period)
# stocks_data_frame=Load_Data(stocks)
# idea=(stocks_data_frame["IDEA.NS"])
# print(idea.tail())
# plt.plot(idea["Close"],label="close")
# plt.plot(idea["EMA50"],label="50")
# plt.plot(idea["EMA100"],label="100")
# plt.ylim(bottom=0)
# plt.legend(loc="best")

# slice_data=Slice_Dataframe(stocks_data_frame["IDEA.NS"],"20200504")
# print(slice_data)
# print(slice_data.iloc[:-1])
# print(slice_data.iat[-1,2])


class Portfolio(object):
    '''
    An object of type Portfolio which keeps track of objects "Stock_Lot_Long" , "Stock_Lot_Short","Stock_Lot_EMA" trades and current cash.

    Input parameters:
        long_cash= The amount of cash to be invested in long trades (Float)
        short_cash= The amount of cash kept as reserve against the short trades(Float)
        stock_lot_dict= Dict with keys "Long","Short","EMA" to store objects "Stock_Lot_Long","Stock_Lot_Short","Stock_Lot_EMA" trades in the appropiate key value (Dictionary)

    Functions:
        __init__(): Intialises all the neccessary variables for object "Portfolio":
            self.long_cash= Used to store long_cash(Float)
            self.short_cash=Used to store short_cash(Float)
            self.stock_lot_dict=Used to store stock_lot_dict(Dictionary)

        get_long_cash(): Returns self.long_cash


        get_short_cash(): Returns self.short_cash


        get_stock_lot_dict(): Returns self.stock_lot_dict


        add_stock_lot_long(Stock_Lot_Long): Adds new Object "Stock_Lot_Long" to "Long" key of self.stock_lot_dict


        remove_stock_lot_long(Stock_Lot_Long): Removes existing Object "Stock_Lot_Long" from "Long" key of self.stock_lot_dict



        add_stock_lot_short(Stock_Lot_Short): Adds new Object "Stock_Lot_Short" to "Short" key of self.stock_lot_dict



        remove_stock_lot_short(Stock_Lot_Short): Removes existing Object "Stock_Lot_Short" from "Short" key of self.stock_lot_dict



        add_stock_lot_short(Stock_Lot_EMA): Adds new Object "Stock_Lot_EMA" to "EMA" key of self.stock_lot_dict


        remove_stock_lot_short(Stock_Lot_EMA): Removes existing Object "Stock_Lot_EMA" from "EMA" key of self.stock_lot_dict


        add_long_cash(cash): Adds cash(Float) to self.long_cash


        remove_long_cash(cash): Removes cash(Float) from self.long_cash


        add_short_cash(cash): Adds cash(Float) from self.short_cash


        remove_short_cash(cash): Removes cash(Float) from self.short_cash


        get_long_worth(stocks_data_frame,date): Gets worth of stock_lot from "Long" and "EMA" key of self.stock_lot_dict
                                                Gets prices of current stock from stocks_data_frame on a particular date
                                                and then calculates total worth


        get_short_worth(stocks_data_frame,date): Gets worth of stock_lot from "Short" key of self.stock_lot_dict
                                                Gets prices of current stock from stocks_data_frame on a particular date
                                                and then calculates total worth.

        print_portfolio(): prints all the stock_lot objects in self.stock_lot_dict, self.long_cash and self.short_cash
    '''
    def __init__(self, long_cash, short_cash, stock_lot_dict):
        self.long_cash = float(long_cash)
        self.short_cash = float(short_cash)
        self.stock_lot_dict = stock_lot_dict

    def get_long_cash(self):
        return self.long_cash

    def get_short_cash(self):
        return self.short_cash

    def get_stock_lot_dict(self):

        return self.stock_lot_dict

    # @BCP - This should not have the EXACT same name as a class.
    def add_stock_lot_long(self, Stock_Lot_Long):
        self.stock_lot_dict["Long"].append(Stock_Lot_Long)

    def remove_stock_lot_long(self, Stock_Lot_Long):
        self.stock_lot_dict["Long"].remove(Stock_Lot_Long)

    def add_stock_lot_short(self, Stock_Lot_Short):
        self.stock_lot_dict["Short"].append(Stock_Lot_Short)

    def remove_stock_lot_short(self, Stock_Lot_Short):
        self.stock_lot_dict["Short"].remove(Stock_Lot_Short)

    def add_stock_lot_ema(self, Stock_Lot_EMA):
        self.stock_lot_dict["EMA"].append(Stock_Lot_EMA)

    def remove_stock_lot_ema(self, Stock_Lot_EMA):
        self.stock_lot_dict["EMA"].remove(Stock_Lot_EMA)

    def add_long_cash(self, cash):
        self.long_cash += cash

    def add_short_cash(self, cash):
        self.short_cash += cash

    def remove_long_cash(self, cash):
        self.long_cash -= cash

    def remove_short_cash(self, cash):
        self.short_cash -= cash

    def get_long_worth(self, stocks_data_frame, date):
        """


        Parameters
        ----------
        stocks_data_frame : A dictionary of dataframe objects of different stocks
            DESCRIPTION.
        date : TYPE  string of date : eg "20200205"
            DESCRIPTION.

        Returns
        -------
        Portiofolio worth according to the closing price of the stocks on the date

        """
        worth = 0
        for stock_lot in self.stock_lot_dict:
            if stock_lot != "Short":
                lot_list = self.stock_lot_dict[stock_lot]

                for lot in lot_list:
                    name = lot.get_stock_name()
                    quantity = lot.get_stock_quantity()
                    stock_data = stocks_data_frame[name]
                    stock_worth = stock_data.at[date, "Close"]
                    worth += stock_worth * quantity

        return worth

    def get_short_worth(self, stocks_data_frame, date):
        worth = 0
        stock_lot = self.stock_lot_dict["Short"]
        for lot in stock_lot:
            name = lot.get_stock_name()
            quantity = lot.get_stock_quantity()
            stock_data = stocks_data_frame[name]
            stock_worth = stock_data.at[date, "Close"]
            worth += stock_worth * quantity

        return worth

    def print_portfolio(self):
        print("---------------------------------")
        for stock_lot in self.stock_lot_dict:
            for lot in stock_lot:
                print(lot)

        print("Cash: " + str(self.get_long_cash()))

        print("---------------------------------")

# @BCP - This should never have been a class.  There's too many attributes and methods attached to it.
# This should be broken out into individual classes.
class Technical_analysis(object):
    '''
    An object of type Technical_analysis used to conduct technical analysis on stock_data_frame

    Input parameters:
        sliced_data= object of type DataFrame containing the data of the stock on which technical analysis is gonna be conducted.


    Functions:
        __init__(): Intialises neccassary object variables to be used by object later:
            self.data= Used to store copy of "sliced_data"
            self.index= Stores Index of self.data
            self.columns=List of columns of self.data
            self.highindex= Stores index of "High"
            self.closeindex= Stores index of "Close"
            self.lowindex= Stores index of "Low"
            self.openindex=Stores index of "Open"
            self.volumeindex=Stores index of "Volume"
            self.avg_volumeindex=Stores index of "AVG_VOLUME"
            self.ema50index=Stores index of "EMA50"
            self.ema100index=Stores index of "EMA100"
            self.ema200index=Stores index of "EMA200"
            self.ema25index=Stores index of "EMA25"
            self.ema9index=Stores index of "EMA9"
            self.ema21index=Stores index of "EMA21"
            self.macdindex=Stores index of "MACD"
            self.ema_macdindex=Stores index of "EMA_MACD"
            self.sma20index=Stores index of "SMA20"
            self.bol_upindex=Stores index of "BOL_UP"
            self.bol_lowindex=Stores index of "BOL_LOW"

        bullish_marubozu(): Checks for bullish marubozu candlestick pattern.

        bearish_marubozu(): Checks for bearish marubozu candlestick pattern.

        spining_top(): Checks for spinning top candlestick pattern

        doji(): Checks for doji candlestick pattern

        downtrend(): Checks if the market is in a downward trend.

        uptrend(): Checks if the market is in an upward trend.

        bullish_hammer() : Checks for bullish hammer candlestick pattern

        bearish_hanging_man(): Checks for bearish hanging man candlestick pattern

        bearish_shooting_star(): Checks for bearish shooting star candlestick pattern

        bullish_inverted_hammer(): Checks for bullish inverted hammer candlestick pattern

        bullish_engulfing(): Checks for bullish engulfing candlestick pattern

        bearish_engulfing(): Checks for bearish engulfing candlestick pattern

        bullish_piercing_pattern(): Checks for bullish piercing candlestick pattern

        bearish_dark_cloud_cover(): Checks for bearish dark cloud cover candlestick pattern

        bearish_harami() : Checks for bearish harami candlestick pattern

        bullish_harami() : Checks for bullish harami candlestick pattern

        bullish_morning_star(): Checks for bullish morning star candlestick pattern

        bearish_evening_star(): Checks for bearish evening star candlestick pattern

        volume(): Checks if the volume traded on that day is greater or smaller than Last 10 days average volume

        bullish_ema_50_100(): Checks if EMA 50 is greater than EMA 100

        bullish_ema_100_200(): Checks if EMA 100 is greater than EMA 200

        bullish_ema_25_50(): Checks if EMA 25 is greater than EMA 200

        bullish_ema_9_21(): Checks if EMA 9 is greater than EMA 21

        bullish_macd(): Checks if MACD is greater than EMA_MACD

        bearish_macd(): Checks if MACD is less than EMA_MACD

        bullish_bollinger(): Checks if price is less than BOL_LOW

        bearish_bollinger(): Checks if price is greater than BOL_UP


    '''
    def __init__(self, sliced_data):
        self.data = copy.deepcopy(sliced_data)

        # @BCP - This is unnecessary and brings additional cognitive load
        self.index = self.data.index
        self.columns = list(self.data.columns)
        self.highindex = self.columns.index("High")
        self.lowindex = self.columns.index("Low")
        self.openindex = self.columns.index("Open")
        self.closeindex = self.columns.index("Close")

        # @BCP This is inconsistent case
        self.volumeindex = self.columns.index("Volume")
        self.avg_volumeindex = self.columns.index("AVG_VOLUME")

        self.ema50index = self.columns.index("EMA50")
        self.ema100index = self.columns.index("EMA100")
        self.ema200index = self.columns.index("EMA200")
        self.ema25index = self.columns.index('EMA25')
        self.ema9index = self.columns.index('EMA9')
        self.ema21index = self.columns.index("EMA21")
        self.macdindex = self.columns.index("MACD")
        self.ema_macdindex = self.columns.index("EMA_MACD")
        self.sma20index = self.columns.index("SMA20")
        self.bol_upindex = self.columns.index("BOL_UP")
        self.bol_lowindex = self.columns.index("BOL_LOW")

    # @BCP - Notice the trend that all the bullish functions have repeated code setting the
    # buy_price, stop_loss, and pattern.  The same goes for the bear functions have repeated code setting the default
    # values for sell_price, stop_loss, pattern

    # @BCP - This is a bad method name - methods / functions should be verbs and not nouns
    def bullish_marubozu(self):
        buy_price = None
        stop_loss = None
        pattern = False
        # @BCP - This pattern gets used quite a bit - it would probably be better to put it in a function and make it
        # more readable.
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]

        if close >= open:

            if (open - low) <= (open * 0.01) and (close - high) <= (close * 0.01):
                pattern = True
                buy_price = close
                stop_loss = low

        return (pattern, buy_price, stop_loss)

    def bearish_marubozu(self):
        sell_price = None
        stop_loss = None
        pattern = False
        index = self.index[-1]
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
        if close <= open:

            if abs(open - high) <= (open * 0.01) and abs(close - low) <= (close * 0.01):
                pattern = True
                sell_price = close
                stop_loss = high

        return (pattern, sell_price, stop_loss)

    def spinning_top(self):
        buy_price = None
        stop_loss = None
        pattern = False
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
       

        if open >= close:
            uppershadow = abs(high - open)
            lowershadow = abs(close - low)

            if abs(open - close) <= 0.03 * close and abs(uppershadow - lowershadow) <= 0.03 * uppershadow:
                pattern = True
        else:
            uppershadow = abs(high - close)
            lowershadow = abs(open - low)

            if abs(open - close) <= 0.03 * open and abs(uppershadow - lowershadow) <= 0.03 * lowershadow:
                pattern = True

        return (pattern, buy_price, stop_loss)

    def doji(self):
        buy_price = None
        stop_loss = None
        pattern = False
        index = self.index[-1]
        open = self.data.at[index, "Open"]
        close = self.data.at[index, "Close"]

        if abs(open - close) <= 0.03 * open or abs(open - close) <= 0.03 * close:
            pattern = True

        return (pattern, buy_price, stop_loss)

    # @BCP - this is a bad method name because it's a noun and would make the user think this is an attribute and
    # not a method.  The same goes for uptrend and volume method names.

    # @BCP - just return the logic results
    def downtrend(self):
        pattern = False
        prev_day_close = self.data.iat[-2, self.closeindex]

        # @BCP - is this ten_day_close or nine_day_close?
        # The -10 should shift you to day 9.
        ten_day_close = self.data.iat[-10, self.closeindex]
        if ten_day_close > prev_day_close:

            if abs(ten_day_close - prev_day_close) >= 0.05 * ten_day_close:
                pattern = True

        return pattern

    def uptrend(self):
        pattern = False
        prev_day_close = self.data.iat[-2, self.closeindex]

        # @BCP - same comment as downtrend.
        ten_day_close = self.data.iat[-10, self.closeindex]

        if prev_day_close > ten_day_close:
            if abs(prev_day_close - ten_day_close) >= 0.05 * prev_day_close:
                pattern = True

        return pattern

    def bullish_hammer(self):
        buy_price = None
        stop_loss = None
        pattern = False
        index = self.index[-1]
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
        body = None
        lowershadow = None

        if open >= close:
            if abs(high - open) <= 0.02 * high:
                body = open - close
                lowershadow = close - low


        else:
            if abs(high - close) <= 0.02 * high:
                body = close - open
                lowershadow = open - low

        if lowershadow != None and body != None:
            if lowershadow >= 2 * body:
                check_downtrend = self.downtrend()
                if check_downtrend:
                    pattern = True
                    buy_price = close
                    stop_loss = low

        return (pattern, buy_price, stop_loss)

    def bearish_hanging_man(self):
        sell_price = None
        stop_loss = None
        pattern = False
        index = self.index[-1]
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
       
        body = None
        lowershadow = None

        if open >= close:
            if abs(high - open) <= 0.02 * high:
                body = open - close
                lowershadow = close - low


        else:
            if abs(high - close) <= 0.02 * high:
                body = close - open
                lowershadow = open - low

        if lowershadow != None and body != None:

            if lowershadow >= 2 * body:
                check_uptrend = self.uptrend()
                if check_uptrend:
                    pattern = True
                    sell_price = close
                    stop_loss = high

        return (pattern, sell_price, stop_loss)

    # @BCP - This is a good example of cons of repeating code.  Notice the inconsistency.  In other bearish methods,
    # it starts off with sell_price, stop_loss, pattern
    def bearish_shooting_star(self):
        pattern = False
        sell_price = None
        stop_loss = None
        index = self.index[-1]
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
       
        body = None
        uppershadow = None

        if open >= close:
            if abs(close - low) <= 0.02 * close:
                body = open - close
                uppershadow = high - open
        else:
            if abs(close - low) <= 0.02 * close:
                body = close - open
                uppershadow = high - close

        if uppershadow != None and body != None:
            if uppershadow >= 2 * body:
                check_uptrend = self.uptrend()
                if check_uptrend:
                    pattern = True
                    sell_price = close
                    stop_loss = high

        return (pattern, sell_price, stop_loss)

    # @BCP - same as the comment above.  Code inconsistency - in other bullish methods, it starts with
    #  buy_price, stop_loss, pattern
    def bullish_inverted_hammer(self):
        pattern = False
        buy_price = None
        stop_loss = None
        index = self.index[-1]
        high = self.data.iat[-1, self.highindex]
        open = self.data.iat[-1, self.openindex]
        close = self.data.iat[-1, self.closeindex]
        low = self.data.iat[-1, self.lowindex]
       
        body = None
        uppershadow = None

        if open >= close:
            if abs(close - low) <= 0.02 * close:
                body = open - close
                uppershadow = high - open
        else:
            if abs(close - low) <= 0.02 * close:
                body = close - open
                uppershadow = high - close

        if uppershadow != None and body != None:
            if uppershadow >= 2 * body:
                check_downtrend = self.downtrend()
                if check_downtrend:
                    pattern = True
                    buy_price = close
                    stop_loss = low

        return (pattern, buy_price, stop_loss)

    def bullish_engulfing(self):
        pattern = False
        buy_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_low = self.data.iat[-2, self.lowindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_low = self.data.iat[-1, self.lowindex]
        if current_day_low <= prev_day_low:
            low = current_day_low
        else:
            low = prev_day_low

        if prev_day_close <= prev_day_open:
            if current_day_open <= prev_day_close and current_day_close > current_day_open:
                prev_day_body = prev_day_open - prev_day_close
                current_body = current_day_close - current_day_open

                if current_body > prev_day_body:
                    check_downtrend = self.downtrend()
                    if check_downtrend:
                        pattern = True
                        buy_price = current_day_close
                        stop_loss = low
        return (pattern, buy_price, stop_loss)

    def bearish_engulfing(self):
        pattern = False
        sell_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_high = self.data.iat[-2, self.highindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_high = self.data.iat[-1, self.highindex]
        if current_day_high >= prev_day_high:
            high = current_day_high
        else:
            high = prev_day_high

        if prev_day_close >= prev_day_open:
            if current_day_open >= prev_day_close and current_day_close < current_day_open:
                prev_day_body = prev_day_close - prev_day_open
                current_day_body = current_day_close - current_day_open
                if current_day_body > prev_day_body:
                    check_uptrend = self.uptrend()
                    if check_uptrend:
                        pattern = True
                        sell_price = current_day_close
                        stop_loss = high
        return (pattern, sell_price, stop_loss)

    def bullish_piercing_pattern(self):
        pattern = False
        buy_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_low = self.data.iat[-2, self.lowindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_low = self.data.iat[-1, self.lowindex]
        if current_day_low <= prev_day_low:
            low = current_day_low
        else:
            low = prev_day_low

        if prev_day_close <= prev_day_open:
            if current_day_open <= prev_day_close and current_day_close > current_day_open:
                prev_day_body = prev_day_open - prev_day_close
                current_body = current_day_close - current_day_open

                if prev_day_body > current_body > 0.5 * prev_day_body:
                    check_downtrend = self.downtrend()
                    if check_downtrend:
                        pattern = True
                        buy_price = current_day_close
                        stop_loss = low
        return (pattern, buy_price, stop_loss)

    def bearish_dark_cloud_cover(self):
        pattern = False
        sell_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_high = self.data.iat[-2, self.highindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_high = self.data.iat[-1, self.highindex]
        if current_day_high >= prev_day_high:
            high = current_day_high
        else:
            high = prev_day_high

        if prev_day_close >= prev_day_open:
            if current_day_open >= prev_day_close and current_day_close < current_day_open:
                prev_day_body = prev_day_close - prev_day_open
                current_day_body = current_day_close - current_day_open
                if prev_day_body > current_day_body > 0.5 * prev_day_body:
                    check_uptrend = self.uptrend()
                    if check_uptrend:
                        pattern = True
                        sell_price = current_day_close
                        stop_loss = high
        return (pattern, sell_price, stop_loss)

    def bullish_harami(self):
        pattern = False
        buy_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_low = self.data.iat[-2, self.lowindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_low = self.data.iat[-1, self.lowindex]
        if current_day_low <= prev_day_low:
            low = current_day_low
        else:
            low = prev_day_low

        if prev_day_close < prev_day_open:
            if current_day_open > prev_day_close and current_day_close < prev_day_open:
                check_downtrend = self.downtrend()
                if check_downtrend:
                    pattern = True
                    buy_price = current_day_close
                    stop_loss = low
        return (pattern, buy_price, stop_loss)

    def bearish_harami(self):
        pattern = False
        sell_price = None
        stop_loss = None
        prev_day_open = self.data.iat[-2, self.openindex]
        prev_day_close = self.data.iat[-2, self.closeindex]
        prev_day_high = self.data.iat[-2, self.highindex]
        current_day_close = self.data.iat[-1, self.closeindex]
        current_day_open = self.data.iat[-1, self.openindex]
        current_day_high = self.data.iat[-1, self.highindex]
        if current_day_high >= prev_day_high:
            high = current_day_high
        else:
            high = prev_day_high

        if prev_day_close > prev_day_open:
            if current_day_open < prev_day_close and current_day_close > prev_day_open:
                check_uptrend = self.uptrend()
                if check_uptrend:
                    pattern = True
                    sell_price = current_day_close
                    stop_loss = high

        return (pattern, sell_price, stop_loss)

    def bullish_morning_star(self):
        pattern = False
        buy_price = None
        stop_loss = None

        # @BCP - too much cognitive load on the dates
        day1_close = self.data.iat[-3, self.closeindex]
        day1_open = self.data.iat[-3, self.openindex]
        day2_open = self.data.iat[-2, self.openindex]
        day2_close = self.data.iat[-2, self.closeindex]
        day1_low = self.data.iat[-3, self.lowindex]
        day2_low = self.data.iat[-2, self.lowindex]
        day3_low = self.data.iat[-1, self.lowindex]
        low = min(day1_low, day2_low, day3_low)
        check_downtrend = self.downtrend()
        if check_downtrend:

            if day1_close < day1_open:
                if day2_open < day1_close:

                    # @BCP - this is using extra rows of data - it grabs everything except the current day's pricing.
                    # However, doji and spinning top only need 1 day's worth of pricing
                    day2_data_slice = self.data.iloc[:-1, :]
                    day2_technical_analysis = Technical_analysis(day2_data_slice)
                    check_doji, _, _ = day2_technical_analysis.doji()
                    check_spining_top, _, _ = day2_technical_analysis.spinning_top()

                    if check_doji or check_spining_top:
                        day3_open = self.data.iat[-1, self.openindex]
                        day3_close = self.data.iat[-1, self.closeindex]
                        if day3_open > day2_close and day3_close > day1_open:
                            pattern = True
                            buy_price = day3_close
                            stop_loss = low
        return (pattern, buy_price, stop_loss)

    def bearish_evening_star(self):
        pattern = False
        sell_price = None
        stop_loss = None

        # @BCP - bad naming convention - this is cognitive overload to others because the variables
        # are not descriptive
        day1_close = self.data.iat[-3, self.closeindex]
        day1_open = self.data.iat[-3, self.openindex]
        day2_open = self.data.iat[-2, self.openindex]
        day2_close = self.data.iat[-2, self.closeindex]
        day1_high = self.data.iat[-3, self.highindex]
        day2_high = self.data.iat[-2, self.highindex]
        day3_high = self.data.iat[-1, self.highindex]
        low = min(day1_high, day2_high, day3_high)
        check_uptrend = self.uptrend()

        # @BCP - There are 4 nested if-statements - this is a code smell and should be refactored.
        if check_uptrend:

            if day1_close > day1_open:
                if day2_open > day1_close:
                    day2_data_slice = self.data.iloc[:-1, :]
                    day2_technical_analysis = Technical_analysis(day2_data_slice)
                    check_doji, _, _ = day2_technical_analysis.doji()
                    check_spining_top, _, _ = day2_technical_analysis.spinning_top()

                    if check_doji or check_spining_top:
                        day3_open = self.data.iat[-1, self.openindex]
                        day3_close = self.data.iat[-1, self.closeindex]
                        if day3_open < day2_close and day3_close < day1_open:
                            pattern = True
                            sell_price = day3_close
                            stop_loss = low
        return (pattern, sell_price, stop_loss)

    def volume(self):
        avg_volume = self.data.iat[-1, self.avg_volumeindex]
        today_volume = self.data.iat[-1, self.volumeindex]

        if today_volume >= avg_volume:
            return True

        return False

    # @BCP - These bullish EMA codes are all doing the same thing.
    def bullish_ema_50_100(self):
        ema50 = self.data.iat[-1, self.ema50index]
        ema100 = self.data.iat[-1, self.ema100index]
        pattern = False
        buy_price = None
        stop_loss = None

        if ema50 > ema100:
            pattern = True
            buy_price = self.data.iat[-1, self.closeindex]

        return (pattern, buy_price, stop_loss)

    def bullish_ema_9_21(self):
        ema9 = self.data.iat[-1, self.ema9index]
        ema21 = self.data.iat[-1, self.ema21index]
        pattern = False
        buy_price = None
        stop_loss = None

        if ema9 > ema21:
            pattern = True
            buy_price = self.data.iat[-1, self.closeindex]

        return (pattern, buy_price, stop_loss)

    def bullish_ema_25_50(self):
        ema50 = self.data.iat[-1, self.ema50index]
        ema25 = self.data.iat[-1, self.ema25index]
        pattern = False
        buy_price = None
        stop_loss = None

        if ema25 > ema50:
            pattern = True
            buy_price = self.data.iat[-1, self.closeindex]

        return (pattern, buy_price, stop_loss)

    def bullish_ema_100_200(self):
        ema200 = self.data.iat[-1, self.ema200index]
        ema100 = self.data.iat[-1, self.ema100index]
        pattern = False
        buy_price = None
        stop_loss = None

        if ema100 > ema200:
            pattern = True
            buy_price = self.data.iat[-1, self.closeindex]

        return (pattern, buy_price, stop_loss)

    def bullish_macd(self):
        macd = self.data.iat[-1, self.macdindex]
        ema_macd = self.data.iat[-1, self.ema_macdindex]
        pattern = False
        buy_price = None
        stop_loss = None

        if macd > ema_macd:
            pattern = True
            buy_price = self.data.iat[-1, self.closeindex]

        return (pattern, buy_price, stop_loss)

    def bearish_macd(self):
        macd = self.data.iat[-1, self.macdindex]
        ema_macd = self.data.iat[-1, self.ema_macdindex]
        pattern = False
        sell_price = None
        stop_loss = None

        if macd < ema_macd:
            pattern = True
            sell_price = self.data.iat[-1, self.closeindex]

        return (pattern, sell_price, stop_loss)

    def bullish_bollinger(self):
        pattern = False
        buy_price = None
        stop_loss = None

        bol_low = self.data.iat[-1, self.bol_lowindex]

        close = self.data.iat[-1, self.closeindex]

        if close <= bol_low:
            pattern = True
            buy_price = close

        return (pattern, buy_price, stop_loss)

    def bearish_bollinger(self):
        pattern = False
        sell_price = None
        stop_loss = None
        bol_up = self.data.iat[-1, self.bol_upindex]
        close = self.data.iat[-1, self.closeindex]

        if close >= bol_up:
            pattern = True
            sell_price = close

        return (pattern, sell_price, stop_loss)

# @BCP - the long_call and short_call methods are too long.  What happens if the user wants to add other types of
# analysis?  The user doesn't have the flexibility to do the analysis they want.
class Logic(object):
    def __init__(self, Technical_analysis, weights):
        self.tech_analysis = Technical_analysis
        self.weights = weights
        self.long = 0
        self.short = 0
        self.long_cash = None
        self.short_cash = None

    def long_call(self):

        bullish_marubozu = self.tech_analysis.bullish_marubozu()

        # @BCP - Should be if bullish_marubozu[0]
        if bullish_marubozu[0] == True:
            self.long += self.weights["bullish_marubozu"]
            # print("bullish marubozu")

        bullish_hammer = self.tech_analysis.bullish_hammer()
        if bullish_hammer[0] == True:
            self.long += self.weights["bullish_hammer"]
            # print("bullish hammer")

        bullish_inverted_hammer = self.tech_analysis.bullish_inverted_hammer()
        if bullish_inverted_hammer[0] == True:
            self.long += self.weights["bullish_inverted_hammer"]
            # print("bullish inverted hammer")

        bullish_engulfing = self.tech_analysis.bullish_engulfing()
        if bullish_engulfing[0] == True:
            self.long += self.weights["bullish_engulfing"]
            # print("bullish engulfing")

        bullish_piercing_pattern = self.tech_analysis.bullish_piercing_pattern()
        if bullish_piercing_pattern[0] == True:
            self.long += self.weights["bullish_piercing_pattern"]
            # print("bullish piercing pattern")

        bullish_harami = self.tech_analysis.bullish_harami()
        if bullish_harami[0] == True:
            self.long += self.weights["bullish_harami"]
            # print("bullish harami")

        bullish_morning_star = self.tech_analysis.bullish_morning_star()
        if bullish_morning_star[0] == True:
            self.long += self.weights["bullish_morning_star"]
            # print("bullish morning star")

        volume = self.tech_analysis.volume()
        if volume == True:
            self.long += self.weights["volume"]

        if 0.10 < self.long <= 0.20:
            self.long_cash = 0.05

        elif 0.20 < self.long <= 0.30:
            self.long_cash = 0.06

        elif 0.30 < self.long <= 0.40:
            self.long_cash = 0.07

        elif 0.40 < self.long <= 0.50:
            self.long_cash = 0.08

        elif 0.50 < self.long <= 0.60:
            self.long_cash = 0.09

        elif 0.60 < self.long <= 0.70:
            self.long_cash = 0.10

        elif 0.70 < self.long <= 0.80:
            self.long_cash = 0.11

        elif self.long > 0.80:
            self.long_cash = 0.15

        return self.long_cash

    def short_call(self):
        bearish_marubozu=self.tech_analysis.bearish_marubozu()
        if bearish_marubozu[0]==True:
            self.short +=self.weights["bearish_marubozu"]
            # print("bearish_marubozu")

        bearish_hanging_man = self.tech_analysis.bearish_hanging_man()
        if bearish_hanging_man[0] == True:
            self.short += self.weights["bearish_hanging_man"]
            # print("bearish_hanging_man")

        bearish_shooting_star = self.tech_analysis.bearish_shooting_star()
        if bearish_shooting_star[0] == True:
            self.short += self.weights["bearish_shooting_star"]
            # print("bearish_shooting_star")

        bearish_engulfing = self.tech_analysis.bearish_engulfing()
        if bearish_engulfing[0] == True:
            self.short += self.weights["bearish_engulfing"]
            # print("bearish_engulfing")

        bearish_dark_cloud_cover = self.tech_analysis.bearish_dark_cloud_cover()
        if bearish_dark_cloud_cover[0] == True:
            self.short += self.weights["bearish_dark_cloud_cover"]
            # print("bearish_dark_cloud_cover")

        bearish_harami = self.tech_analysis.bearish_harami()
        if bearish_harami[0] == True:
            self.short += self.weights["bearish_harami"]
            # print("bearish_harami")

        bearish_evening_star = self.tech_analysis.bearish_evening_star()
        if bearish_evening_star[0] == True:
            self.short += self.weights["bearish_evening_star"]
            # print("bearish_evening_star")

        volume = self.tech_analysis.volume()
        if volume == True:
            self.short += self.weights["volume"]

    # @BCP - This block of code is too repetitive.
    # Notice that this is in order - use bisect
    # No Else condition
        if 0 < self.short <= 0.20:
            self.short_cash = 0.05

        elif 0.20 < self.short <= 0.30:
            self.short_cash = 0.06

        elif 0.30 < self.short <= 0.40:
            self.short_cash = 0.07

        elif 0.40 < self.short <= 0.50:
            self.short_cash = 0.08

        elif 0.50 < self.short <= 0.60:
            self.short_cash = 0.09

        elif 0.60 < self.short <= 0.70:
            self.short_cash = 0.10

        elif 0.70 < self.short <= 0.80:
            self.short_cash = 0.11

        elif self.short > 0.80:
            self.short_cash = 0.15

        return self.short_cash

    # @BCP - inconsistent code - should return cash just like long_call, short_call.
    def ema_50_100(self):

        ema = self.tech_analysis.bullish_ema_50_100()
        cash = 0.10
        return (ema, cash)

    def ema_100_200(self):

        ema = self.tech_analysis.bullish_ema_100_200()
        cash = 0.20
        return (ema, cash)

    def ema_25_50(self):

        ema = self.tech_analysis.bullish_ema_25_50()
        cash = 0.10
        return (ema, cash)

    def ema_9_21(self):

        ema = self.tech_analysis.bullish_ema_9_21()
        cash = 0.05
        return (ema, cash)

    def bullish_bollinger(self):
        long_bollinger, _, _ = self.tech_analysis.bullish_bollinger()
        cash = 0.10
        return (long_bollinger, cash)

    def bullish_macd(self):
        long_macd, _, _ = self.tech_analysis.bullish_macd()
        cash = 0.10
        return (long_macd, cash)


# @BCP - this class is too bloated - too many methods.
class Backtest(object):
    def __init__(self, Portfolio, stocks_data_frame, weights, start_date, end_date):
        self.stocks_data_frame = stocks_data_frame
        self.portfolio = Portfolio
        self.start_date = start_date
        self.end_date = end_date
        self.weights = weights
        self.worth=[]
        self.date=[]
        self.intial_invest=self.portfolio.get_long_cash()
        self.total_invested=self.portfolio.get_long_cash()

        self.msft = self.stocks_data_frame["TCS.NS"]



        columns = list(self.msft.columns)
        self.columnsindex = {}
        self.columnsindex["Close"] = columns.index("Close")
        self.columnsindex["EMA50"] = columns.index("EMA50")
        self.columnsindex["EMA100"] = columns.index("EMA100")
        self.columnsindex["EMA200"] = columns.index("EMA200")
        self.columnsindex["EMA25"] = columns.index("EMA25")
        self.columnsindex["EMA9"] = columns.index("EMA9")
        self.columnsindex["EMA21"] = columns.index("EMA21")

        start_date_timestamp = pd.Timestamp(start_date)
        end_date_timestamp = pd.Timestamp(end_date)
        self.start_date_index = list(self.msft.index).index(start_date_timestamp)
        self.end_date_index = list(self.msft.index).index(end_date_timestamp)
        for a in self.msft.index:
            self.date.append(str(a.date()))

        # print(self.date)

    def check_current_stock(self, date):

        stock_lot_dict = self.portfolio.get_stock_lot_dict()

        for stock_lot in stock_lot_dict:
            if stock_lot == "Long":
                long_lot = stock_lot_dict["Long"]
                for lot in long_lot:

                    name = lot.get_stock_name()
                    target = lot.get_stock_target()
                    stop_loss = lot.get_stock_stop_loss()
                    price = self.stocks_data_frame[name].iat[date, self.columnsindex["Close"]]
                    sell_cash = None

                    if price >= target:
                        sell_cash = lot.get_stock_quantity() * price

                    elif price <= stop_loss:
                        sell_cash = lot.get_stock_quantity() * price

                    if sell_cash != None:
                        self.portfolio.add_long_cash(sell_cash)
                        self.portfolio.remove_stock_lot_long(lot)
            elif stock_lot == "Short":
                short_lot = stock_lot_dict["Short"]
                for lot in short_lot:
                    name = lot.get_stock_name()
                    target = lot.get_stock_target()
                    stop_loss = lot.get_stock_stop_loss()
                    price = self.stocks_data_frame[name].iat[date, self.columnsindex["Close"]]
                    sell_cash = None

                    if price <= target:
                        sell_cash = lot.get_stock_quantity() * price

                    elif price >= stop_loss:
                        sell_cash = lot.get_stock_quantity() * price

                    if sell_cash != None:
                        self.portfolio.remove_short_cash(sell_cash)
                        self.portfolio.remove_stock_lot_short(lot)
            elif stock_lot == "EMA":
                ema_lot = stock_lot_dict["EMA"]
                for lot in ema_lot:

                    name = lot.get_stock_name()
                    ema_shorter, ema_longer = lot.get_stock_ema()

                    ema_short_value = self.stocks_data_frame[name].iat[
                        date, self.columnsindex["EMA" + str(ema_shorter)]]
                    ema_long_value = self.stocks_data_frame[name].iat[date, self.columnsindex["EMA" + str(ema_longer)]]
                    sell_cash = None
                    price = self.stocks_data_frame[name].iat[date, self.columnsindex["Close"]]
                    if ema_short_value <= ema_long_value:
                        sell_cash = lot.get_stock_quantity() * price

                    if sell_cash != None:
                        self.portfolio.add_long_cash(sell_cash)
                        self.portfolio.remove_stock_lot_ema(lot)

    def long_short_stock(self, date):
        decision_dict={}
        price_dict={}

        for stock in self.stocks_data_frame:

            # @BCP - just dict.fromkeys
            # stock_dict = dict.fromkeys(['long_call', 'short_call', 'ema_50_100'], 0)
            stock_dict={}
            stock_dict["long_call"]=0
            stock_dict["short_call"]=0
            stock_dict["ema_50_100"]=0
            stock_dict["ema_100_200"]=0
            stock_dict["ema_25_50"]=0
            stock_dict["ema_9_21"]=0
            stock_dict["long_bollinger"]=0
            stock_dict["long_macd"]=0

            stock_data = self.stocks_data_frame[stock]
            stock_slice_data = Slice_Dataframe(stock_data, date)
            price = stock_data.iat[date, self.columnsindex["Close"]]
            stock_name = str(stock)
            price_dict[stock_name]=price
            tech_analysis = Technical_analysis(stock_slice_data)
            logic = Logic(tech_analysis, self.weights)
            long_call = logic.long_call()
            short_call = logic.short_call()

            ema50_100 = logic.ema_50_100()
            ema100_200 = logic.ema_100_200()
            ema25_50 = logic.ema_25_50()
            ema9_21 = logic.ema_9_21()
            long_macd = logic.bullish_macd()
            long_bollinger = logic.bullish_bollinger()

            # @BCP - Remove commented out code

            # @BCP - Notice how the first 2 conditions are different?  This is a result of
            # having inconsistent returns in Logic class.
            if long_call != None:
                stock_dict["long_call"]=long_call
                # long_cash = self.portfolio.get_long_cash() * long_call
                # long_quantity = math.floor(long_cash / price)
                #
                # cash_spent = long_quantity * price
                # if self.portfolio.get_long_cash() > 0 and long_quantity > 0:
                #     # print("bought long")
                #     lot = Stock_Lot_Long(stock_name, price, long_quantity, date)
                #     self.portfolio.add_stock_lot_long(lot)
                #     self.portfolio.remove_long_cash(cash_spent)
            if short_call != None:
                stock_dict["short_call"]=short_call
                # short_cash = self.portfolio.get_short_cash() * short_call
                # short_quantity = math.floor(short_cash / price)
                # cash_spent = short_quantity * price
                #
                # if self.portfolio.get_short_cash() > 1.10 * cash_spent and short_quantity > 0:
                #     # print("shorted stock")
                #     lot = Stock_Lot_Short(stock_name, price, short_quantity, date)
                #     self.portfolio.add_stock_lot_short(lot)
                #     self.portfolio.add_short_cash(cash_spent)

            if ema50_100[0]:
                stock_dict["ema_50_100"]=ema50_100[1]
                # cash= ema50_100[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                #
                #     if quantity > 0:
                #         lot = Stock_Lot_EMA(stock_name, price, quantity, date, [50, 100])
                #         self.portfolio.add_stock_lot_ema(lot)
                #         self.portfolio.remove_long_cash(cash_spent)
            if ema100_200[0]:
                stock_dict["ema_100_200"]=ema100_200[1]
                # cash = ema100_200[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                #
                #     if quantity > 0:
                #         lot = Stock_Lot_EMA(stock_name, price, quantity, date, [100, 200])
                #         self.portfolio.add_stock_lot_ema(lot)
                #         self.portfolio.remove_long_cash(cash_spent)
            if ema25_50[0]:
                stock_dict["ema_25_50"]=ema25_50[1]
                # cash = ema25_50[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                #
                #     if quantity > 0:
                #         lot = Stock_Lot_EMA(stock_name, price, quantity, date, [25, 50])
                #         self.portfolio.add_stock_lot_ema(lot)
                #         self.portfolio.remove_long_cash(cash_spent)
            if ema9_21[0]:
                stock_dict["ema_9_21"]=ema9_21[1]
                # cash = ema9_21[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                #
                #     if quantity > 0:
                #         lot = Stock_Lot_EMA(stock_name, price, quantity, date, [9, 21])
                #         self.portfolio.add_stock_lot_ema(lot)
                #         self.portfolio.remove_long_cash(cash_spent)
            if long_bollinger[0]:
                stock_dict["long_bollinger"]=long_bollinger[1]
                # cash = long_bollinger[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                # if quantity > 0:
                #     lot = Stock_Lot_Long(stock_name, price, quantity, date)
                #     self.portfolio.add_stock_lot_long(lot)
                #     self.portfolio.remove_long_cash(cash_spent)
            if long_macd[0]:
                stock_dict["long_macd"]=long_macd[1]
                # cash = long_macd[1]
                # if self.portfolio.get_long_cash() > 0:
                #     cash_spent = cash * self.portfolio.get_long_cash()
                #     quantity = math.floor(cash_spent / price)
                #     cash_spent = quantity * price
                # if quantity > 0:
                #     lot = Stock_Lot_Long(stock_name, price, quantity, date)
                #     self.portfolio.add_stock_lot_long(lot)
                #     self.portfolio.remove_long_cash(cash_spent)
            decision_dict[stock_name]=stock_dict
        return (decision_dict,price_dict)

    def decision_scheduler(self,decision_dict):
        long_list=[]
        short_list=[]
        for stock in decision_dict:
            for call in decision_dict[stock]:
                if call!="short_call":
                    if decision_dict[stock][call]!=0:
                        long_pair=(decision_dict[stock][call],str(stock)+"_"+str(call))
                        long_list.append(long_pair)
                else:
                    if decision_dict[stock][call]!=0:
                        short_pair=(decision_dict[stock][call],str(stock)+"_"+str(call))
                        short_list.append(short_pair)

        long_list.sort(reverse=True,key=lambda x:x[0])
        short_list.sort(reverse=True,key=lambda x:x[0])


        long_total=0
        final_long=[]
        for pair in long_list:
            if pair[0]+long_total<=1:
                final_long.append(pair)
                long_total+=pair[0]

            if long_total==1:
                break
        # print(final_long)

        return (final_long,short_list)

    def long_short_transcation(self,long_list,short_list, price_dict,date):
        total=0
        for pair in long_list:
            split=pair[1].split("_")
            # print(split)
            stock_name=str(split[0])
            price=price_dict[stock_name]
            long_call=pair[0]
            long_cash = self.portfolio.get_long_cash() * long_call
            long_quantity = math.floor(long_cash / price)
            cash_spent = long_quantity * price
            if self.portfolio.get_long_cash() > 0 and long_quantity > 0:
                total+=cash_spent
                if split[1]=="long":
                    lot = Stock_Lot_Long(stock_name, price, long_quantity, date)
                    self.portfolio.add_stock_lot_long(lot)
                else:
                    lot = Stock_Lot_EMA(stock_name, price, long_quantity, date, [int(split[2]),int(split[3])])
                    self.portfolio.add_stock_lot_ema(lot)

        self.portfolio.remove_long_cash(total)

        for pair in short_list:
            split=pair[1].split("_")
            # print(split)
            stock_name=str(split[0])
            price=price_dict[str(stock_name)]
            short_call=pair[0]
            short_cash = self.portfolio.get_short_cash() * short_call
            short_quantity = math.floor(short_cash / price)
            cash_spent = short_quantity * price
            if self.portfolio.get_short_cash() > 1.10 * cash_spent and short_quantity > 0:
                # print("shorted stock")
                lot = Stock_Lot_Short(stock_name, price, short_quantity, date)
                self.portfolio.add_stock_lot_short(lot)
                self.portfolio.add_short_cash(cash_spent)



    def run(self):
        i=1

        for date in range(self.start_date_index, self.end_date_index):
            if i%30==0:
                self.portfolio.add_long_cash(5000)
                self.total_invested +=5000
            print("The date today is "+str(self.date[date]))
            self.check_current_stock(date)
            decision_dict,price_dict =self.long_short_stock(date)
            long_list,short_list=self.decision_scheduler(decision_dict)
            self.long_short_transcation(long_list,short_list, price_dict, date)
            self.worth.append(self.get_worth(str(self.date[date]))+ self.portfolio.get_long_cash())
            i +=1


    def get_worth(self, date):
        return self.portfolio.get_long_worth(self.stocks_data_frame, date)

    def get_current_stocks(self):
        stock_dict = self.portfolio.get_stock_lot_dict()
        for stock_lot in stock_dict:
            print("-----------------------" + str(stock_lot) + "--------------------")
            for stock in stock_dict[stock_lot]:
                print(stock)


    def plot_worth(self):
        plt.style.use('ggplot')
        plt.figure()

        plt.plot(self.date[self.start_date_index:self.end_date_index],self.worth,label="Net Portfolio Worth")
        plt.xlabel("Date")
        plt.ylabel("Indian Rupees")
        plt.legend(loc="best")


    def summary(self):
        print("From Date :"+str(self.date[self.start_date_index])+"  To Date :"+str(self.date[self.end_date_index]))
        print("Base Investment "+str(self.intial_invest))
        print("Total money invested :"+str(self.total_invested))
        total_worth=self.get_worth(self.date[self.end_date_index])
        print("Total Worth of portfolio on "+self.date[self.end_date_index]+" : "+str(round(total_worth)))
        profit=total_worth-self.total_invested
        profit_per=(profit/self.total_invested)*100
        print("Profit "+str(round(profit)))
        print("Profit Percentage "+str(round(profit_per,2))+"%")












def intialize_variables(stocks,period,long_cash,short_cash):

    # Create_Data(stocks, period)
    stocks_data_frame = Load_Data(stocks)
    weights = {"bullish_marubozu": 0.1, "bullish_hammer": 0.4, "bullish_inverted_hammer": 0.4, "bullish_engulfing": 0.4,
               "bullish_piercing_pattern": 0.4}
    weights["bullish_harami"] = 0.4
    weights["bullish_morning_star"] = 0.4
    weights["volume"] = 0.00
    weights["bearish_marubozu"] = 0
    weights["bearish_hanging_man"] = 0.4
    weights["bearish_shooting_star"] = 0.4
    weights["bearish_engulfing"] = 0.4
    weights["bearish_dark_cloud_cover"] = 0.4
    weights["bearish_harami"] = 0.4
    weights["bearish_evening_star"] = 0.4
    intial_stocks = {}

    intial_stocks["Long"] = []
    intial_stocks["EMA"] = []
    intial_stocks["Short"] = []
    port=Portfolio(long_cash, short_cash, intial_stocks)




    return port,stocks_data_frame,weights





##############################################################################################################


stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "HINDUNILVR.NS", "BHARTIARTL.NS", "INFY.NS","JSWSTEEL.NS"]
period = "10y"
long_cash=200000
short_cash=100000
Create_Data(stocks, period)
port,stocks_data_frame,weights=intialize_variables(stocks, period, long_cash, short_cash)

backtest = Backtest(port, stocks_data_frame, weights, "20120102", "20171215")
backtest.run()
backtest.plot_worth()
backtest.summary()
# backtest.get_current_stocks()
# port.print_portfolio()
d=port.get_short_worth(stocks_data_frame, "20201215")
e=port.get_short_cash()
print(d)
print(e)
#checking editing