o
    �R�b�  �                   @   s�   d dl Z d dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZ	dZ
dZd	Zd
ZdZe �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey\   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz

 https://bit.ly/3Hz6Ff5�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �api.py�header"   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint)   s
   
�r   c            	      C   s"  	 t ttd t ��} t| �dkrHddlm} d|  }|� }d|d< tj||d	�}|�	� d
 dkr=t
td � t�d� n
ttd � t��  nttd � q	 t�d� t�  t ttd t ��}|dkr�ddlm} d|  d | }|� }d|d< tj||d	�}|�	� d
 dkr�z"t
td t |�	� d d  � t
td t |�	� d d  � W n   t
td t � Y nt
dt � nttd � qP	 |�	� d d }dt d }|� }||d < d|d< tj||d	�}	 t ttd! t ��}|dk�rt�d"� t�d#� t�d$� t�d%� d S d S )&NTz
     Enter Number : �   r   )�CaseInsensitiveDictzahttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=19892&app_version=78&msisdn=88Z(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key)�headersZrdescZOKz
     A OTP Sent Your Number.�   z)     OTP Not Sent.Please Try Again Leter.z      Please Enter a valid Numberr   z
     Enter OTP Code: � zfhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=validateOTC&pin=19892&app_version=78&msisdn=88z&otc=zExpired pinz
     Nickname: �dataZnicknamez     API Key:  Zmkeyz
     OTP Not Valid


z
     OTP Not Validz     Please Enter Otpz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&message=Hey!+I'm+Generate+My+API+Key+From+ARU's+System.z&retry=falsez	x-api-keyz+

     Press Enter For Again Genarate API  r   z.apiGeneratezpython api.py�   )�str�input�green�yellow�lenZrequests.structuresr   �requests�getZjsonr   r   r   �print�redr   �exitr   r   r	   �white�mark�cyan�purpler   )	Znumberr   Zurlr   ZrespZOTCZapiZresp_stZenterr   r   r   �main/   sf   �
 $�



�r(   )r   r   r   r   r   ZblueZ	lightbluer"   r$   r   r   r&   �endr'   r%   r	   r   r(   �KeyboardInterruptr#   r   r   r   r   �<module>   s4   


<�