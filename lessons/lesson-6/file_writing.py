# ava fail output.txt
# kirjuta sinna kaks rida teksti
# sulge fail
# kui faili ei ole siis tee see

# a = append, failile juurde lisamiseks. Kui faili ei ole siis teeb selle.
# r = read, avab faili lugemiseks. Fail peab olemas olema.
# w = write, avab faili kirjutamiseks. Kui faili pole siis teeb selle.
# r+ = read + write, avab faili lugemiseks ja kirjutamiseks. Kui faili ei ole annab errori.
# w+ = write + read, avab faili kirjutamiseks ja lugemiseks. Kui faili ei ole siis teeb selle.

exercise = open("files/output.txt", "w")
exercise.write("Päike paistab.\n")
exercise.write("Ilm on soe.")


exercise.close()
