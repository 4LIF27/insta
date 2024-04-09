AJ='Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3'
AI='user-agent'
AH=Exception
AE=' * selesai\n  \\__[ ©alifxynn/zhukov-z ] '
AD=' + '
AC='users'
AB='.cookie_ig.txt'
A8='strict-origin-when-cross-origin'
A7='https://www.instagram.com/alifxynn'
A6='25532C62-8BBC-4927-B6C5-02631D6E05BF'
A5='XMLHttpRequest'
A4='1009977574'
A3='936619743392459'
A2='129477'
A1='1475'
A0='same-origin'
z='cors'
y='empty'
w='"15.0.0"'
v='"Windows"'
u='""'
t='?0'
s='dark'
r='1.30208'
q='application/x-www-form-urlencoded'
p='en-US,en;q=0.9'
o='*/*'
n='Referrer-Policy'
m='Referer'
l='x-web-device-id'
k='x-requested-with'
j='x-instagram-ajax'
i='x-ig-www-claim'
h='x-ig-app-id'
g='x-csrftoken'
f='x-asbd-id'
e='viewport-width'
d='sec-fetch-site'
c='sec-fetch-mode'
b='sec-fetch-dest'
a='sec-ch-ua-platform-version'
Z='sec-ch-ua-platform'
Y='sec-ch-ua-model'
X='sec-ch-ua-mobile'
W='sec-ch-ua-full-version-list'
V='sec-ch-ua'
U='sec-ch-prefers-color-scheme'
T='dpr'
S='content-type'
R='accept-language'
Q='accept'
P='csrftoken=(\\w+)'
N='full_name'
M='user'
G=str
J='username'
I=exit
F=''
B='cookie'
A=print
import re as H,requests as C,json as K,random as L,time as x,os,sys,string as D
A9=C.Session()
E='Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'
AN=[]
id=[]
def AA():
	A(' * login your ig for continue');C=input(f"\n ? cookie : ")+';';open(AB,'w').write(C)
	try:
		E={AI:AJ};F={B:C};id=H.findall('ds_user_id=(\\d+);',G(C))[0];J=A9.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers=E,cookies=F);D=K.loads(J.text)
		if N in G(D):AF()
		elif'challenge_required'in G(D):I(' akun checkpoint')
		else:A(' cookie invalid atau perangkat spam');I()
	except AH as L:I(' terjadi kesalahan')
def AF():
	try:C=open(AB,'r').read()
	except:AA()
	try:
		J={AI:AJ};L={B:C};id=H.search('ds_user_id=(\\d+)',G(C)).group(1);O=A9.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers=J,cookies=L);D=K.loads(O.text)
		if N in G(D):
			try:I=D[M][N].split(' ')[0].lower()
			except:I=D[M][N].lower()
			E=D[M]['pk']
		else:AA()
	except AH as P:AA()
	A("\n _           _        \n(_)_ __  ___| |_ __ _ \n| | '_ \\/ __| __/ _` |. unfollow who don't \n| | | | \\__ \\ || (_| |. follow me back   \n|_|_| |_|___/\\__\\__,_|. github.com/zhukov-z\n\t");A(f"\t [ HAI {I} ] ");A(f"""
  1. unfol who dont foll back
  2. unfol masal 
  3. cek unfollow only 
   . log out
  """);F=input(' input : ')
	if F in['1','01']:AL(E,C)
	elif F in['2','02']:AK(E,C)
	elif F in['3','03']:AM(E,C)
	else:os.remove(AB)
def AK(uid,coki):
	N=coki;AI=F.join(L.choices(D.ascii_letters+D.digits,k=32));AA=H.search(P,N);AB=AA.group(1);A9={Q:o,R:p,S:q,T:r,U:s,V:E,W:E,X:t,Y:u,Z:v,a:w,b:y,c:z,d:A0,e:A1,f:A2,g:AB,h:A3,i:O(),j:A4,k:A5,l:A6,m:A7,n:A8};AF=C.get(f"https://www.instagram.com/api/v1/friendships/{uid}/following/?count=100",headers=A9,cookies={B:N})
	for G in K.loads(AF.text)[AC]:A();A(AD,G[J]);G=G[J];AH=C.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={G}",headers=A9,cookies={B:N}).json()['data'][M]['id'];AG(AH,G,N);x.sleep(10)
	I(AE)
def AL(uid,coki):
	N=coki;AJ=F.join(L.choices(D.ascii_letters+D.digits,k=32));AA=H.search(P,N);AB=AA.group(1);A9={Q:o,R:p,S:q,T:r,U:s,V:E,W:E,X:t,Y:u,Z:v,a:w,b:y,c:z,d:A0,e:A1,f:A2,g:AB,h:A3,i:O(),j:A4,k:A5,l:A6,m:A7,n:A8};AF=C.get(f"https://www.instagram.com/api/v1/friendships/{uid}/following/?count=100",headers=A9,cookies={B:N})
	for G in K.loads(AF.text)[AC]:
		A();A(AD,G[J]);G=G[J];AH=C.get(f"https://www.instagram.com/api/v1/friendships/{uid}/followers/?count=100",headers=A9,cookies={B:N})
		if G in AH.text:A(f"  + {G} sudah follow back")
		else:AI=C.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={G}",headers=A9,cookies={B:N}).json()['data'][M]['id'];AG(AI,G,N)
		x.sleep(10)
	I(AE)
def AM(uid,coki):
	M=coki;AG=F.join(L.choices(D.ascii_letters+D.digits,k=32));A9=H.search(P,M);AA=A9.group(1);N={Q:o,R:p,S:q,T:r,U:s,V:E,W:E,X:t,Y:u,Z:v,a:w,b:y,c:z,d:A0,e:A1,f:A2,g:AA,h:A3,i:O(),j:A4,k:A5,l:A6,m:A7,n:A8};AB=C.get(f"https://www.instagram.com/api/v1/friendships/{uid}/following/?count=100",headers=N,cookies={B:M})
	for G in K.loads(AB.text)[AC]:
		A();A(AD,G[J]);G=G[J];AF=C.get(f"https://www.instagram.com/api/v1/friendships/{uid}/followers/?count=100",headers=N,cookies={B:M})
		if G in AF.text:A(f"  + {G} sudah follow back")
		else:A(f"  + {G} belum follback")
		x.sleep(10)
	I(AE)
def O():B='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';A=L.choices;C=F.join(A(B,k=17));D=F.join(A(B,k=10));E=F.join(A(B,k=10));G=F.join(A(B,k=7));return f"hmac.{C}-{D}-{E}-{G}-"
def AG(user,x,coki):
	N=F.join(L.choices(D.ascii_letters+D.digits,k=32));G=H.search(P,coki);I=G.group(1);J={'container_module':'profile','nav_chain':f"PolarisProfileRoot:profilePage:1:via_cold_start",'user_id':user};K={Q:o,R:p,S:q,T:r,U:s,V:E,W:E,X:t,Y:u,Z:v,a:w,b:y,c:z,d:A0,e:A1,f:A2,g:I,h:A3,i:O(),j:A4,k:A5,l:A6,m:A7,n:A8};M=A9.post(f"https://www.instagram.com/api/v1/friendships/destroy/{user}/",headers=K,data=J,cookies={B:coki});C=M.json()['friendship_status']['following']
	if isinstance(C,bool):
		if C:A(f"  \\__[ gagal unfol {x} ]")
		else:A(f"  \\__[ done unfol {x} ]")
os.system('clear')
AF()
