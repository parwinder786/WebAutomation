from datetime import datetime
import logging

class CommonFunction:

    @staticmethod
    def datetimediff(found_lineL,found_lineL1):
        try:
            ab = found_lineL.split()
            cd = found_lineL1.split()
            edt0 = ab[1][1:19]
            sdt0 = cd[1][1:19]

            edt = edt0.replace('T', ' ')
            sdt = sdt0.replace('T', ' ')

            d1 = datetime.strptime(edt, "%Y-%m-%d %H:%M:%S")
            d2 = datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S")
            diff0 = d1 - d2
            diff = diff0.days
            return diff
        except:
            print('function not working')

