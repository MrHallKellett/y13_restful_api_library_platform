def process_cats():

    table = '''Breed	Average Weight (lbs)	Lifespan (years)	Notable Traits
    Siamese	8-10	12-15	 Vocal, intelligent, social
    Persian	7-12	10-15	Long-haired, calm, gentle
    Maine Coon	10-18	12-15	Large size, good with children
    Russian Blue	8-12	15-20	Quiet, shy, hypoallergenic
    Ragdoll	10-20	12-17	Relaxed, affectionate, blue eyes'''.splitlines()

    headers = table[0].split("\t")

    data = {"cats":[]}

    for line in table[1:]:
        this_cat = dict()
        line = line.split("\t")
        for i in range(len(headers)):
            this_cat[headers[i]] = line[i]

        data["cats"].append(this_cat)


    return data