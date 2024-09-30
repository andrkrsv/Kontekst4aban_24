def count_nucle(dno):
    stop_words = {"UAA", "UAG", "UGA"}
    result = []
    chain_len = 0 

    for i in range(0, len(dno), 3):
        condon = dno[i:i+3]
        if condon in stop_words:
            result.append(chain_len)
            chain_len = 0
        else:
            chain_len += 3
    return result


dna_bts = input().strip()
nucle_cout = count_nucle(dna_bts)

print(*nucle_cout)