o
    Y�b	  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey^   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �followings.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint%   s
   
�r   c            	      C   s�  	 t td t �} | dkr�t�d�j}ddlm} d|  d }|� }||d	< d
|d< tj||d�}t�	d� t
�  ttd � t�d� t�	d� t
�  ttd t |  � ttd t |�� d d  d � t�d� |�� d d }d}tt|��D ]3}ttd t |�� d d | d  t d t d |�� d d | d  � t�d� |d  q}nttd � qtt td t ��}|dkr�t�d� t�d � t�	d!� t�d� d S t��  d S )"NTz
     Enter Circle ID: � z!https://pastebin.com/raw/RptmpLnKr   )�CaseInsensitiveDictz_https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getFollowingInfoList&offset=0&nickname=z
&limit=500z	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key)�headersr   z%

     Your Following Data Loading...�   z
     Your ID: z     Total Following: �data�totalr
   Z	followingz
 Nickname: Znicknamez
  Number: �+Zmsisdng�������?�   z
     Please Enter Valid IDz"

     Press Enter For Again Find r   z.showFollowingszpython followings.py)�input�green�yellow�requests�get�textZrequests.structuresr   r   r   r	   �printr   r   �json�range�len�cyan�red�str�purpler   r   �exit)	�user�keyr   Zurlr   Zresp�y�iZenterr   r   r   �main,   sF   


$
P

� 


r.   )r   r   r"   r   r   r   ZblueZ	lightbluer&   Zwhiter   r   r%   �endr(   r	   r   r.   �KeyboardInterruptr)   r   r   r   r   �<module>   s2    



*�