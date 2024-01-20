#!/usr/local/bin/env groovy
def urlFromEnvironment = System.getenv('config_page')

def logFile = new File("/output.log")
logFile.append(urlFromEnvironment)

def storm2.base.url = urlFromEnvironment
def grails.serverUrl = urlFromEnvironment