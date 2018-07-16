""" ### 
Author : H@ns
Scripted On : May 14, 2018 08:39PM
Purpose : Based on technical test in BNP Paribas, Malad
### """

from operator import itemgetter
def frd():
	fp=open('fin.dat')
        header=[]
        final_list=[]
        length=0
	for v in fp:
		ap=sorted(v.split(','))
		for val in ap:
                        hv=val.split('=')[0].replace('\n','')
                        hv2=val.split('=')[1].replace('\n','')
                        if hv not in header:
                                header.append(hv)
                        if length<len(hv):
                                length=len(hv)
                        if length<len(hv2):
                                length=len(hv2)
        #print header
        fp=open('fin.dat')
        for vl in fp:
                apk=sorted(vl.split(','))
                #print 'apk',apk
                fr_data=[]                
                un_li=[]
                for v in apk:
                        val=v.split('=')
                        if val[0] not in un_li:
                                un_li.append(val[0])
                
                # looping over header
                for vls in sorted(header): 
                        # for each row split value iteration
                        for sa in apk:
                                val=sa.split('=')
                                if vls in un_li and val[0]==vls:
                                        fr_data.append(val[1].replace('\n',''))
                                        break
                                elif vls not in un_li:
                                        fr_data.append('')
                                        break
                final_list.append(fr_data)
                #print final_list,un_li
        return [sorted(header),final_list,length]


def dwr(act_dat):
        f = open('output.txt','w')
        head=act_dat[0]
        values=act_dat[1]
        length=act_dat[2]
        sp=' '
        for hc in sorted(head):
                txtlen=length-len(hc)
                word=hc+str(sp*(txtlen)+sp)
                f.write(word)
        f.write('\n\n')
        values=sorted(values, key=itemgetter(4))
        for vs in values:
                #print vs
                for i in vs:
                        if i!='':
                                vtxtlen=length-len(i)
                                vword=i+sp*vtxtlen+sp
                                f.write(vword)
                        else:
                                f.write(sp*length+sp)
                else:
                        f.write('\n')
        f.close()

act_dat=frd()
dwr(act_dat)


"""###--- *** ---###"""
as_di={'0':{'Name':'Akash','EmplId':101,},'1':{'Dept':'CC','EmplId':102},'2':{'Name':'Ram','Dept':'Zept','EmplId':20}}

for v in sorted(as_di,key=lambda x: (as_di[x]['EmplId'])):
	print as_di[v]

