__author__ = 'rocky'
# date_pool=['20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
date_pool=['20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327'];
grad_size=18
county=0
for date in date_pool:
    print date
    file=open(date+'StandAngCount.csv')
    File=open(date+'StandGrid.csv','wt')
    dence={}
    dencity_cluster=[0,0,0,0,0,0,0,0,0,0]
    for x in range(-50,56):
        dence[x]={}
        for y in range(-35,30):
            dence[x][y]=0
    print 'dense matrix initiated'
    while 1:
        county+=1
        countx=0
        total=0
        line=file.readline()
        if line =='':
            break
        line=line.strip().split(',')
        for count
