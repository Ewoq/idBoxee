    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

    parser.add_argument('-s','--search', help = 'The title of the tv-show to search for', type = str)
    parser.add_argument('-t','--tvshow', help = 'Title of the tv-show for the NFO file', type = str)
    parser.add_argument('-m','--movie', help = 'Title of the movie for the NFO file', type = str)
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
