def make_tvshow(title, id):
    file = open('tvshow.nfo', 'w')
    file.write('<tvshow>\n<title>' + title + '</title>\n<id>' + str(id) + '</id>\n</tvshow>')
    file.close()
    print 'tvshow.nfo saved with title '+ title + ' and id ' + str(id)
    
def search_tvdb(searchString):

    print('Searching...\n')
    urlstring = 'http://thetvdb.com/api/GetSeries.php?seriesname=<' + searchString + '>'
    response = urllib2.urlopen(urlstring)
    
    data = response.read()
    tree = XML(data)
    
    for allSeries in tree.findall('Series'):
        seriesName = allSeries.find('SeriesName').text
        seriesid = allSeries.find('seriesid').text
        try:
            firstAired = allSeries.find('FirstAired').text
        except AttributeError:
            print '%s, id: %s' % (seriesName, seriesid)
        else:
            print '%s, aired: %s, id: %s' % (seriesName, firstAired, seriesid)

if __name__ == '__main__':
    import argparse
    import re
    import urllib2
    from xml.etree.ElementTree import XML
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-s','--search', help = 'List the name of the tv-show', type = str)
    parser.add_argument('-t','--tvshow', help = 'List the name of the tv-show', type = str)
    parser.add_argument('-m','--movie', help = 'List the name of the movie', type = str)
    parser.add_argument('--id', help = 'The id of the tv-show or movie', type = int)

    args = parser.parse_args()

    if args.search:
        search = re.compile(' ').sub('%20', args.search) # Replaces spaces with %20 in the search string for the html call
        search_tvdb(search)
        
    if args.tvshow and args.id:
        make_tvshow(args.tvshow, args.id)
        
    if args.movie:
        print('movie: ' + args.movie)

    # <tvshow>
    # <title>MythBusters</title>
    # <id>73388</id>
    # </tvshow>
