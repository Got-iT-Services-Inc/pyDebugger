#! /usr/bin/env python3
#############################################################
# Title: Python Debug Class                                 #
# Description: Wrapper around Debugging and Logging for any #
#              python class                                 #
# Version:                                                  #
#   * Version 1.0 03/28/2016 RC                             #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2016      #
#############################################################

class pyDebugger

    #Debug Function
    def Log(self, sString, endd="\n"):
        if self.__Debug == True:
            print(self.__class__.__name__ + ": " + sString,end=endd)
        if self.__LogToFile == True:
            try:
                with open("/var/log/" + self.__class__.__name__ + ".log", "a+") as logFile:
                    logFile.write(sString+endd)
                    logFile.close()
            except Exception as e:
                print(self.__class__.__name__ + "_Logging Error: " + str(e))
                
    def __init__(self,otherself, Debug, LogToFile):
        self.__Debug = Debug
        self.__LogToFile = LogToFile
        self.Log(otherself, "Starting Debugger, Debug="+ Debug + " LogToFile=" + LogToFile)
    
