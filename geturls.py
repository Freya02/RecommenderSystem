from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def geturllist(query,typeofurl):
    #searchlist=input("Search something:")
    results = google_search(query, "Key", "Key", num=10)
    urllist=[]
    requrls=[]
    for result in results:
        if typeofurl in result['link']:
            requrls.append(result['link'])
        else:
            urllist.append(result['link'])
    print(requrls)
    return requrls
