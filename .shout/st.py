o
    �T�b�  �                   @   s�   d dl Z d dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZ	dZ
dZd	Zd
ZdZe �d� dd� Zdd� Zdd� Zdd� Zz	e�  e�  W dS  ey`   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz4
 
 
 Sent From ARU's system
 https://bit.ly/3Hz6Ff5�clearc                   C   �,   t �d� t �d� t �d� t �d� d S �N�..zlolcat banner.shz.Textzlolcat MyText.txt��os�chdir�system� r
   r
   �st.py�header&   �   


r   c                   C   r   r   r   r
   r
   r
   r   �header2,   r   r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr
   r
   r   �	logoprint3   s
   
�r   c            	      C   sL  t �d� 	 tttd t ��} | dkr ttd � t�	d� n	t �d� t
�  nq	 tttd t ��}|dkrEttd � t�	d� n	t �d� t
�  nq+	 tttd	 t ��}|dkrjttd � t�	d� nnqPt �d� t
�  ttd
 � t�	d� t �d� t
�  ttd t | � ttd t t|� � t|�D ]Y}d| t d }| dd�}z:tj||d�}|�� d }|dkr�ttd |�� d d  d � n|dkr�ttd � nttd � t�	d� W q�   ttd � t�	d� Y q�tttd t ��}|dk�r t �d� t �d � t �d!� t�	d� d S t��  d S )"Nzlolcat st.shTz

     Enter Your API Key: � z$     Your Entered Value Is Not Valid�   r   z

     Enter Your Message: z

     Enter Your Shout Amout: z!

     Your Request Prosseing....�   z
     Your Message: z
     Shout Amount: zrhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&message=z&retry=falseZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg)z	x-api-keyz	x-app-key)�headersZrdesczRequest acceptedz
    CSHOUT Sent your�data�totalZ	FollowerszInsufficient pointsz
      Insufficient pointsz
     Errorz*
     Please Make Sure Internet Connection�   z#

     Press Enter For Again Shout r   z.shoutzpython st.py)r   r	   �str�input�green�yellow�print�redr   r   r   �int�cyanr   �range�	watermark�requests�getZjson�purpler   r   �exit)	Zapi�message�amount�iZurlr   Zresp�statusZenterr
   r
   r   �main<   sv   

�	
�	�


�"
�



r1   )r   r   r   r)   r	   ZblueZ	lightbluer$   Zwhiter"   r!   r&   �endr+   r(   r   r   r   r1   �KeyboardInterruptr,   r
   r
   r
   r   �<module>   s6   


	>�