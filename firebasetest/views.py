from django.shortcuts import render

from django.shortcuts import render
import pyrebase


config = {

    "apiKey": "AIzaSyDzatatG73Id4TPLRuVxzpmUjosxK57M8Q",
    "authDomain": "yashpro1-a11f9.firebaseapp.com",
    "databaseURL": "https://yashpro1-a11f9-default-rtdb.asia-southeast1.firebasedatabase.app",
    "type": "service_account",
    "project_id": "yashpro1-a11f9",
    "storageBucket": "yashpro1-a11f9.appspot.com",
    "messagingSenderId": "517745548781",
    "appId": "1:517745548781:web:1740858a27af2e27661be4",
    "measurementId": "G-QGCLDZD4KD",
    "private_key_id": "8ac543587b1f442a2277f97cd39f753e469af117",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxJ7QLJx0lh583\nZkkG+0NkvkhtxdP9Iy48QNjsyPgrlTdD23hzD1gxKxWvSSDxM4G/yYHVF1fsYQ4G\n1WQHFBlWfxeGcoDeKWpXlkmXtl4cI9BVnznZH/p110KKELUjVnJmgjKedhCd9hrr\nRs/XECA7W2mI/uccE7msEThSnmmbVZs7Uq+cWWJR/aZLf45yXau9lOVrZ1F559Fz\nyPf6jzOfZDADKAgXBEphDr7zVygzFsPBjf0hna+hgIkOcfhw6Q2QMnV9PwlVe0o6\nApkoe5YNunc8/c0yAWYyTpyaooey8/TFI1dKu1p04ID8KiZdrMYUfSlv7dqos0L0\nuE1QEKHRAgMBAAECggEAJH5dz/hYQD1udo6bF5WWHgA20mowz9I5+Y6QQULrIKtF\n7bQd3XH5RHOwLWI+p4FpRpVfqgJ7icW6inzV9MFWsONQeNFIq7tTXUSn11lpjJly\nFtlMpOY6BaF44xErB2MNAQHsJImExc2HYRU+xnpbcW7U0DRWbom/s2r+s8JPVgCV\nMP3X5rX+kjTLLjkdysVOFMmB+bDZvkw54B+6R9x9wG31gMD7m0yQzI1hbQkzLOJj\nlzjMQ/eccJQdJXbk55rHeBWnDkwmJZcSf8JNlZRIz2L9iXQGov5jgPu7dLIq+JQc\nvArtVEZIGicC/iiP8hymuHmzzyhX0vBUJvwG/i/7+QKBgQD6CD1NHzhRKGVwXbcq\n+8L5QeonDvwCRUBs10myWi3KqLsumCQ+7wrXdLUUjd8ORBWaLW9U+hk8+uqoMed4\nqp/dokHS2SzrchZwri6xGVAv0yihwr5dvguGE2HhuB3y90SiWNPdXReiTupCt8p9\nwIeuiDDqyZ+zRsG/4qovu415nQKBgQC1YiqKBilz1pltJ/Z8SXtTss66nyaSjB4t\nxnpG+JtT/iVyV/7z+iE/tDWGIfOeEg4YW9eFKfmvDSkp2ILBaZXcFySF221dPJQr\nHZW93tZTxnevtxshYo14JMeTGna0+UqqEr05CR0eOS/9c2sBbgWW4JFMxQpMOI4t\nLM63NVJ8xQKBgQDaFZO6kA+kIlMQRn28nSn8FXUyKky/gj3mcYXTbfrg+HmD86ox\nxnizYxWK3w/+tn4NI7Im8ZpP6SACIr0eL90PCTbWvR0EJFfUYulRCZ46iLi5F07K\nHziX8pH+uoRM50ZTQJ1TSJ6TsLd+CCcztlnibuIT+Fc2nPHj98WvqqyEtQKBgQCR\nz5R62HFCWeWExndzem7V3gwqIf6UGGe6TK/HldroLopT3UFrSEyqNWhBp9F75O/H\nzSz4M8IwYtgQd6jFaue5wjDuGnNUXHqQHnxd4mFRf15/tybsM5meV5LIQqHi4fSP\nu/i5fQYXYcmeacY/o/6CR40Gte+NTnmc/0Q+K3NgMQKBgDFatPfV+hkWDw40yUWL\nVzU+Vte9pf+XegU63yCcCgfH2ZDVHzT18OEa57clDwMPvmbEM1VVXGJ4WI6beu46\njtl5kD1Q3u6mzoEcnt3oHz1FZDV7q9z5m9Tv4v/Efev+kBuckI/czpZsrMlY64ll\nddSv2zHbP7BX5wEgCX7V5DKv\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-wb517@yashpro1-a11f9.iam.gserviceaccount.com",
    "client_id": "116743134430715584470",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wb517%40yashpro1-a11f9.iam.gserviceaccount.com"
}

###################// ACESS DATABASE\\ #########################
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# print(database)
# print(firebase)

# n1 = database.child('DDs').child('Rahul').get().val()
# n2 = database.child('DDs').child('Raj').get().val()

# stack = database.child('Data').child('Stack').get().val()
# framework = database.child('Data').child('Framework').get().val()



###########// ACESSING CHILD VALUES OF DDs \\#################
def index(request):
    n1 = database.child('DDs').child('Rahul').get().val()
    n2 = database.child('DDs').child('Raj').get().val()
    n3 = database.child('DDs').get().val()


    
    context = {
        'n1':n1,
        'n2':n2,
        'n3':n3, 
    }
     
    return render(request, 'Home.html', context)