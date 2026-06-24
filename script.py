# Colecciones de datos de entrada estructuradas en listas paralelas
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States']] # Muestra simplificada

# --- 1. Conversión de Daños a Valores Numéricos ---
def actualizar_danos(lista_danos):
    conversion = {"M": 1000000, "B": 1000000000}
    danos_actualizados = []
    for dano in lista_danos:
        if dano == "Damages not recorded":
            danos_actualizados.append(dano)
        elif "M" in dano:
            danos_actualizados.append(float(dano.strip("M")) * conversion["M"])
        elif "B" in dano:
            danos_actualizados.append(float(dano.strip("B")) * conversion["B"])
    return danos_actualizados

danos_actualizados = actualizar_danos(damages)

# --- 2. Construcción de Diccionario Principal Maestre ---
def crear_diccionario_huracanes():
    huracanes = {}
    for i in range(len(names)):
        huracanes[names[i]] = {
            "Name": names[i], "Month": months[i], "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i], "Damage": danos_actualizados[i], "Deaths": deaths[i]
        }
    return huracanes

huracanes = crear_diccionario_huracanes()

# --- 3. Clasificación de Severidad por Escala de Daño ---
def clasificar_por_dano(huracanes):
    escala_dano = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    huracanes_por_dano = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for huracan in huracanes:
        dano_total = huracanes[huracan]['Damage']
        if dano_total == "Damages not recorded" or dano_total == escala_dano[0]:
            huracanes_por_dano[0].append(huracanes[huracan])
        elif dano_total > escala_dano[0] and dano_total <= escala_dano[1]:
            huracanes_por_dano[1].append(huracanes[huracan])
        elif dano_total > escala_dano[1] and dano_total <= escala_dano[2]:
            huracanes_por_dano[2].append(huracanes[huracan])
        elif dano_total > escala_dano[2] and dano_total <= escala_dano[3]:
            huracanes_por_dano[3].append(huracanes[huracan])
        elif dano_total > escala_dano[3] and dano_total <= escala_dano[4]:
            huracanes_por_dano[4].append(huracanes[huracan])
        elif dano_total > escala_dano[4]:
            huracanes_por_dano[5].append(huracanes[huracan])
    return huracanes_por_dano

huracanes_por_dano = clasificar_por_dano(huracanes)
