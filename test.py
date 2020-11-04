def text_queries(sentences, queries):
    # Write your code here
    for i in range(len(sentences)):
        sentences[i] = sentences[i].split()
        
    for i in range(len(queries)):
        queries[i] = queries[i].split()
    
    output = []
    for i, x in enumerate(sentences):
        print("Current Sentence:", x)
        for query in queries:
            print("Current Query:", query)
            temp = []
            match = True
            for word in query:
                print("Current Word:", word)
                if word not in x:
                    print(word, "not in ", x)
                    match = False
                    break
            if match == True:
                print(query, "matches:", x)
                print(i)
                temp.append(i)
                
        if temp:
            output.append(temp)
    
    for x in output:
        print (x)