import smtplib

CREDS = {
    "em": "tdummy027@gmail.com",
    "em2": "superinfinity5@gmail.com",
    "pss": "***************************",
    "msg": "The ISS Is Above You!",
    "port": 587
}


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=CREDS['port']) as con:
        con.starttls()
        con.login(user=CREDS['em'], password=CREDS['pss'])
        con.sendmail(
            from_addr=CREDS['em'],
            to_addrs=CREDS['em2'],
            msg=f"Subject:LOOK ABOVE THE ISS!\n\n{CREDS['msg']}"
        )
