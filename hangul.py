def make_char(i, m, t):
    code = ((i * 21) + m) * 28 + t + 0xAC00
    return chr(code)

def i_chr_idx(cha):
    idx = ((ord(cha) - 0xAC00) // 28) // 21
    return idx

def m_chr_idx(cha):
    idx = ((ord(cha) - 0xAC00) // 28) % 21
    return idx

def t_chr_idx(cha):
    idx = (ord(cha) - 0xAC00) % 28
    return idx

index_i = [
          'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 
          'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
          'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

index_m = [
          'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 
          'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
          'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 
          'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ' ]

index_t = [
          '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 
          'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 
          'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

idx_j_comb1 = ['ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']
idx_j_comb2 = ['ㄱㅅ','ㄴㅈ','ㄴㅎ','ㄹㄱ','ㄹㅁ','ㄹㅂ','ㄹㅅ','ㄹㅌ','ㄹㅍ','ㄹㅎ','ㅂㅅ']
idx_m_comb1 = ['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ']
idx_m_comb2 = ['ㅗㅏ','ㅗㅐ','ㅗㅣ','ㅜㅓ','ㅜㅔ','ㅜㅣ','ㅡㅣ']

ja_code = ord('ㄱ')
ja_code_last = ord('ㅎ')
mo_code = ord('ㅏ')
mo_code_last = ord('ㅣ')


text_data = ''

while True:
    print('text_data')
    print(text_data)
    cha = input()

    cha_code = ord(cha)
    is_ja = ja_code <= cha_code and cha_code <= ja_code_last
    is_mo = mo_code <= cha_code and cha_code <= mo_code_last
    
    if text_data:
        last_cha = text_data[-1]
        last_cha_code = ord(last_cha)
        if ja_code <= last_cha_code and last_cha_code <= mo_code_last:
            if ja_code <= last_cha_code and last_cha_code <= ja_code_last:
                if is_mo:
                    i = index_i.index(last_cha)
                    m = index_m.index(cha)
                    t = 0
                    c = make_char(i, m, t)
                    text_data = text_data[:-1] + c
                    continue
            elif mo_code <= last_cha_code and last_cha_code <= mo_code_last:
                1
        elif last_cha_code >= 0xAC00 and last_cha_code <= (0xAC00 + 0x2BA4):
            i = i_chr_idx(last_cha)
            m = m_chr_idx(last_cha)
            t = t_chr_idx(last_cha)
            if t == 0:
                if is_ja:
                    if cha in index_t:
                        t = index_t.index(cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        continue
                elif is_mo:
                    chk_cha = index_m[m] + cha
                    if chk_cha in idx_m_comb2:
                        comb_idx = idx_m_comb2.index(chk_cha)
                        comb_cha = idx_m_comb1[comb_idx]
                        m = index_m.index(comb_cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        continue
            else:
                if is_mo:
                    t_cha = index_t[t]
                    if t_cha in idx_j_comb1:
                        comb_idx = idx_j_comb1.index(t_cha)
                        part_cha = idx_j_comb2[comb_idx]
                        t = index_t.index(part_cha[0])
                        t_cha = part_cha[1]
                    else:
                        t = 0
                    
                    c1 = make_char(i, m, t)
                    if t_cha in index_i:
                        i = index_i.index(t_cha)
                        m = index_m.index(cha)
                        c2 = make_char(i, m, 0)
                        text_data = text_data[:-1] + c1 + c2
                        continue
                elif is_ja:
                    chk_cha = index_t[t] + cha
                    if chk_cha in idx_j_comb2:
                        comb_idx = idx_j_comb2.index(chk_cha)
                        comb_cha = idx_j_comb1[comb_idx]
                        t = index_t.index(comb_cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        continue
    
    text_data += cha
    