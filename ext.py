def foldername(extension):
# lista di estensioni che diventano sottocartelle
    if(extension == ""):
        return None
    else:
        switcher = {
            "exe"  : "Software", 
            "txt"  : "Note-Testo",
            "csv"  : "Dati grezzi",
            "dat"  : "Dati grezzi",
            "pdf"  : "PDFs", 
            "c"    : "C programs", 
            "py"   : "Python",
            "java" : "Java programs",
            "class": "Java programs", 
            "cpp"  : "Cpp programs", 
            "jpg"  : "Immagini", 
            "png"  : "Immagini",  
            "jpeg" : "Immagini", 
            "raw"  : "Immagini",
            "mp3"  : "Musica", 
            "mp4"  : "Video", 
            "mkv"  : "Video",
            "xlsx" : "Fogli di calcolo",
            "xls"  : "Fogli di calcolo",
            "ods"  : "Fogli di calcolo",
            "ppt"  : "Presentazioni",
            "pptx" : "Presentazioni",
            "doc"  : "Documenti",
            "docx" : "Documenti",
            "zip"  : "Compressi"
        }
        return switcher.get(extension, "Miscellanea") #returns "Miscellanea" if not in dictionary
