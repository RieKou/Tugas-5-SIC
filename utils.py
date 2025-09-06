def KonversiSuhu(nilai, suhu_awal, suhu_akhir):
    if suhu_awal == 'c' and suhu_akhir == 'f':
        return (nilai * 9/5) + 32
    elif suhu_awal == 'c' and suhu_akhir == 'k':
        return nilai + 273.15
    elif suhu_awal == 'f' and suhu_akhir == 'c':
        return (nilai - 32) * 5/9
    elif suhu_awal == 'f' and suhu_akhir == 'k':
        return (nilai - 32) * 5/9 + 273.15
    elif suhu_awal == 'k' and suhu_akhir == 'c':
        return nilai - 273.15
    elif suhu_awal == 'k' and suhu_akhir == 'f':
        return (nilai - 273.15) * 9/5 + 32
    else:
        return nilai