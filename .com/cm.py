o
    �T�b�  �                   @   s�   d dl Z d dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZ	dZ
dZd	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  eyZ   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �cm.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint&   s
   
�r   c                  C   sj  t �d� tttd t ��} t �d� t�  tttd t ��}t�	d� t �d� t�  tttd t ��}ddl
m} d	|  d
 | d }|� }||d< d|d< z-tj||d�}|�� d dkrjttd � n|�� d dkryttd � nttd � W n
   ttd � Y tttd t ��}|dkr�t �d� t �d� t �d� t�	d� d S t��  d S )Nzlolcat cm.ddlz

     Enter Circle ID: r   z
     Enter Your API Key: �   z
     Enter Your Message: r   )�CaseInsensitiveDictz^https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=78&nickname=zN&action=kom&msgId=974&imei=355176100129757&imsi=470022500179917&msisd&message=z&retry=false&operator=Robiz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key)�headersZrdesczRequest acceptedz      CCOM Successfully SentzInsufficient pointsz.     CCOM Not sent Beacuse Insufficient pointsz     CCOM Not SentzJ
        Your Request Rejected.Please Use VPN 
	       or Try Again Leter z"

     Press Enter For Again Find � r   z.comzpython cm.py�   )r   r   �str�input�cyan�yellowr	   �greenr   r   Zrequests.structuresr   �requests�getZjson�print�red�purpler   r   �exit)�userZapi�messager   Zurlr   ZrespZenterr   r   r   �main-   s>   



�


r%   )r   r   r   r   r   ZblueZ	lightbluer    Zwhiter   r   r   �endr!   r	   r   r%   �KeyboardInterruptr"   r   r   r   r   �<module>   s2   


*�