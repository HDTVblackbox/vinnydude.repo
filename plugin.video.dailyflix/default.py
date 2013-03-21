import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import urlresolver, os
from t0mm0.common.net import Net
#below you can add anything here just to keep your typing down to a minimum(shortcuts)
     
# i.e
icon = 'http://www.dailyflix.net/public/style_images/5_1_DF05.png'
divxicon = 'http://icons.iconarchive.com/icons/deleket/folder/256/Divx-Movies-icon.png'
hdicon = 'http://icons.iconarchive.com/icons/deleket/folder/256/My-Videos-icon.png'
flashicon = 'http://icons.iconarchive.com/icons/deleket/folder/256/Macromedia-Flash-icon.png'
searchicon = 'http://icons.iconarchive.com/icons/iconleak/atrous/256/search-icon.png'
#now look at the first addDir where i have written icon then look at second listed item i have put the url for image directly makes no odds how you do it !!
     
ADDON = xbmcaddon.Addon(id='plugin.video.dailyflix')
net = Net()
img = ''





def send_request_to_google_analytics(utm_url):
    ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    import urllib2
    try:
        req = urllib2.Request(utm_url, None,
                                    {'User-Agent':ua}
                                     )
        response = urllib2.urlopen(req).read()
    except:
        print ("GA fail: %s" % utm_url)         
    return response
       
def send_request_to_google_analytics(utm_url):
    ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    import urllib2
    try:
        req = urllib2.Request(utm_url, None,
                                    {'User-Agent':ua}
                                     )
        response = urllib2.urlopen(req).read()
    except:
        print ("GA fail: %s" % utm_url)         
    return response
  
     
ADDON = xbmcaddon.Addon(id='plugin.video.dailyflix')#<<<--------------
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
if os.path.exists(datapath)==False:
    os.mkdir(datapath) 
VISITOR_NUMBER = os.path.join(datapath, 'visitor')

if os.path.exists(VISITOR_NUMBER)==False:
    from random import randint
    txtfile = open(VISITOR_NUMBER,"w") 
    txtfile.write(str(randint(0, 0x7fffffff)))
    txtfile.close()

    
def send_request_to_google_analytics(utm_url):
    ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    import urllib2
    try:
        req = urllib2.Request(utm_url, None,
                                    {'User-Agent':ua}
                                     )
        response = urllib2.urlopen(req).read()
    except:
        print ("GA fail: %s" % utm_url)         
    return response
       
def GA(group,name):
        try:
            try:
                from hashlib import md5
            except:
                from md5 import md5
            from random import randint
            import time
            from urllib import unquote, quote
            from os import environ
            from hashlib import sha1
            VERSION = "4.2.8"
            VISITOR = open(VISITOR_NUMBER).read()
            PATH = "XBMC_NOTFILMON" #<---------------------------------           
            UATRACK="UA-38375410-1"#<-------------------------------
            website = "www.filmon.com"         
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            if name=="None":
                    utm_url = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
            else:
                if group=="None":
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
                else:
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+group+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
                                
            print "============================ POSTING ANALYTICS ============================"
            send_request_to_google_analytics(utm_url)
            
            if not group=="None":
                    utm_track = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmhn=" + quote(website) + \
                            "&utmt=" + "events" + \
                            "&utme="+ quote("5("+PATH+"*"+group+"*"+name+")")+\
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", "1", "1", VISITOR,"1","2"])
                    try:
                        print "============================ POSTING TRACK EVENT ============================"
                        send_request_to_google_analytics(utm_track)
                    except:
                        print "============================  CANNOT POST TRACK EVENT ============================" 

        except:
            print "================  CANNOT POST TO ANALYTICS  ================"

#      addDir('name','url','mode','iconimage','description') mode is where it tells the plugin where to go scroll to bottom to see where mode is
def CATEGORIES():
        addDir('HD Movies','structure_HD_movies',4,hdicon,'HD Movies')
        addDir('DivX Movies','structure_divx_movies',3,divxicon,'DivX Movies')
        addDir('Flash Movies','structure_flash_movies',6,flashicon,'Flash Movies')
        addDir('Search','structure_search(url)',10,searchicon,'Search')
        addDir('HD TV Shows','structure_HD_TV',7,icon,'HD TV Shows')
        addDir('DivX TV Shows','structure_divx_TV',8,icon,'DivX TV Shows')
        addDir('Flash TV Shows','structure_flash_TV',9,icon,'Flash TV Shows')
        setView('movies', 'default')
        #setView is setting the automatic view.....first is what section "movies"......second is what you called it in the settings xml  
                
def nextdirectory(url):
        link=OPEN_URL(url)
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,1,'','')
        match=re.compile('href="(.+?)" title=.+? class=.+?>(.+?)</a>').findall(link)
        for url, name in match:
                addDir(name,url,2,'','')
        match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,1,'','')

def nextdirectorytv(url):
        link=OPEN_URL(url)
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,14,'','')
        match=re.compile('href="(.+?)" title=.+? class=.+?>((?!(?:Posting)).+?)</a>').findall(link)
        for url, name in match:
                addDir(name,url,12,'','')
        match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,14,'','')

#def imdb(url):
#    print 'URL: '+url
#    req = urllib2.Request(url)
#    req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
#    response = urllib2.urlopen(req)
#    link=OPEN_URL(url)
#    response.close()
#    match=re.compile('''<a href='http://www.imdb.com/title/(.+?)/' class='bbc_url''').findall(link)
#    url = 'http://www.imdb.com/title/'+match[0]
#    req = urllib2.Request(url)
#    req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
#    response = urllib2.urlopen(req)
#    link=response.read()
#    response.close()
#    imdbinfo=re.compile('''<span class="star-box-rating-label">Your rating:</span>.<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id=".+?" data-ga-identifier="".title="(.+?) - click stars to rate">.+?<p itemprop="description">(.+?)</p>''', re.DOTALL).findall(link)
#    print 'BLERB: '+str(imdbinfo)
#    return imdbinfo
   
def nextdirectory_nextdirectory(url): #links
        link=OPEN_URL(url)
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,2,'','')
        #imdb(url)
        #blerb = str(imdb(url))
        #print 'BLURB TRACE: '+str(imdb(url))
        #listitem = xbmcgui.ListItem(str(imdb(url))
        link=link.replace("rel='external'>http://www.imdb.com",'')
        cover=re.compile('''<img src='(.+?)' alt='Posted Image' class='bbc_img' />''').findall(link)
        link=link.replace("rel='external'>http://i.imgur.com",'')
        link=link.replace("rel='external'>http://s11.postimage",'')
        link=link.replace("<a href='http://nfomation.net",'')
        match=re.compile('''<a href='(.+?)' class='.+?' title='.+?' rel='.+?'>http://w?w?w?\.?(.+?)\..+?</a''').findall(link)
        match.reverse()
        for url, name in match:
                addDir(name,url,5,cover[0],'')
        match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,2,'','')

def structure_search(url):
        url = 'http://www.dailyflix.net/index.php'
        req = urllib2.Request(url)
        req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            print 'MATCH: '+str(match)
            print 'URL: '+str(url)
            for name, url in match:
                addDir(name,url,11,'','')
        go = 'search'
        keyboard = xbmc.Keyboard('')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search = keyboard.getText()
            search = search.replace(' ','%20')
            print 'SEARCH: '+str(search)
            source = 'http://www.dailyflix.net/index.php?app=core&module=search&do=search&search_term='+search
            print 'SOURCE DONE : '+str(source)
            req = urllib2.Request(source)
            req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            linkz=response.read()
            response.close()
            results = re.compile("class='ipsBadge ipsBadge_lightgrey'>((?!(?:mHD))\b|Flash|HD|DivX|DivX TV|HD TV|Flash TV|\b)</a>.+?<h4><a href='(.+?)' title='View result'>(.+?)</a></h4>", re.DOTALL).findall(linkz)
            print 'RESULTS : '+str(results)
            for name, url, description in results:
                if "TV" in name:
                    addDir(description+' '+name,url,12,searchicon,'')
                else:
                    addDir(description+' '+name,url,2,searchicon,'')
            match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
            if match:
                print 'MATCH: '+str(match)
                print 'URL: '+str(url)
                for url, name in match:
                    addDir(url,name,11,'','')

        else:
            print 'FAILED SEARCH'

def structure_searchpages(url):
        print 'structure_searchpages'
        url = url.replace('amp;','')
        link=OPEN_URL(url)
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,11,'','')
        results = re.compile("class='ipsBadge ipsBadge_lightgrey'>((?!(?:mHD))\b|Flash|HD|DivX|DivX TV|HD TV|Flash TV|\b)</a>.+?<h4><a href='(.+?)' title='View result'>(.+?)</a></h4>", re.DOTALL).findall(link)
        print 'RESULTS : '+str(results)
        for name, url, description in results:
                if "TV" in name:
                    addDir(description+' '+name,url,12,searchicon,'')
                else:
                    addDir(description+' '+name,url,2,searchicon,'')
        match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, url in match:
                addDir(name,url,11,'','')

def structure_seasons(url):
        link=OPEN_URL(url)
        print 'URLz: '+url
        match=re.compile("<link rel='((?=(?:prev|first)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, urlz in match:
                addDir(name,urlz,12,'','')
        seasonone=re.compile('\.([sS]01|1)([eE][0-9][0-9])\.(...............)').findall(link)
        seasontwo=re.compile('\.([sS]02|2)([eE][0-9][0-9])\.(...............)').findall(link)
        seasonthree=re.compile('\.([sS]03|3)([eE][0-9][0-9])\.(...............)').findall(link)
        seasonfour=re.compile('\.([sS]04|4)([eE][0-9][0-9])\.(...............)').findall(link)
        seasonfive=re.compile('\.([sS]05|5)([eE][0-9][0-9])\.(...............)').findall(link)
        seasonsix=re.compile('\.([sS]06|6)([eE][0-9][0-9])\.(...............)').findall(link)
        seasonseven=re.compile('\.([sS]07|7)([eE][0-9][0-9])\.(...............)').findall(link)
        seasoneight=re.compile('\.([sS]08|8)([eE][0-9][0-9])\.(...............)').findall(link)
        img=re.compile("<span rel='lightbox'><img src='(.+?)' alt='Posted Image' class='bbc_img' />").findall(link)

        if img:
            pic=img[0]

        else:
            pic=''
        
        if seasonone:
                print 'Season One :'+str(seasonone)
                seasonone.sort()
                for season, episode, tail in seasonone:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasontwo:
                seasontwo.sort()
                for season, episode, tail in seasontwo:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasonthree:
                seasonthree.sort()
                for season, episode, tail in seasonthree:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasonfour:
                seasonfour.sort()
                for season, episode, tail in seasonfour:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasonfive:
                seasonfive.sort()
                for season, episode, tail in seasonfive:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasonsix:
                seasonsix.sort()
                for season, episode, tail in seasonsix:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasonseven:
                seasonseven.sort()
                for season, episode, tail in seasonseven:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        if seasoneight:
                seasoneight.sort()
                for season, episode, tail in seasoneight:
                    addDir(season+' '+episode,url,13,pic,season+episode+'.'+tail)

        match=re.compile("<link rel='((?=(?:next|last)).+?)' href='(.+?)'").findall(link) #prev/next page
        if match:
            for name, urlz in match:
                addDir(name,urlz,12,'','')

def structure_episodesone(url):
        link=OPEN_URL(url)
        print 'URL: '+url
        episodes=re.compile(description+"(.+?)((</div>|</a><br />.<br />))",re.DOTALL).findall(link)
        print 'EPISODES: '+str(episodes)
        links=re.compile("<a href='(.+?)' class='.+?' title='.+?' rel='.+?'>http://w?w?w?\.?(.+?)\..+?</a").findall(str(episodes))
        links.reverse()
        print 'LINKS: '+str(links)
        for url, name in links:
            addDir(name,url,5,'','')
        

def structure_divx_movies():
        addDir('Movies 2012-2013        A-Z','http://www.dailyflix.net/index.php?/forum/49-divx-2012-2013/',1,icon,'DivX Movies 2012-2013 - A-Z')
        addDir('Movies 2006-2011        A-Z','http://www.dailyflix.net/index.php?/forum/50-divx-2006-2011/',1,icon,'DivX Movies 2006-2011 - A-Z')
        addDir('Movies 2000-2005        A-Z','http://www.dailyflix.net/index.php?/forum/52-divx-2000-2005/',1,icon,'DivX Movies 2000-2005 - A-Z')
        addDir('Movies 1990-1999        A-Z','http://www.dailyflix.net/index.php?/forum/55-divx-1990-1999/',1,icon,'DivX Movies 1990-1999 - A-Z')
        addDir('Movies 1980-1989        A-Z','http://www.dailyflix.net/index.php?/forum/56-divx-1980-1989/',1,icon,'DivX Movies 1980-1999 - A-Z')
        addDir('Movies Pre 1979         A-Z','http://www.dailyflix.net/index.php?/forum/57-divx-1979-earlier/',1,icon,'DivX Movies Pre 1979  - A-Z')
        addDir('Movies 2012-2013        Recently Added','http://www.dailyflix.net/index.php?/forum/49-divx-2012-2013/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies 2012-2013 - Recently Added')
        addDir('Movies 2006-2011        Recently Added','http://www.dailyflix.net/index.php?/forum/50-divx-2006-2011/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies 2006-2011 - Recently Added')
        addDir('Movies 2000-2005        Recently Added','http://www.dailyflix.net/index.php?/forum/52-divx-2000-2005/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies 2000-2005 - Recently Added')
        addDir('Movies 1990-1999        Recently Added','http://www.dailyflix.net/index.php?/forum/55-divx-1990-1999/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies 1990-1999 - Recently Added')
        addDir('Movies 1980-1989        Recently Added','http://www.dailyflix.net/index.php?/forum/56-divx-1980-1989/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies 1980-1999 - Recently Added')
        addDir('Movies Pre 1979         Recently Added','http://www.dailyflix.net/index.php?/forum/57-divx-1979-earlier/page__sort_key__last_post__sort_by__Z-A',1,icon,'DivX Movies Pre 1979  - Recently Added')        
        setView('divxmovies', 'default')

def structure_HD_movies():
        addDir('Movies 2012-2013        A-Z','http://www.dailyflix.net/index.php?/forum/196-hd-movies-2012-2013/',1,icon,'HD Movies 2012-2013 - A-Z')
        addDir('Movies 2006-2011        A-Z','http://www.dailyflix.net/index.php?/forum/197-hd-movies-2006-2011/',1,icon,'HD Movies 2006-2011 - A-Z')
        addDir('Movies 2000-2005        A-Z','http://www.dailyflix.net/index.php?/forum/199-hd-movies-2000-2005/',1,icon,'HD Movies 2000-2005 - A-Z')
        addDir('Movies 1990-1999        A-Z','http://www.dailyflix.net/index.php?/forum/202-hd-movies-1990-1999/',1,icon,'HD Movies 1990-1999 - A-Z')
        addDir('Movies Pre 1989         A-Z','http://www.dailyflix.net/index.php?/forum/203-hd-movies-1989-earlier/',1,icon,'HD Movies Pre 1989  - A-Z')
        addDir('Movies 2012-2013        Recently Added','http://www.dailyflix.net/index.php?/forum/196-hd-movies-2012-2013/page__sort_key__last_post__sort_by__Z-A',1,icon,'HD Movies 2012-2013 - Recently Added')
        addDir('Movies 2006-2011        Recently Added','http://www.dailyflix.net/index.php?/forum/197-hd-movies-2006-2011/page__sort_key__last_post__sort_by__Z-A',1,icon,'HD Movies 2006-2011 - Recently Added')
        addDir('Movies 2000-2005        Recently Added','http://www.dailyflix.net/index.php?/forum/199-hd-movies-2000-2005/page__sort_key__last_post__sort_by__Z-A',1,icon,'HD Movies 2000-2005 - Recently Added')
        addDir('Movies 1990-1999        Recently Added','http://www.dailyflix.net/index.php?/forum/202-hd-movies-1990-1999/page__sort_key__last_post__sort_by__Z-A',1,icon,'HD Movies 1990-1999 - Recently Added')
        addDir('Movies Pre 1989         Recently Added','http://www.dailyflix.net/index.php?/forum/203-hd-movies-1989-earlier/page__sort_key__last_post__sort_by__Z-A',1,icon,'HD Movies Pre 1989  - Recently Added')        
        setView('divxmovies', 'default')

def structure_flash_movies():
        addDir('Movies 2012-2013        A-Z','http://www.dailyflix.net/index.php?/forum/64-flash-2012-2013/',1,icon,'Flash Movies 2012-2013 - A-Z')
        addDir('Movies 2006-2011        A-Z','http://www.dailyflix.net/index.php?/forum/65-flash-2006-2011/',1,icon,'Flash Movies 2006-2011 - A-Z')
        addDir('Movies 2000-2005        A-Z','http://www.dailyflix.net/index.php?/forum/66-flash-2000-2005/',1,icon,'Flash Movies 2000-2005 - A-Z')
        addDir('Movies 1990-1999        A-Z','http://www.dailyflix.net/index.php?/forum/67-flash-1990-1999/',1,icon,'Flash Movies 1990-1999 - A-Z')
        addDir('Movies 1980-1989        A-Z','http://www.dailyflix.net/index.php?/forum/210-flash-1980-1989/',1,icon,'Flash Movies 1980-1999 - A-Z')
        addDir('Movies Pre 1979         A-Z','http://www.dailyflix.net/index.php?/forum/68-flash-1979-earlier/',1,icon,'Flash Movies Pre 1979  - A-Z')
        addDir('Movies 2012-2013        Recently Added','http://www.dailyflix.net/index.php?/forum/64-flash-2012-2013/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies 2012-2013 - Recently Added')
        addDir('Movies 2006-2011        Recently Added','http://www.dailyflix.net/index.php?/forum/65-flash-2006-2011/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies 2006-2011 - Recently Added')
        addDir('Movies 2000-2005        Recently Added','http://www.dailyflix.net/index.php?/forum/66-flash-2000-2005/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies 2000-2005 - Recently Added')
        addDir('Movies 1990-1999        Recently Added','http://www.dailyflix.net/index.php?/forum/67-flash-1990-1999/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies 1990-1999 - Recently Added')
        addDir('Movies 1980-1989        Recently Added','http://www.dailyflix.net/index.php?/forum/210-flash-1980-1989/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies 1980-1999 - Recently Added')
        addDir('Movies Pre 1979         Recently Added','http://www.dailyflix.net/index.php?/forum/68-flash-1979-earlier/page__sort_key__last_post__sort_by__Z-A',1,icon,'Flash Movies Pre 1979  - Recently Added')        
        setView('divxmovies', 'default')

def structure_HD_TV():
        addDir('General TV                      A-Z','http://www.dailyflix.net/index.php?/forum/35-hd-general-tv/page__sort_key__title__sort_by__A-Z',14,icon,'HD General TV - A-Z')
        addDir('Comedy                          A-Z','http://www.dailyflix.net/index.php?/forum/37-hd-comedy/page__sort_key__title__sort_by__A-Z',14,icon,'HD Comedy - A-Z')
        addDir('Sci-Fi/Fantasy/Horror   A-Z','http://www.dailyflix.net/index.php?/forum/38-hd-sci-fi-fantasy-horror/page__sort_key__title__sort_by__A-Z',14,icon,'HD Sci-Fi/Fantasy/Horror - A-Z')
        addDir('Cartoons                        A-Z','http://www.dailyflix.net/index.php?/forum/39-hd-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'HD Cartoons - A-Z')
        addDir('Kids TV and Cartoons    A-Z','http://www.dailyflix.net/index.php?/forum/40-hd-kids-tv-shows-and-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'HD Kids TV and Cartoons - A-Z')
        addDir('General TV                      Recently Added','http://www.dailyflix.net/index.php?/forum/35-hd-general-tv/page__sort_key__last_post__sort_by__Z-A',14,icon,'HD General TV - Recently Added')
        addDir('Comedy                          Recently Added','http://www.dailyflix.net/index.php?/forum/37-hd-comedy/page__sort_key__last_post__sort_by__Z-A',14,icon,'HD Comedy - Recently Added')
        addDir('Sci-Fi/Fantasy/Horror   Recently Added','http://www.dailyflix.net/index.php?/forum/38-hd-sci-fi-fantasy-horror/page__sort_key__last_post__sort_by__Z-A',14,icon,'HD Sci-Fi/Fantasy/Horror - Recently Added')
        addDir('Cartoons                        Recently Added','http://www.dailyflix.net/index.php?/forum/39-hd-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'HD Cartoons - Recently Added')
        addDir('Kids TV and Cartoons    Recently Added','http://www.dailyflix.net/index.php?/forum/40-hd-kids-tv-shows-and-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'HD Kids TV and Cartoons - Recently Added')

def structure_divx_TV():
        addDir('General TV                      A-Z','http://www.dailyflix.net/index.php?/forum/28-divx-general-tv/page__sort_key__title__sort_by__A-Z',14,icon,'DivX General TV - A-Z')
        addDir('Comedy                          A-Z','http://www.dailyflix.net/index.php?/forum/30-divx-comedy/page__sort_key__title__sort_by__A-Z',14,icon,'DivX Comedy - A-Z')
        addDir('Sci-Fi/Fantasy/Horror   A-Z','http://www.dailyflix.net/index.php?/forum/31-divx-sci-fi-fantasy-horror/page__sort_key__title__sort_by__A-Z',14,icon,'DivX Sci-Fi/Fantasy/Horror - A-Z')
        addDir('Cartoons                        A-Z','http://www.dailyflix.net/index.php?/forum/32-divx-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'DivX Cartoons - A-Z')
        addDir('Kids TV and Cartoons    A-Z','http://www.dailyflix.net/index.php?/forum/33-divx-kids-tv-shows-and-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'DivX Kids TV and Cartoons - A-Z')
        addDir('General TV                      Recently Added','http://www.dailyflix.net/index.php?/forum/28-divx-general-tv/page__sort_key__last_post__sort_by__Z-A',14,icon,'DivX General TV - Recently Added')
        addDir('Comedy                          Recently Added','http://www.dailyflix.net/index.php?/forum/30-divx-comedy/page__sort_key__last_post__sort_by__Z-A',14,icon,'DivX Comedy - Recently Added')
        addDir('Sci-Fi/Fantasy/Horror   Recently Added','http://www.dailyflix.net/index.php?/forum/31-divx-sci-fi-fantasy-horror/page__sort_key__last_post__sort_by__Z-A',14,icon,'DivX Sci-Fi/Fantasy/Horror - Recently Added')
        addDir('Cartoons                        Recently Added','http://www.dailyflix.net/index.php?/forum/32-divx-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'DivX Cartoons - Recently Added')
        addDir('Kids TV and Cartoons    Recently Added','http://www.dailyflix.net/index.php?/forum/33-divx-kids-tv-shows-and-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'DivX Kids TV and Cartoons - Recently Added')

def structure_flash_TV():
        addDir('General TV                      A-Z','http://www.dailyflix.net/index.php?/forum/42-flashflv-general-tv/page__sort_key__title__sort_by__A-Z',14,icon,'Flash General TV - A-Z')
        addDir('Comedy                          A-Z','http://www.dailyflix.net/index.php?/forum/44-flashflv-comedy/page__sort_key__title__sort_by__A-Z',14,icon,'Flash Comedy - A-Z')
        addDir('Sci-Fi/Fantasy/Horror   A-Z','http://www.dailyflix.net/index.php?/forum/45-flashflv-sci-fi-fantasy-horror/page__sort_key__title__sort_by__A-Z',14,icon,'Flash Sci-Fi/Fantasy/Horror - A-Z')
        addDir('Cartoons                        A-Z','http://www.dailyflix.net/index.php?/forum/46-flashflv-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'Flash Cartoons - A-Z')
        addDir('Kids TV and Cartoons    A-Z','http://www.dailyflix.net/index.php?/forum/47-flashflv-kids-tv-shows-and-cartoons/page__sort_key__title__sort_by__A-Z',14,icon,'Flash Kids TV and Cartoons - A-Z')
        addDir('General TV                      Recently Added','http://www.dailyflix.net/index.php?/forum/42-flashflv-general-tv/page__sort_key__last_post__sort_by__Z-A',14,icon,'Flash General TV - Recently Added')
        addDir('Comedy                          Recently Added','http://www.dailyflix.net/index.php?/forum/44-flashflv-comedy/page__sort_key__last_post__sort_by__Z-A',14,icon,'Flash Comedy - Recently Added')
        addDir('Sci-Fi/Fantasy/Horror   Recently Added','http://www.dailyflix.net/index.php?/forum/45-flashflv-sci-fi-fantasy-horror/page__sort_key__last_post__sort_by__Z-A',14,icon,'Flash Sci-Fi/Fantasy/Horror - Recently Added')
        addDir('Cartoons                        Recently Added','http://www.dailyflix.net/index.php?/forum/46-flashflv-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'Flash Cartoons - Recently Added')
        addDir('Kids TV and Cartoons    Recently Added','http://www.dailyflix.net/index.php?/forum/47-flashflv-kids-tv-shows-and-cartoons/page__sort_key__last_post__sort_by__Z-A',14,icon,'Flash Kids TV and Cartoons - Recently Added')


def PLAY(name,url):
        GA("None","Second Directory")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
        #print name
        listitem.setInfo("Video", infoLabels={ "Title": name})
        listitem.setProperty('mimetype', 'video/x-msvideo')
        listitem.setProperty('IsPlayable', 'true')
        media = urlresolver.HostedMediaFile(url)
        source = media
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        #link=OPEN_URL(url)
        #cover=re.compile('''<img src='(.+?)' alt='Posted Image' class='bbc_img' />''').findall(link)
        addDir('','','','','')
     
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    link = str(link)
    return link
     
     
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                   
        return param
     
# this is the listing of the items
     
def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "PlotOutline": description} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
#same as above but this is addlink this is where you pass your playable content so you dont use addDir you use addLink "url" is always the playable content        
def addLink(name,url,iconimage,description):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
     
           
#below tells plugin about the views                
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true)
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                         

                 
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
send=None

     

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
     
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
       
           
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
           
elif mode==1:
        print "nextdirectory "+url
        nextdirectory(url)
           
elif mode==2:
        print "nextdirectory_nextdirectory "+url
        nextdirectory_nextdirectory(url)

elif mode==3:
        print "structure_divx_movies "
        structure_divx_movies()

elif mode==4:
        print "structure_HD_movies "
        structure_HD_movies()
        
elif mode==5:
        print "PLAY "+url
        PLAY(name,url)

elif mode==6:
        print "structure_flash_movies "+url
        structure_flash_movies()

elif mode==7:
        print ""+url
        structure_HD_TV()

elif mode==8:
        print ""+url
        structure_divx_TV()

elif mode==9:
        print ""+url
        structure_flash_TV()

elif mode==10:
        print "structure_search "+url
        structure_search(url)

elif mode==11:
        print "structure_searchpages "+url
        structure_searchpages(url)

elif mode==12:
        print "structure_seasons "+url
        structure_seasons(url)

elif mode==13:
        print "structure_episodes "
        structure_episodesone(url)

elif mode==14:
        print "next directory tv"+url
        nextdirectorytv(url)
     
elif mode == 'play':
    stream_url = urlresolver.HostedMediaFile(url).resolve()
    if stream_url:
        xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(stream_url)
        addon.add_directory({'mode': 'play', 'url': url}, {'title': 'Play Again'})
           
     
           
xbmcplugin.endOfDirectory(int(sys.argv[1]))
