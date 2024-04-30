import os
import sys

class CustomException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "Error Occured in Python Script Name [{0}] Line Number [{1}] Error Message [{2}]".format(
            self.file_name,self.line_no,str(self.error_message))
        
    