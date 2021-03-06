seq1 = "MAGPATQSPMKLMALQLLLWHSALWTVQEATPLGPASSLPQSFLLKCLEQVRKIQGDGAALQEKLVSECATYKLCHPEELVLLGHSLGIPWAPLSSCPSQALQLAGCLSQLHSGLFLYQGLLQALEGISPELGPTLDTLQLDVADFATTIWQQMEELGMAPALQPTQGAMPAFASAFQRRAGGVLVASHLQSFLEVSYRVLRHLAQP"

seq2 = "MDTWTVIILLQYFLFASLVQSAPVGLPSNLPPAFRETAVEAKTLGDKILKDISATHAATVKAFSLDSSASSLQLMAASMRIPSSPVLKAPSEHFTLETCVSHMLAGVQMYQNLLEVLSSKVIGLDDLRADLRDLLNHINKLKEVAQLTVDVSDQNLSTDLASHLQDSHNVQVALQLTLTQLRSFCHDLNRTFKVLSINRP"



BLOSUM52 = {'GW': -3.0, 'GV': -4.0, 'GT': -2.0, 'GS': 0.0, 'GR': -3.0, 'GQ': -2.0, 'GP': -2.0, 'GY': -3.0, 'GG': 8.0, 'GF': -4.0, 'GE': -3.0, 'GD': -1.0, 'GC': -3.0, 'GA': 0.0, 'GN': 0.0, 'GM': -3.0, 'GL': -4.0, 'GK': -2.0, 'GI': -4.0, 'GH': -2.0, 'ME': -2.0, 'MD': -4.0, 'MG': -3.0, 'MF': 0.0, 'MA': -1.0, 'MC': -2.0, 'MM': 7.0, 'ML': 3.0, 'MN': -2.0, 'MI': 2.0, 'MH': -1.0, 'MK': -2.0, 'MT': -1.0, 'MW': -1.0, 'MV': 1.0, 'MQ': 0.0, 'MP': -3.0, 'MS': -2.0, 'MR': -2.0, 'MY': 0.0, 'FP': -4.0, 'FQ': -4.0, 'FR': -3.0, 'FS': -3.0, 'FT': -2.0, 'FV': -1.0, 'FW': 1.0, 'FY': 4.0, 'FA': -3.0, 'FC': -2.0, 'FD': -5.0, 'FE': -3.0, 'FF': 8.0, 'FG': -4.0, 'FH': -1.0, 'FI': 0.0, 'FK': -4.0, 'FL': 1.0, 'FM': 0.0, 'FN': -4.0, 'SY': -2.0, 'SS': 5.0, 'SR': -1.0, 'SQ': 0.0, 'SP': -1.0, 'SW': -4.0, 'SV': -2.0, 'ST': 2.0, 'SK': 0.0, 'SI': -3.0, 'SH': -1.0, 'SN': 1.0, 'SM': -2.0, 'SL': -3.0, 'SC': -1.0, 'SA': 1.0, 'SG': 0.0, 'SF': -3.0, 'SE': -1.0, 'SD': 0.0, 'YI': -1.0, 'YH': 2.0, 'YK': -2.0, 'YM': 0.0, 'YL': -1.0, 'YN': -2.0, 'YA': -2.0, 'YC': -3.0, 'YE': -2.0, 'YD': -3.0, 'YG': -3.0, 'YF': 4.0, 'YY': 8.0, 'YQ': -1.0, 'YP': -3.0, 'YS': -2.0, 'YR': -1.0, 'YT': -2.0, 'YW': 2.0, 'YV': -1.0, 'LF': 1.0, 'LG': -4.0, 'LD': -4.0, 'LE': -3.0, 'LC': -2.0, 'LA': -2.0, 'LN': -4.0, 'LL': 5.0, 'LM': 3.0, 'LK': -3.0, 'LH': -3.0, 'LI': 2.0, 'LV': 1.0, 'LW': -2.0, 'LT': -1.0, 'LR': -3.0, 'LS': -3.0, 'LP': -4.0, 'LQ': -2.0, 'LY': -1.0, 'RT': -1.0, 'RV': -3.0, 'RW': -3.0, 'RP': -3.0, 'RQ': 1.0, 'RR': 7.0, 'RS': -1.0, 'RY': -1.0, 'RD': -2.0, 'RE': 0.0, 'RF': -3.0, 'RG': -3.0, 'RA': -2.0, 'RC': -4.0, 'RL': -3.0, 'RM': -2.0, 'RN': -1.0, 'RH': 0.0, 'RI': -4.0, 'RK': 3.0, 'VH': -4.0, 'VI': 4.0, 'EM': -2.0, 'EL': -3.0, 'EN': 0.0, 'EI': -4.0, 'EH': 0.0, 'EK': 1.0, 'EE': 6.0, 'ED': 2.0, 'EG': -3.0, 'EF': -3.0, 'EA': -1.0, 'EC': -3.0, 'VM': 1.0, 'EY': -2.0, 'VN': -3.0, 'ET': -1.0, 'EW': -3.0, 'EV': -3.0, 'EQ': 2.0, 'EP': -1.0, 'ES': -1.0, 'ER': 0.0, 'VP': -3.0, 'VQ': -3.0, 'VR': -3.0, 'VT': 0.0, 'VW': -3.0, 'KC': -3.0, 'KA': -1.0, 'KG': -2.0, 'KF': -4.0, 'KE': 1.0, 'KD': -1.0, 'KK': 6.0, 'KI': -3.0, 'KH': 0.0, 'KN': 0.0, 'KM': -2.0, 'KL': -3.0, 'KS': 0.0, 'KR': 3.0, 'KQ': 2.0, 'KP': -1.0, 'KW': -3.0, 'KV': -3.0, 'KT': -1.0, 'KY': -2.0, 'DN': 2.0, 'DL': -4.0, 'DM': -4.0, 'DK': -1.0, 'DH': -1.0, 'DI': -4.0, 'DF': -5.0, 'DG': -1.0, 'DD': 8.0, 'DE': 2.0, 'DC': -4.0, 'DA': -2.0, 'DY': -3.0, 'DV': -4.0, 'DW': -5.0, 'DT': -1.0, 'DR': -2.0, 'DS': 0.0, 'DP': -1.0, 'DQ': 0.0, 'QQ': 7.0, 'QP': -1.0, 'QS': 0.0, 'QR': 1.0, 'QT': -1.0, 'QW': -1.0, 'QV': -3.0, 'QY': -1.0, 'QA': -1.0, 'QC': -3.0, 'QE': 2.0, 'QD': 0.0, 'QG': -2.0, 'QF': -4.0, 'QI': -3.0, 'QH': 1.0, 'QK': 2.0, 'QM': 0.0, 'QL': -2.0, 'QN': 0.0, 'WG': -3.0, 'WF': 1.0, 'WE': -3.0, 'WD': -5.0, 'WC': -5.0, 'WA': -3.0, 'WN': -4.0, 'WM': -1.0, 'WL': -2.0, 'WK': -3.0, 'WI': -3.0, 'WH': -3.0, 'WW': 15.0, 'WV': -3.0, 'WT': -3.0, 'WS': -4.0, 'WR': -3.0, 'WQ': -1.0, 'WP': -4.0, 'WY': 2.0, 'PR': -3.0, 'PS': -1.0, 'PP': 10.0, 'PQ': -1.0, 'PV': -3.0, 'PW': -4.0, 'PT': -1.0, 'PY': -3.0, 'PC': -4.0, 'PA': -1.0, 'PF': -4.0, 'PG': -2.0, 'PD': -1.0, 'PE': -1.0, 'PK': -1.0, 'PH': -2.0, 'PI': -3.0, 'PN': -2.0, 'PL': -4.0, 'PM': -3.0, 'CK': -3.0, 'CI': -2.0, 'CH': -3.0, 'CN': -2.0, 'CM': -2.0, 'CL': -2.0, 'CC': 13.0, 'CA': -1.0, 'CG': -3.0, 'CF': -2.0, 'CE': -3.0, 'CD': -4.0, 'CY': -3.0, 'CS': -1.0, 'CR': -4.0, 'CQ': -3.0, 'CP': -4.0, 'CW': -5.0, 'CV': -1.0, 'CT': -1.0, 'IY': -1.0, 'VA': 0.0, 'VC': -1.0, 'VD': -4.0, 'VE': -3.0, 'VF': -1.0, 'VG': -4.0, 'IQ': -3.0, 'IP': -3.0, 'IS': -3.0, 'IR': -4.0, 'VL': 1.0, 'IT': -1.0, 'IW': -3.0, 'IV': 4.0, 'II': 5.0, 'IH': -4.0, 'IK': -3.0, 'VS': -2.0, 'IM': 2.0, 'IL': 2.0, 'VV': 5.0, 'IN': -3.0, 'IA': -1.0, 'VY': -1.0, 'IC': -2.0, 'IE': -4.0, 'ID': -4.0, 'IG': -4.0, 'IF': 0.0, 'HY': 2.0, 'HR': 0.0, 'HS': -1.0, 'HP': -2.0, 'HQ': 1.0, 'HV': -4.0, 'HW': -3.0, 'HT': -2.0, 'HK': 0.0, 'HH': 10.0, 'HI': -4.0, 'HN': 1.0, 'HL': -3.0, 'HM': -1.0, 'HC': -3.0, 'HA': -2.0, 'HF': -1.0, 'HG': -2.0, 'HD': -1.0, 'HE': 0.0, 'NH': 1.0, 'NI': -3.0, 'NK': 0.0, 'NL': -4.0, 'NM': -2.0, 'NN': 7.0, 'NA': -1.0, 'NC': -2.0, 'ND': 2.0, 'NE': 0.0, 'NF': -4.0, 'NG': 0.0, 'NY': -2.0, 'NP': -2.0, 'NQ': 0.0, 'NR': -1.0, 'NS': 1.0, 'NT': 0.0, 'NV': -3.0, 'NW': -4.0, 'TY': -2.0, 'TV': 0.0, 'TW': -3.0, 'TT': 5.0, 'TR': -1.0, 'TS': 2.0, 'TP': -1.0, 'TQ': -1.0, 'TN': 0.0, 'TL': -1.0, 'TM': -1.0, 'TK': -1.0, 'TH': -2.0, 'TI': -1.0, 'TF': -2.0, 'TG': -2.0, 'TD': -1.0, 'TE': -1.0, 'TC': -1.0, 'TA': 0.0, 'AA': 5.0, 'AC': -1.0, 'AE': -1.0, 'AD': -2.0, 'AG': 0.0, 'AF': -3.0, 'AI': -1.0, 'AH': -2.0, 'AK': -1.0, 'AM': -1.0, 'AL': -2.0, 'AN': -1.0, 'AQ': -1.0, 'AP': -1.0, 'AS': 1.0, 'AR': -2.0, 'AT': 0.0, 'AW': -3.0, 'AV': 0.0, 'AY': -2.0, 'VK': -3.0}
def exam():
    def calculate_matrix(seq1,seq2,S,gap):
        F=[]
        for i in range(len(seq1)+1):
            subF=[]
            for j in range(len(seq2)+1):
                subF.append(0)
            F.append(subF)
        for i in range (1,len(seq1)+1):
            F[i][0]= -i*gap
        for j in range (1,len(seq2)+1):
            F[0][j]= -j*gap

        for i in range (1,len(seq1)+1):
            for j in range (1,len(seq2)+1):
                sD=F[i-1][j-1]+ float (S[seq1[i-1] + seq2[j-1]])
                sC=F[i-1][j] -gap
                sR=F[i][j-1] - gap
                F[i][j]= max(sR,sC,sD)
        P=[]
        for i in range(len(seq1)+1):
            subP=[]
            for j in range (len(seq2)+1):
                subP.append(0)
            P.append(subP)
        for i in range (1,len(seq1)+1):
            P[i][0]="l"
        for j in range (1,len(seq2)+1):
            P[0][j]= "u"
        for i in range (1,len(seq1)+1):
            for j in range (1,len(seq2)+1):
                if F[i][j]==F[i-1][j-1]+ float (S[seq1[i-1] + seq2[j-1]]):
                    P[i][j]="d"
                elif F[i][j]==F[i-1][j] -gap:
                    P[i][j]="l"
                elif F[i][j]==F[i][j-1] - gap:
                    P[i][j]="u"
        return [F,P]

    def best_alignment(F,P):
        i=len(seq1)
        j=len(seq2)
        A=""
        B=""
        score=F[i][j]
        while(i>0 or j>0):
            if P[i][j]=="d":
                A=seq1[i-1]+A
                B=seq2[j-1]+B
                i=i-1
                j=j-1
            elif P[i][j]=="u":
                A="-"+A
                B=seq2[j-1]+B
                j=j-1
            elif P[i][j]=="l":
                A=seq1[i-1]+A
                B="-"+B
                i=i-1
        return [A,B ,score]
    R=calculate_matrix(seq1,seq2,BLOSUM52,1)
    L=best_alignment(R[0],R[1])
    print (L[0])
    print (L[1])
    print ("The score of this aligment is ", L[2])

    return



                    
         
        

