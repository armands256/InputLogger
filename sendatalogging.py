import csv
import time


class Logger:
    """Class for logging keyboard and mouse clicks to file in CSV format
    """

    def __init__(self, path='./'):
        """
        Constructor that initializes logger. also csv file is created.
        File name of this file contains date and time this file is created following this format:
        data-<Day>-<Month>-<Year>-<Hour>-<Minute>-<Second>.csv
        Keyword arguments:
            path --  path for the log file to be created
        """
        self.path = path
        self.filename = "data-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".csv"
        self.open()

    def writeRow(self, data=[]):
        """
        Function that logs data.
            :param data: - list of data to be added at the end of the log file
        """
        try:
            self.datawriter.writerow(data)
        except ValueError:
            print("Exception while logging packet")
            print (ValueError)

    def release(self):
        """Closes csv file that was used for data logging"""
        self.outputfile.close()

    def open(self):
        """Open csv file that was used for data logging"""
        self.outputfile = open(self.path + self.filename, 'ab')
        self.datawriter = csv.writer(self.outputfile, delimiter=',')



