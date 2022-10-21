def rc(n):
    r=[]
    if(n==2):
        r = ['0','1']
    elif(n==4):
        r = ['00','01','11','10']
    return r

def is_legal_region(kmap_function, term):
    number_rows = len(kmap_function)
    for i in range(0,number_rows-1):
        if(len(kmap_function[i])==len(kmap_function[i+1])):
            continue
        else:
            raise ValueError("UNEQUAL ROWS")
            break
    number_columns = len(kmap_function[0])
    row = rc(number_columns)
    column = rc(number_rows)
    term_str=''
    not_none= []
    for i in range(0,len(term)):
        if term[i]==1 or term[i]==0:
            term_str+=str(term[i])
            not_none.append(i)
            continue
        elif term[i]==None:
            term_str+='x'
            continue
    string=''
    list_indices=[]
    for j in range(0,len(column)):
        for i in range(0,len(row)):
            string=row[i]+column[j]
            list_indices.append((string,j,i))
    region=[]
    x = True
    for i in range(0,len(list_indices)):
        for j in not_none:
            if list_indices[i][0][j]==term_str[j]:
                x=True
                continue
            else:
                x=False
                break
        if x:
            region.append((list_indices[i][1],list_indices[i][2]))
    is_legal = True
    for i in region:
        if kmap_function[i[0]][i[1]]==1 or kmap_function[i[0]][i[1]]=='x':
            is_legal = True
            continue 
        elif kmap_function[i[0]][i[1]]==0:
            is_legal = False
            break
    rows_indices=[0]
    x = region[0][0]
    r=[x]
    for i in range(len(region)):
        if region[i][0] != x:
            rows_indices.append(i)
            x = region[i][0]
            r.append(x)
    rows=[] 
    for i in range(len(rows_indices)):
        if rows_indices[i]<rows_indices[-1]:
            rows.append(region[rows_indices[i]:rows_indices[i+1]])
        elif rows_indices[i]==rows_indices[-1]:
            rows.append(region[rows_indices[i]:len(region)])
    print(r)
    print(rows)      
    c=[]
    for i in range(len(rows[0])):
        c.append(rows[0][i][1])
    rows_cts = True
    columns_cts = True
    for i in range(len(r)-1):
        if r[i]+1==r[i+1]:
            rows_cts = True
        else:
            rows_cts = False
            break
    for i in range(len(c)-1):
        if c[i]+1==c[i+1]:
            columns_cts = True
        else:
            columns_cts = False
            break
    top_left=()
    bottom_right=()
    if rows_cts==True and columns_cts==True:
        top_left = min(region)
        bottom_right = max(region)
    elif rows_cts==False and columns_cts==True:
        top_left = rows[-1][0]
        bottom_right = rows[0][-1]
    elif rows_cts==True and columns_cts==False:
        top_left = rows[0][-1]
        bottom_right = rows[-1][0]
    elif rows_cts==False and columns_cts==False:
        top_left = max(region)
        bottom_right = min(region)      
    return (top_left,bottom_right,is_legal)
print(is_legal_region([[0,1,1,0],['x',1,'x',0],[1,0,0,0],[1,'x',0,0]],[None,0,None,0]))
