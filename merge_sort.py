def mergeSort(lstPerformMergeSort):
    if len(lstPerformMergeSort) == 1:
        return lstPerformMergeSort
    
    lstSubPerformMergeSort1 = []
    lstSubPerformMergeSort2 = []
    for iter in range(len(lstPerformMergeSort)):
        if iter < len(lstPerformMergeSort) / 2:
            lstSubPerformMergeSort1.append(lstPerformMergeSort[iter])
        else:
            lstSubPerformMergeSort2.append(lstPerformMergeSort[iter])
    
    lstSubPerformMergeSort1 = mergeSort(lstSubPerformMergeSort1)
    lstSubPerformMergeSort2 = mergeSort(lstSubPerformMergeSort2)

    idxCount1 = 0
    idxCount2 = 0
    for iter in range(len(lstPerformMergeSort)):
        if idxCount1 == len(lstSubPerformMergeSort1):
            lstPerformMergeSort[iter] = lstSubPerformMergeSort2[idxCount2]
            idxCount2 += 1
        elif idxCount2 == len(lstSubPerformMergeSort2):
            lstPerformMergeSort[iter] = lstSubPerformMergeSort1[idxCount1]
            idxCount1 += 1
        elif lstSubPerformMergeSort1[idxCount1] > lstSubPerformMergeSort2[idxCount2]:
            lstPerformMergeSort[iter] = lstSubPerformMergeSort2[idxCount2]
            idxCount2 += 1
        else:
            lstPerformMergeSort[iter] = lstSubPerformMergeSort1[idxCount1]
            idxCount1 += 1
    return lstPerformMergeSort

a = [1,5,4,2,3,4,56]
a = mergeSort(a)
print(a)