import os
# Cherry was here - 29/7/2023
blocked_sites = ["pornhub.com", "xvideos.com", "pornimigur.com","xnxx.com","nsfw.xxx","rule34.xxx","spankbang.com","spankbang1.com","iporntv.net","porngifer.com","viralpornhub.com","mat6tube.com","xxxhdvideo.mobi","pienude.com","hdvideosporn.com","xhamster.com","xxk.mobi","xnxx2.info","xhofficial.com","xhamster2.com","fullsexmovs.com","shufflesex.com","pornfuck.net","thumbzilla.com","sexomdrag.com","you-porn.com","xxxpornxxx.net","xxxpornvideo.net","fapcat.com","93.115.61.56","hqporn.pro","hindiclips.com","youporner.net","free-xxx-tubes.com","hifixxx.fun","xhamster.desi","fr.youporn.com","youporn.com","xhamster1.desi","jerk-porn.com","99n-sbi.maggyvosseler.de","maggyvosseler.de","camwhores.in","big-tits-model.com","oceanzycia.pl","nsfwbrowser.com","1g7ea.oceanzycia.pl","gallimmobilien.de","u7ah.gallimmobilien.de","clssm.pl","752ma1.clssm.pl","truyen-hentai.co.uk","pornzonexxx.com","1bigclub.com","rajwap.cc","porno-zona.com","xxx18.uno","onlyfans.com","onlyfansleaks.vip","sxyprn.com","sex.com","es.sex.com","de.sex.com","ca.sex.com","us.sex.com","in.sex.com","love4porn.com","baddieslut.com","slut.com","horny.com","animepornhd.com","x-videos.blog","fapelloleaks.com","erome.com","qorno.com","dinotube.com","redwap-xxx.com","leakhd.com","leakporner.com","newporntv.click","kanporno.com","buceta.blog","sexy-egirls.com","sexpicturespass.com","tubegalore.com","cambro.tv","epal.gg","fapmasta.wtf","kgbvkrhhbwozugvvlyzjbkpjzfjzebrtygmnerkpopcfimtglcmjmfgislujcrg.danielodom.tech","danielodom.tech","00000nwebcamnow.com","0000114.com","0001casino.com","0005.us","000babes.com","000dvd.com","000freehosting.com","000go.com","000porn.com","porn.com","000pussy69pornxxxporno.com","000relationships.com","000-sex.com","000sexe.com","000webhostapp.com","00101001.com","0011cartoons.com","001-adult-toys-n-sex-dolls.com","001am.com","001porno.com","001londonescorts.com"] # <----- Blocked Websites (Will add more each update)

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # <------ Points to the Hosts file in Windows

with open(hosts_path, "a") as hosts_file:
    for website in blocked_sites:
        hosts_file.write(f"\n127.0.0.1 {website}")
print("Successfully Blocked some popular NSFW Websites (BlockList Version: 29/7/2023)")
print("Stay Safe & Stay Based - Cherry")
input("Press Enter to exit")