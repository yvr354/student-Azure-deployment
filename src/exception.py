import sys
from src.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ##this will give you three information ,first two i am not intrested i last information that exc_tb 
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number[{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

    


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_details)

    def __str__(self):
        return self.error_message



         








    ##exc will show on which file exceptiom occur and which line exception occur store in the exc_tb varible