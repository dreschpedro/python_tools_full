import csv

# Función para escribir los datos en un archivo CSV
def write_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

# Datos proporcionados
data = [
("Ramen",),
("118. Ramen Sopa" ,"$8500"),
("-	Carne",),
("-	Pollo",),
("-	Cerdo",),
("-	Vegetariano",),
("119. Ramen Sopa ","$11100"),
("-	Mariscos ",),
("-	Camarones",),
("120. Ramen Salteado ","$8500"),
("-	Carne",),
("-	Pollo",),
("-	Cerdo",),
("-	Vegetariano ",),
("121. Ramen Salteado ","$11100"),
("-	Mariscos ",),
("-	Camarones",),



("Manu Vegetariano",),

("Entradas",),
("122. Rollitos Primavera De Verdura" ,"$3000"),
("123. Papas Fritas Tradicionales" ,"$3700"),
("124. Papas Noiset" ,"$4500"),
("125. Queso De Soja Crocante" ,"$3600"),
("126. Empanaditas Hervidas" ,"$3300"),
("127. Empanaditas A La Plancha" ,"$3700"),
("128. Pure De Papas" ,"$2400"),
("129. Baochi Pan Al Vapor De Verduras" ,"$2500"),

("Sopas",),
("130. Sopa De Choclo Vegetariana" ,"$4200"),
("131. Sopa Agripicante Vegetariana" ,"$4200"),
("132. Sopa De Algas Con Huevo Y Tofu" ,"$4900"),
("134. Sopa Tun-Fu" ,"$5500"),


("Platos Principales",),
("135. Fideo Revuelto Mixto Vegetariano ","$5700"),
("136. Bifun Salteado Mixto Vegetariano ","$6400"),
("137. Arroz Frito Mixto Vegetariano ","$4600"),
("138. Arroz Con Salsa Curry ","$5700"),
("139. Queso De Soja Revuelto ", "$7800 (Hongos Chinos Y Carne Vegetales)"),
("140. Queso De Soja A La Plancha" ,"$6100 (Con Salsa Sate)"),
("141. Chop Suey  Vegetariano ","$5100"),
("143. Verduras Revueltas ","$3700"),
("144. Carne De Soja Agridulce ","$5700"),
("145. Omelette De Jamón De Soja"," $5100"),
("146. Omelette De Papa Natural ","$4500"),
("147. Hongo, Champiñon Y Bambú Salteados ","$6600"),
("148. Filet Kingdom Vegetariano ","$8500"),
("149. Acusay Revuelto Con Tun-Fun ","$5700"),
("151. Buñuelos Agridulce Con Semillas De Sésamo ","$6100"),
("152. Panache De Verduras ","$5700"),

]

# Nombre del archivo CSV de salida
csv_file = "menu.csv"

# Escribir los datos en el archivo CSV
write_to_csv(data, csv_file)
