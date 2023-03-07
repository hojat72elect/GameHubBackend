from csv import reader, writer

with open("github1.csv", mode="r") as old_db:
    readerObj = reader(old_db)
    with open("github2.csv", mode="w") as new_db:
        writerObj = writer(new_db)
        for line in readerObj:
            if len(line[0]) < 80:
                writerObj.writerow(line)
        new_db.close()
    old_db.close()
