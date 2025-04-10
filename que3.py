def error(error_message):
    return error_message.strip('* ').strip()
result=error("** input message **")
print(result)