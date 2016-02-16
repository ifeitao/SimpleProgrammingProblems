def sorted_merge(items1, items2):
    index1 = 0
    index2 = 0
    items_merged = []
    length1 = len(items1)
    length2 = len(items2)
    while True:
        if index1 == length1:
            for item in items2[index2::]:
                items_merged.append(item)
            break
        if index2 == length2:
            for item in items1[index1::]:
                items_merged.append(item)
            break
        if items1[index1] < items2[index2]:
            items_merged.append(items1[index1])
            index1 += 1
        else:
            items_merged.append(items2[index2])
            index2 += 1
    return items_merged

if __name__ == "__main__":
    print(sorted_merge([1, 100, 1000, 10000], [2, 4, 6, 101, 1001]))
