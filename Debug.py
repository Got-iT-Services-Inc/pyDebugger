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

class pyDebugger:

    #Debug Function
    def Log(self, sString, endd="\n"):
        if self.__Debug == True:
            print(self.ClassName + ": " + sString,end=endd)
        if self.__LogToFile == True:
            try:
                with open("/var/log/" + self.ClassName + ".log", "a+") as logFile:
                    logFile.write(sString+endd)
                    logFile.close()
            except Exception as e:
                print(self.ClassName + "_Logging Error: " + str(e))
                
    def __init__(self,otherSelf, Debug, LogToFile):
        self.__Debug = Debug
        self.__LogToFile = LogToFile
        self.ClassName = otherSelf.__class__.__name__
        self.Log("Starting Debugger, Debug="+ str(Debug) + " LogToFile=" + str(LogToFile))
    
