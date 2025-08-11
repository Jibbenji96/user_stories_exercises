def reading_time_estimator(text = None):
    if text == None:
        return "no word count given"
    
    elif type(text) != str:
        return "Text string must be provided."
    
    word_count = len(text.split())
    total_time = word_count / 200
    minutes = int(total_time)
    seconds = int((total_time - minutes) * 60)
    
    if minutes > 0:
        return f"{minutes} minutes" + (f" {seconds} seconds" if seconds else "")
    
    else:
        return f"{seconds} seconds"

