o
    ���b�  �                   @   s  d dl Z d dlZd dl Z d dlZd dlZzd dlZW n   e �d� d dlZY zd dlZW n   e �d� d dlZY d dlmZ ej	j
jed� dZdZdZdZd	Zd
ZdZdZdZe �d� dd� Zdd� Zdd� Zdd� Zz	e�  e�  W dS  ey�   e��  Y dS w )�    Nzpip install requestszpip install aiohttp)�InsecureRequestWarning)�categoryz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s"   t �d� t �d� t �d� d S )N�lolcat banner.sh�.Text�lolcat MyText.txt)�os�system�chdir� r   r   �	circle.py�header)   s   

r   c                   C   s,   t �d� t �d� t �d� t �d� d S )N�..r   r   r   )r   r
   r	   r   r   r   r   �header2.   s   


r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint4   s
   
�r   c                  C   s�  	 d} t ttd t ��}|| kr/ttd � t�d� t�d� t	�  t
td t d � nt
td	 � t�d
� q	 d}t ttd t ��}||kr�ttd � t�d� t�d� t	�  t
td t d � t
td t d � t�d� ttd � t�d� t�d� nt
td � t�d
� q<	 t�d� t	�  t�d� t ttd t ��}|dkr�t�d� t	�  ttd � t�d� t�d� t�d� t�d� d S |dkr�t�d� t	�  ttd � t�d� t�d� t�d� t�d� d S |dk�r&t�d� t	�  ttd  � t�d� t�d� t�d!� t�d"� d S |d#k�rOt�d� t	�  ttd$ � t�d� t�d� t�d%� t�d&� d S |d'k�rxt�d� t	�  ttd( � t�d� t�d� t�d)� t�d*� d S |d+k�r�t�d� t	�  ttd, � t�d� t�d� t�d-� t�d.� d S |d/k�r�t�d� t	�  ttd0 � t�d� t�d� t�d1� t�d2� d S |d3k�r�t�d� t	�  ttd4 � t�d� t�d� t�d5� t�d6� d S |d7k�rt�d� t	�  ttd8 � t�d� t�d� t�d9� t�d:� d S |d;k�rJt�d� t	�  ttd< � t�d� t�d� t�d=� t�d>� t�d?� d S |d@k�rxt�d� t	�  ttdA � t�d� t�d� t�d=� t�dB� t�dC� d S |dDk�r�t�d� t	�  ttdE � t�d� t�d� t�d=� t�dF� t�dG� d S |dHk�r�t�d� t	�  ttdI � t�d� t�d� t�dJ� t�dK� d S t
tdL � t�d� q�)MNTZmr_aruz
    Enter Username: z    [Username Correct]�   r   z
    Username : z[Ariful Islam Arman]z    Incorrect Usernamez)xdg-open https://www.facebook.com/Aru.OfcZme_noobz
    Enter Password: z    [Password Correct]z
    Password : z[MR-ARU]�   z


    Loging in Please Wait...�   z    Incorrect Passwordzlolcat option.shz     Choose a Option: �1z>

    You Choosed Circle API Key Genarate.

    Please wait...r   z.apiGenaratezpython api.py�2zA

    You Choosed Circle ID To Number Option.

    Please wait...z.iDtoNumzpython idtonum.py�3z>

    You Choosed Number To Circle Option.

    Please wait...z.numToIDzpython numToId.py�4zA

    You Choosed Chek Following List Option.

    Please wait...z.showFollowingszpython followings.py�5zA

    You Choosed Chek Followers List Option.

    Please wait...z.showFollowerszpython followers.py�6zB

    You Choosed Clean Following List Option.

    Please wait...z.followingCleanzpython clean.py�7z3

    You Choosed CPoke Option.

    Please wait...z.pokezpython cp.py�8z2

    You Choosed CCOM Option.

    Please wait...z.comzpython cm.py�9z4

    You Choosed CSHOUT Option.

    Please wait...z.shoutzpython st.pyZ10z;

    You Choosed Change Gender Option.

    Please wait...z.changez.genderzpython g.pyZ11z=

    You Choosed Change Birthday Option.

    Please wait...z.bdatezpython b.pyZ12z=

    You Choosed Change Nickname Option.

    Please wait...z.nickzpython n.pyZ13z=

    You Choosed Chek Shout List Option.

    Please wait...z.updatezpython shout.pyz
     Please Enter Valid Value)�str�input�green�yellowr   r   r   r   r	   r   �print�	lightblue�cyan�redr
   )ZcorrectuserZusernameZcorrectpassZpasswordZchosser   r   r   �main:   s@  


�





�

















































































 ��r-   )r   Zasyncior   r   Zrequestsr	   ZaiohttpZurllib3.exceptionsr   ZpackagesZurllib3Zdisable_warningsZbluer*   r,   Zwhiter(   r'   r+   �endZpurpler   r   r   r-   �KeyboardInterrupt�exitr   r   r   r   �<module>   sH   




 3�