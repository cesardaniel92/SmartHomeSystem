
import wifi
import urllib2
from wifi import Cell,Scheme
import wifi.subprocess_compat as subprocess
def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    #return False


def FindFromSavedList(ssid):
    
    cell = wifi.Scheme.find('wlan0', ssid)

    if cell:
        return cell

    #return False


def Connect(ssid, password):
    
   
    
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell,password)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    #return False


def Add(cell, password):
    

      
      scheme = wifi.Scheme.for_cell('wlan0', ssid,cell, password)
      scheme.save()
      return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    #return False

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        print(' Connected to the wifi ')
    except urllib2.URLError as err:
      print(' DisConnected from wifi ')


if __name__ == '__main__':
    
    # Search WiFi and return WiFi list
    print Search()
    ssid = raw_input("network ssid : ")
    password = raw_input(" network password : ")
    
   
    print Connect(ssid.encode('utf8'),password.encode('utf8'))
    print internet_on()
    
  

