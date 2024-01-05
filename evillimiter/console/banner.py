from .io import IO


_MAIN_BANNER = r"""{}
-------- 
    !    
    !      (◍•ᴗ•◍) 𝙃𝙖𝙘𝙠𝙚𝙧 💖彡
    !    
----!     

                {}Edited by JHacker from J Project Platform  ~  limit devices on your network (LAN) 

                            Telegram Join @JProjectPlatform
                                    

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)
