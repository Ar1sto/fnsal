#!/usr/bin/env python
#coding: utf-8 
#Author: Ar1st0
import os, sys, stdiomask, time, string, random, base64, subprocess, pyttsx3
from random import randint
from colorama import Fore, Style 

def tts(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()
ufile = open("_user_/usernames.txt", 'r+')
pfile = open("_user_/passwords.txt", 'r+')
ucont = ufile.read()
pcont = pfile.read()
def selftype_fast(string: str) -> None:
    for buchstabe in string:
        print(buchstabe, end='', flush=True)
        time.sleep(0.0001)
def selftype(string: str) -> None:
    for buchstabe in string:
        print(buchstabe, end='', flush=True)
        time.sleep(0.05)
def clearw():
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
def register():
    global u
    global p
    global ucont
    global pcont
    global base64_pw
    u = str(input(Style.RESET_ALL+"Username: "))
    if u == "":
        print (Fore.RED+"\nUsername can't be empty.")
        sys.exit(2)
    else:
        ufile.write("\n[+] Username: "+u)
#   pw = stdiomask.getpass
#    stdiomask.getpass()
    p = str(stdiomask.getpass())
    if p == "":
        print (Fore.RED+"\nPassword can't be empty.")
        sys.exit(2)
    else:
        encpw = p
        pw_bytes = encpw.encode('ascii')
        base64_bytes = base64.b64encode(pw_bytes)
        base64_pw = base64_bytes.decode('ascii')
        pfile.write(base64_pw)
        print ("\nIhre Registrierung ist abgeschlossen.")
        tts("Welcome "+u)
        sys.exit(3)
def banner():
    selftype_fast((Fore.BLUE+Style.BRIGHT+'''                                                                                                                                                                                      

                                                                                                                @@@@@ @                                                                                                
                                                                                                      @@@BOu/xcC0dkkkdmQXu/nO@@@@@                                                                                     
                                                                                               @@@wrQ8a)[[->;:,;I!I,^:>++<~___+}a%0rw@@@                                                                               
                                                                                            @zz80]->"  ti  -&),:p^.f&I . ^&  Q#X.':<-]0%Yz@                                                                            
                                                                                      @@@vOB1-l"-(^'%&    f8r;I;,,"a%:^''-Z. &8 .8O  o.;>+_%Qc@@@                                                                      
                                                                                   @@@n%f1]+l`8.   .>Bp8%,a%r     `8%`   w/"~%%U8%I' %h,)80 ^<)8xB@@                                                                   
                                                                                 @@x%[+<!:^'^;%%&#* `%%'."i%%^   k']%m  .%Il%%-%h^ .B%<I' %%k%]I>?%x@@                                                                 
                                                                               @Jbz}i _     `;i>!;c%<1%0##'   '.        .  .WW+8%".W%~I  8%-_l'0W:i-xbU@@                                                              
                                                                             Bf%?+lI;#&Z      ..|  8..  .td&%@aX)]]?]]{/O8B8of.  .`%MI' 8B[~;' 8%  .:_1%f@                                                             
                                                                         @@@rB}!'    l)%&          x&8t-XB%%%%8&888&88&&8&8%%%b{?d%c   b%1i,  .%8a%;:I>?1Br@                                                           
                                                                        @ (B}->;%&*h   :B8!oi  p%)_B%B%%8%8W&8&8&8&W&&WW8&&8888&&&B%c?%W      8%-+i;"`'"l_}B(@@                                                        
                                                                      @@X%[i. .I<%i<B88t^{ .&q_%%&8888W8&W&&&&&WWW&WWWWW&&8W&&WW&88&8%%%v1%' "%<>:`        ,-%z@                                                       
                                                                     @@Qf[>x&   ^d%+-il  Wd]%%88%&&&&&&W&WMWMMWWMMMWMWWMMW&WWMW&&&&8&8888%8w?%          {o#Bi[j0@@                                                     
                                                                     jB~^    .a~ .%^  "%-B%8&8&8WM&WM&MWMMMWWMWMMMMMMMWWMWMMWWWWMWW&8W&&88&&8%}a_  t&8%] B%>!l~[Br                                                     
                                                                  @@vz_^Zhka#WW%8p" _%]%%88888&&W&MWWWM#MM##M##MM##MM##MMM###MMMMM&&&&W&&&&8888BZnX. ":;%%!.    lrv@@                                                  
                                                                  8b]<:,p%:";!<>;..B_&8%8&%M&&&MMM&WWWMMMWMMM####M####MMM#MM#MWWM#W*}lIlh&&&&8&88%oz_  %%l .oo#MI:_h8                                                  
                                                                @a&~^   ..~%:    8?8%88%8W8&WW&WkWMMW#MM###of<<+    ?M*###MM##W&~/nnnnnnnf_&&&%88%&Bt& `+l%%#++>lB>-&d@                                                
                                                                qB~;%%W%%%!''% _pb%%8%%%&88_fnnnnnnx]jWMMMWX|{{x8@*u  #####MWMYjnnnnnnnnnnnto&W&88888%-o "B+!^.':i%-[Bm                                                
                                                               hB-lB^;>+-1%?  %_%8%8W&88%}xunnnnnnnnnnnM&W&%B*|}%.   ',MWWWMWWOunnnnnxxnnnnnva8&88888&Bf% a'  c   .."<Bk                                               
                                                             @B#}+I8.    ^)] 8]%&8%8&&&8(nnnnnCnnnxcnu8MMW&%BB@w'    'v&#WWWWM8*nndnxqwB&#Ynnf&88&&&&8%&8U',8%&.   0M`<W%@                                             
                                                             @U_l:;%%M(  lW Bc%%8&W&W88/nnW@Bnx@@cnmnvo&8&88&8@       f&&&W&&&Baxnxw@Buucn@unk/&&W&WWW&8&%}>'` 8#%%ki%_]U@                                             
                                                           @@/Ql.   'Y%%M` %JB%&88W&W&*xcn8nnnnznkunnW@&W8&888:. . -  .f&W&88&8qxnuunn@nUunBurxt8WM&MW&&&&%(>`%n_]%_>Y_~J/@@                                           
                                                            d%<Ip%8&WU    %fB8&&&&8W&WncxxnnYx%cZxxzuWB%&&888k .     .'{888&%%M/nnuzxun@xJnnannjh&&MWWWWW&8%c,/%;`.    "!8p                                            
                                                           @v>"a "i<>p%8 W_%&&8W8W&888nux%urn8nCx8rxnj?o#a&&8^@:*@,,@:,JB%%Wh]r%nn%@nxnn@vYnndnnvW&&WMW&&W&&h# . o8WoW8)~?c@                                           
                                                          @0%I.*      '`,)%&%8WWW8W&Whcn8nnx@nJnYxBnzvnnhWWWWWW&&&W&WWW&WWMWWWLnxn@x@xuxub@oBnW@nW&WW&WWMW&&%{%',"' %%?~>>%Q@                                          
                                                          @r_>oB%%8###! %O%&&&WMWWW&Wu%BCoQ@vOnhnnWUnUnY#WWWWWWWWWWWWWWWWWWWW&wb@@xUn8vxnn0n@nnqxMWWMMMWWW8&&%)`   &B"'  "<x@                                          
                                                          8&~_%?-+<>l~:!_%&&&&WWWWWW&Xnnn#n%nx@nYznd@xxzMWWWWWWWWWWWWWWWWWWWW&BbnnhnWnuBQ@nn@nnunbWWMW#MMWWW&%r8 `%%z8&W(;iWW                                          
                                                          (*I".        %z8&WWWMW&MW&&vCnn@nnb8nurnkuuQwB&&WWWW&WMW&&WW&&WWWW&W&&nux@nhOpn@nn@nnxnC8MMWMWWMMW&W&f'n:'      ,a)                                          
                                                          /_.   ch*W8d.U%8&&&WWWMWW&Wu#nn@xn@n%x%unx&nnY,*k' kd wbU bb  kk ab %c8rvx@B@nn&nn@nnnCJ&WMMWWMM&WMWB-h .%%%%%&..~|                                          
                                                        @@cl;%%8_"%l!I~_BW&WWWMMW&&W8n&nnWnnBnnBBcu@uOxC**b' bd wbU bb  bk ab q8nBxU%n&xnQnnkrnnoU8MMMMW#WMMMWWL%^%<---_>%:;z@@                                        
                                                        @@wIl>_-QB%   #-B&&WWWWMW&MW*nZnxonn8nn%nn&#nxcX%ob' bd wbU bb  bk abI%M@0nz#nUwnxmnJcnn&YW&##MM##WMWW&@#!#I,^`":)/!q@@                                        
                                                        @@h`        &.&1%WW&W#WWWWWW0nvnxwnn#nnBnnqnno8@@%k' bd wbU bb  bk hb#hM8xnx@nx%nn@nupnnZzW&MWM#MMMMMMMBUiLp^    ^,;k@                                         
                                                        @ k` o#*oo*&%,&{8&WWW&WMMWWWUnxnnOnnpnn@nxQnnbbXzok. bd wbU bb  bk h&dBzvOnn@nn@nn@nxWnnxuMWWWMWWMMMM&WBJ'       b:^h@                                         
                                                         @O""".  BBM_<&18&WMW&&WWWWWUYnnaXunznn@nrJnnZ0pnU@w bd wbU bb  bk.@oOWun@nn@ru@xn@nnO@xnu&WWMMMMMMM#W&BQ'MohbaM%*I:Z@@                                        
                                                        @ u.   0&%I,^^h?B&WWWMMWWM&&Jhu8nnnxxnnWnxcnnzx@u*B@Bbd wbU bb  b*%@BzqBBBnnYknCcn%xnnxhnd0WMWW#WMWWW&W%%><<~[%XI"``c@@                                        
                                                          )^ '8%^".`l><-%&WWWW&WM&&WC@n@nnndrnnbncxn*@@@@@*b@ @ wkU bb '8@@Oa@@@@@qun@uxhnnBXnnncjx8WMMMWMM&MW8u&III!><>>%^:1                                          
                                                          (d,i_?_>l;Ii>bB&W&W&&MW&W&Lk&OnnOunnxZnZrn*@@@@Bqww0MBBbU ba%@hOQ8b#@@B@%vnBnn@nnn@nwnW*r&WWWMM#MMWWB?U".  .'"::^w)                                          
                                                          W&.^,;:,,"":!%|8&M&MMWWWWWJCQ0xu@xnncCnWrcB%B%BznnJnvh8@@@@B#%XnnnLz%%%B@%n0Ln@nnn@#0uJBBWWMMMMMMMM&BY;".        WM                                          
                                                          @/         ':<}%WMWMWWWWWM8@aXnmunnn@unBnQBBB%BnnJ0ZnoaM@@8a0WmU%nur%%88B%vu@nu8nnMXrxvBB8MMMMWM#WW8)B;'  }     .t@                                          
                                                          @YW     ]#  fi%j%&&WWWWMW&BBonnoXnx@vnn@u@B%%8Mx@unu0o(ooaa0/LZuXnnMc8%8%B@u@onn@xxn8nx&8&WW#MMWWWWBYi""<@@I.   WY@                                          
                                                           @r   ]@ q@Q';~C%WWW&&WM&W&WqnBLknZannx@Q@88%%J&nrCuzYLxpXqu^Zonvwnnw8888BB@xUdn%BnMvBBWM&MMMMM#MWB-dI` BIf.. . x@                                           
                                                            QW    (,t@'^!Y-%WWWMWWWW&W#@@c%nB@nx@c%B%8%BmnnWnLXp(pxlx?/,kuxhunxZ888%B@@n#nYrvnu0B&&WWWM#M&M8c%!^    ,^   WJ                                            
                                                           @@1_   f    .,<&+%WMMWWWWW&%@@xrXr*u%v@@%88%%xnnpncYjl~u;|;0!8nnnunnv&8888B@B@@nQQnnx8W8WMWWWWWW*h<,.        <(@@                                           
                                                             Bc.        .,<8_BMMWWW&8M&&OnzYnxnW8@%8%B%Unko%nnOc.c';-ni`kLnL@oYr8%8888B@@@@vnx@8o&WWWWMWW&&Z>'          Y@                                             
                                                             @*h          .>8-B&&WWWWW&&%BBcxnB@@B%8&f[dhZ}0*oh+Z" ;|, :Ckbb/fk&#O88&#W8#h&B0n@pu8WWWMWW88p<^ '        o*@                                             
                                                               Co      .aW',<8]BWW&&&W&&B88u#@8&owmkCatk%@x@h@qWcnruU0Q?{#_8(?]@a/hkQ{dU|d&@@8@8&uWWW&&%v8i' `0J^8&o .oU                                               
                                                               @uo    %8"^   ;(j%&WW&&&&ZtOaakdj}})t?qao@mooooacx/()()/MpW#aowa*o*+j|/tfL&&8BBB&WhoMMW%-%; :%,<_B>:  ou@                                               
                                                                @Co  ,O:. (o  "_B[%888&&8MrkwUf(/)}zBB@@B8wpwdhhomqawqp&oB#pBBB@BB@@qqBknQm8&8BhwZ8&8Mu|, "1   '^u  oU@                                                
                                                                  aq. "0*. d8X `!ruW88&W8&@t]QBBj|XBBB&88B%B%X%*"h ? Z}B%B%8%%8&W&8W8W&Whd/p%&qrm&&&-%l    M0  ." .dk                                                  
                                                                   @t"  "B?I%^   .!o?B8&8%cjnc0Zfjuv&W&&&&88%%BBBBB@BB@@BB&8&&WWWWMMMW&W&8b0ntJb&%_B!    8%l"n!  `fB                                                   
                                                                     1k  ';l%.M "J .lB-%%8BBB%B%%B%BW&WWMWWMM&W&W&&88&&W&&WWW#WWMMWWMMWWMWW8W888_%l' ;+ W "qB)  a1                                                     
                                                                     @oY.  C%l:%#'f0  IJ0t%88&8WW&&W&WMWWWMWMMWMWMMMWMMW#MMMWMMMMWMMWMWWWW8&%8-8!. ,&'%%BB%B  .Uo@                                                     
                                                                      @B/k  ^B8l,`%8'o. ">%?d8&&W%&&WMWM#M#M#WWMWWMMMMWM##MMWMMM#MWWWMW&&%%-Mv!'  WW %I<B*^  k/B@                                                      
                                                                        @@]Y .."U%!,`%kWi  ,~8})8%W&&WWM#MMM#WMMWMM#MM#M#M###WWWMWMWW&%h?&cl'   X8'^8X`8'..Y]@@                                                        
                                                                         @@%}j  ';;<B+8`!&u~ .I+C%{18%8WWWWW#M###MMM#MWMWMMMWWWMW%%U-p#~,   "M> .>%W>b`  f}%@@                                                         
                                                                             @?m.  +%>:{%:^ &     ';>#Bx_[o%8%%&WW#MWWW&8B%B%u??M&};"^`  Mt  _:%8*<1^  m[@                                                             
                                                                               @@1m.  'n%I^'%8,. M!M .  .,Ii~|m&%%WMooM8B%kc?!:`    'k. ."%^8d,U<!^  .w)@@                                                              
                                                                                 @*[p   ':+>!;^'%d`'.8IW  ~                 .Od*# aW i `;d]??&`   p[*@                                                                 
                                                                                    @k[q      h"i%lIBbI' 8&   k% 'W'"11 (   8.`"!%>8i"'`"x,    p}d@@                                                                   
                                                                                      @@81c1    .,I+%<I-o8%X,;%mii%%8:%8&."l%Z '!B}t%'     1Y18@@                                                                      
                                                                                            B(fw'      .,ikB!i%]~-Bl:"IlBI:;l_#U     ..Zt(%                                                                            
                                                                                               @@#)[XC:                         "LX])#@@                                                                               
                                                                                                    @@@@Bz/[-}fULOOOOZCJf[-[/zB@@@@                                                                                    
                                                                                                             @@@@@@  @@@ @                       BETA-VERSION v0.1 by Ar1sto                                                                        
    '''))
banner()        
def menu():
    selftype("Willkommen {0} beim Hauptdatenbankmanagement-Programm der National-Security-Agency\n".format(u))
    tts("Welcome {0} to Main-Database".format(u))
    load_str = "Standort und IP-Adresse wird ermittelt..."
    ls_len = len(load_str)
    set_ani_one = "}"
    set_ani_two = "{" 
    animation = "|/-ooox\\"
    anicount = 0
    counttime = 0        
    i = 0
    while (counttime != 100): 
        time.sleep(0.1)                               
        load_str_list = list(load_str)  
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res+set_ani_one+animation[anicount]+set_ani_two) 
        sys.stdout.flush() 
        load_str = res 
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
    subprocess.call(['xterm', '-e', 'python3 check.py'])    
    print (Fore.YELLOW+"Tool-Menu wird nun ausgeführt...")
def login():
    global u
    global p
    global ucont
    global pcont
    u = str(input(Style.RESET_ALL+"\nLogin: "))
    if u == "":
        print (Fore.RED+"Benutzername kann nicht leer sein.")
        login()
    elif u in ucont:        
        p = str(stdiomask.getpass())
        if p == "":
            print (Fore.RED+"Passwort kann nicht leer sein.")
            login()
        else:
            pwcont = pcont.splitlines()
            for zeile in pwcont:
                base64_bytes = zeile.encode('ascii')
                pw_bytes = base64.b64decode(base64_bytes)
                clear_pw = pw_bytes.decode('ascii')
                if p == clear_pw:
                    print (Style.BRIGHT+Fore.GREEN+"\nLogin erfolgreich.\n") 
                    clearw()
                    banner()
                    print (Style.RESET_ALL)
                    menu()    
                    break
                else:                 
                    print (Style.BRIGHT+Fore.RED+"Login fehlgeschlagen.")
                    sys.exit(3)    
    else:
        print ("[-] Benutzer nicht registriert\n")
        print ("\n [Ja = j | Nein = n]")
        reg = str(input("Möchtest du dich jetzt registrieren?: "))
        if reg == "j":
            register()
        else:
            sys.exit(3)
login()


