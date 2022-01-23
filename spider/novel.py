#include scripts that scrape novels from web
import requests
from bs4 import BeautifulSoup
import re,html2text  
class Agent(object):
    '''browser user agent'''
    phone="Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001)\
AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8"
    pc="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
class N1(object):
    'https://www.75zhongwen.com/900563/?&fr=www.75zw.com/900563/'
    def __init__(self):
        '''check response status is ok'''
	    
        url='https://www.75zhongwen.com/900563/?&fr=www.75zw.com/900563/'
        headers={'User-Agent':Agent.pc}   
        resp=requests.get(url,headers=headers)
        if resp.reason=="OK":
            text=resp.text
            with open('p.html','w',encoding='utf-8') as fd:
                fd.write(text)
            print('resp ok')
            return 
        else:

            return 
    def parse_html(self):
        '''read html file,parse html \n
        {'第955章 在黑夜中寻求，却闻见──（3）': 'https://www.75zw.info/900563/789672.html'}
        '''
         # read file to str
        text=''
        with open('p.html','r',encoding='utf-8') as fd:
            text=fd.read()
        # parse html with bs
        soup=BeautifulSoup(text,'html.parser')
        rets=soup.find_all('dd')
        res={}
        root_url='https://www.75zw.info'
        for item in rets[12+952:]:
            s=BeautifulSoup(str(item),'html.parser')
            r=s.find('a')
            res[r.get_text()]=root_url+r.get('href')
        return res
    def get_text(self,full_url: str):
        '''download html page and return its text'''
        headers={'User-Agent':Agent.pc}   
        html=requests.get(full_url,headers=headers).text
        return html
    def filter_next_page(self,s):
        s=str(s)
        soup=BeautifulSoup(s,'html.parser')
        ret=soup.find_all('a')[0]

        return ret.get_text()=='下一页'
    def next_page_check(self,html_str: str,root_url: str):
        '''return tuple (next page exist,list of next page links)'''
        soup=BeautifulSoup(html_str,'html.parser')
        rets=soup.find_all('a')
        link=''
        total_str=''
        for item in rets:
            if item.get_text()=='下一页':
                link=root_url+item.get('href')
                
                break

        if link=='':
            return (False,'')
        else:
            while 1:
                print(f'next page link {link}')
                text=self.get_text(link)
                soup=BeautifulSoup(text,'html.parser')
                rets=soup.find_all('a')
                total_str+=text
                l=list(filter(self.filter_next_page, rets))
                if l==[]:
                    break
                else:
                    s=BeautifulSoup(str(l[0]),'html.parser')
                    ret=s.find_all('a')[0]
                    lk=ret.get('href')
                    link=root_url+lk
                    del l
                    continue
            return (True,total_str)
    def down_html(self,items: dict,root_url: str):
        '''append html from web to file'''
        fd=open('a.html','a',encoding='utf-8')
        for k,v in items.items():
            chapter=int(re.findall('第(.*?)章',k)[0])
            if chapter>0:
                print(f'download chapter {chapter}')
                print(f'link is {v}')

                headers={'User-Agent':Agent.pc}   
                html=requests.get(v,headers=headers).text
                fd.write(html)
                (exist,next_page_contents)=self.next_page_check(html,root_url)
                if exist:
                    fd.write(next_page_contents)
    def read_lines(self,file: str):
        '''return list of str'''
        with open(file,'r',encoding='utf-8') as fd:
            s=fd.readlines()
        return s
    def read_to_str(self,file: str)-> str:
        s=''
        with open(file,'r',encoding='utf-8') as fd:
            s=fd.read()
        return s
    def write_to_file(self,contents: str,dst_file: str):
        '''override original file contents'''
        with open(dst_file,'w',encoding='utf-8') as fd:
            fd.write(contents)
    def htmltotxt(self,html_file: str,txt_file: str):
        html_str=self.read_to_str(html_file)
        text=html2text.html2text(html_str)
        self.write_to_file(text,txt_file)
    def clear_garbage_text(self,file: str):
        s=self.read_lines(file)
        total_str=''
        for item in s:
            if '[' in item or ']' in item:
                continue
            if item.strip()=='':
                continue
            if item.strip()=='item.strip()':
                continue
            total_str+=item+'\n'
        self.write_to_file(total_str,file)

    def __call__(self):
        root_url='https://www.75zw.info'
        d=self.parse_html()
        self.down_html(d,root_url)
        self.htmltotxt('a.html','ypzz.txt')
        self.clear_garbage_text('ypzz.txt')

class N2(object):
    'https://www.xswang.com/book/55120/'
    def __init__(self):
        '''check response status is ok'''
	    
        url='https://www.xswang.com/book/55120/'
        headers={'User-Agent':Agent.pc}   
        resp=requests.get(url,headers=headers)
        if resp.reason=="OK":
            text=resp.text
            with open('p.html','w',encoding='utf-8') as fd:
                fd.write(text)
            print('resp ok')
            return 
        else:

            return 
    def get_text(self,full_url: str):
        '''download html page and return its text'''
        headers={'User-Agent':Agent.pc}   
        html=requests.get(full_url,headers=headers).text
        return html
    def parse_html(self):
        '''read html file,parse html \n
        {'第955章 在黑夜中寻求，却闻见──（3）': 'https://www.75zw.info/900563/789672.html'}
        '''
         # read file to str
        text=''
        with open('p.html','r',encoding='utf-8') as fd:
            text=fd.read()
        # parse html with bs
        soup=BeautifulSoup(text,'html.parser')
        rets=soup.find_all('dd')
        res={}
        root_url='https://www.xswang.com'
        for item in rets[124:]:
            s=BeautifulSoup(str(item),'html.parser')
            r=s.find('a')
            res[r.get_text()]=root_url+r.get('href')
        return res
    def filter_next_page(self,s):
        s=str(s)
        soup=BeautifulSoup(s,'html.parser')
        ret=soup.find_all('a')[0]

        return ret.get_text()=='下一页'
    def next_page_check(self,html_str: str,root_url: str):
        '''return tuple (next page exist,list of next page links)'''
        soup=BeautifulSoup(html_str,'html.parser')
        rets=soup.find_all('a')
        link=''
        total_str=''
        for item in rets:
            if item.get_text()=='下一页':
                link=root_url+item.get('href')
                
                break

        if link=='':
            return (False,'')
        else:
            while 1:
                print(f'next page link {link}')
                text=self.get_text(link)
                soup=BeautifulSoup(text,'html.parser')
                rets=soup.find_all('a')
                total_str+=text
                l=list(filter(self.filter_next_page, rets))
                if l==[]:
                    break
                else:
                    s=BeautifulSoup(str(l[0]),'html.parser')
                    ret=s.find_all('a')[0]
                    lk=ret.get('href')
                    link=root_url+lk
                    del l
                    continue
            return (True,total_str)
    def down_html(self,items: dict,root_url: str):
        '''append html from web to file'''
        fd=open('a.html','a',encoding='utf-8')
        chapter=103
        for k,v in items.items():
            chapter+=1
            if chapter>0:
                print(f'download chapter {chapter}')
                print(f'link is {v}')

                headers={'User-Agent':Agent.pc}   
                html=requests.get(v,headers=headers).text
                fd.write(html)
                # (exist,next_page_contents)=self.next_page_check(html,root_url)
                # if exist:
                #     fd.write(next_page_contents)
    def read_lines(self,file: str):
        '''return list of str'''
        with open(file,'r',encoding='utf-8') as fd:
            s=fd.readlines()
        return s
    def read_to_str(self,file: str)-> str:
        s=''
        with open(file,'r',encoding='utf-8') as fd:
            s=fd.read()
        return s
    def write_to_file(self,contents: str,dst_file: str):
        '''override original file contents'''
        with open(dst_file,'w',encoding='utf-8') as fd:
            fd.write(contents)
    def htmltotxt(self,html_file: str,txt_file: str):
        html_str=self.read_to_str(html_file)
        text=html2text.html2text(html_str)
        self.write_to_file(text,txt_file)
    def clear_garbage_text(self,file: str):
        s=self.read_lines(file)
        total_str=''
        for item in s:
            if '[' in item or ']' in item:
                continue
            if item.strip()=='':
                continue
            if item.strip()=='item.strip()':
                continue
            total_str+=item+'\n'
        self.write_to_file(total_str,file)

    def __call__(self):
        root_url='https://www.xswang.com'
        # d=self.parse_html()
        # self.down_html(d,root_url)
        self.htmltotxt('a.html','ypzz.txt')
        self.clear_garbage_text('ypzz.txt')
b=N2()()
