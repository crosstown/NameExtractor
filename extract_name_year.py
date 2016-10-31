import os
import re
import sys
import string


def exteract_year(filedata):
    year_match = re.search('Popularity\sin\s(\d\d\d\d)', filedata)
    tuples = re.findall('<td>(\d+)</td>\s<td>(\w+)</td><td>(\d+,\d+|\d+)</td>\n\s<td>(\w+)</td>\n<td>(\d+,\d+|\d+)</td>', filedata)
    return year_match.group(1), tuples

def openfile(filename):
    print os.path.exists(filename)
    try:
        htmlfile = open(filename,'r')
        filedata = htmlfile.read()
        htmlfile.close()
    except IOError:
        print "Error: can\'t find file or read data"
    return filedata

def process(archive):  
    
      
    filedata = openfile(archive)

    year, kidsdata = exteract_year(filedata)
    ranks=[]
    boysnames=[]
    boysfreq=[]
    girlsnames=[]
    girlsfreq=[]
    quan=[]
    per=0.0
    
    f_boys=0.0
    
    for kiddata in kidsdata:
        ranks.append(int(kiddata[0]))
        boysnames.append(kiddata[1])
        boysfreq.append(int(kiddata[2].replace(',', '')))
        girlsnames.append(kiddata[3])
        girlsfreq.append(int(kiddata[4].replace(',', '')))
        
        processBoys(ranks, boysnames, boysfreq, year)
        
        processGirls(ranks, girlsnames, girlsfreq, year)
        
   
    pass
def processBoys(position,boysnames,boysfreq, year):    
    filename1 = 'top_boy_names_'+str(year)+'.txt'
    total=0.0
    sys.stdout = open(filename1, 'w')
    for i in range(0,len(boysfreq)):
        total +=  (boysfreq[i])
    
    print 'Ranking'.rjust(12), 'Name'.rjust(16)+"\t\t",'Percentage'.rjust(12)
    print '-------------------------------------------------------------'
    for j in range(0,len(boysfreq)):
        
      
      per = (float(boysfreq[j])/total)*100.00
      print str(position[j]).rjust(8), boysnames[j].rjust(20)+"\t\t", str(format(per,'0.3f').rjust(10))
      
    
   
 
    pass
def processGirls(position,girlNames,girlFreq, year):    
    filename2 = 'top_girl_names_'+ str(year)+'.txt'
    total=0.0
    sys.stdout = open(filename2, 'w')
    for i in range(0,len(girlFreq)):
        total +=  (girlFreq[i])
   
    print 'Ranking'.rjust(12), 'Name'.rjust(16)+"\t\t",'Percentage'.rjust(12)
    print '-------------------------------------------------------------'
    for j in range(0,len(girlFreq)):
        
  
      per = (float(girlFreq[j])/total)*100.00
      print str(position[j]).rjust(8), girlNames[j].rjust(20)+"\t\t", str(format(per, '0.3f')).rjust(10)

def main():
    args = sys.argv[1:]
    if not args:
        print 'Usage: python extract_names_year.py [file_name]'
        
        sys.exit(1)
        
        ''' one arg '''
    filepath = args[0]
    
    
    process(filepath)
    pass
    
    
    
    
        

if __name__ == '__main__':
    main()
    pass

    
