class PipelineMonitor:
    def __init__(self):
        self.logger.log(Log.DEBUG, "PipelineMonitor:__init__")

    def isRunning(self):
        self.logger.log(Log.DEBUG, "PipelineMonitor:isRunnable")
        return True

    def stopPipeline(self):
        self.logger.log(Log.DEBUG, "PipelineMonitor:stopPipeline")

    def handleEvent(self, event):
        self.logger.log(Log.DEBUG, "PipelineMonitor:handleEvent")

    def handleFailure(self):
        self.logger.log(Log.DEBUG, "PipelineMonitor:handleFailure")

