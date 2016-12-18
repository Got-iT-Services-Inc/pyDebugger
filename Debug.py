#! /usr/bin/env python3
#############################################################
# Title: Python Debug Class                                 #
# Description: Wrapper around Debugging and Logging for any #
#              python class                                 #
# Version:                                                  #
#   * Version 1.0 03/28/2016 RC                             #
#   * Version 1.1 12/16/2016 RC				    #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2016      #
#############################################################

from datetime import datetime

class pyDebugger:

    #Debug Function
    def Log(self, sString, endd="\n",PrintName=True, DebugLevel="ALL"):
        sCN = ""

        if DebugLevel in self.__DebugLevel or "ALL" in self.__DebugLevel:
            if PrintName == True:
                if self.__PrintDebugLevel == True:
                    sCN += "[" + DebugLevel + "] "
                sCN += self.ClassName + ":"
            if self.__Debug == True:
                print(sCN + sString,end=endd)
            if self.__LogToFile == True:
                try:
                    with open("/var/log/" + self.ClassName + ".log", "a+") as logFile:
                        logFile.write(str(datetime.now()) + " " + sCN + sString+endd)
                        logFile.close()
                except Exception as e:
                    print(self.ClassName + "_Logging Error: " + str(e))

    def SetDebugLevel(self,DebugLevel):
        if "," in DebugLevel:
            self.__DebugLevel = DebugLevel.split(",")
        else:
            self.__DebugLevel = DebugLevel

    def __init__(self,otherSelf, Debug, LogToFile, DebugLevel="ALL,NONE", PrintDebugLevel=True):
        self.SetDebugLevel(DebugLevel)
        self.__PrintDebugLevel = PrintDebugLevel
        self.__Debug = Debug
        self.__LogToFile = LogToFile
        self.ClassName = otherSelf.__class__.__name__
        self.Log("Starting Debugger, Debug="+ str(Debug) + " LogToFile=" + str(LogToFile))
