def json_to_string(obj):
    '''
    inputs an json object from crawler, return the formatted output.
    '''
    string='#### From @%s At %s ####\n%s\n'%(obj['user']['screen_name'],obj['created_at'],obj['text'])
    return string