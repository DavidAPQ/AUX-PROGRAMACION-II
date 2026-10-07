# Libros clásicos en papel
class Libro:
    def __init__(self, titulo, autores, editorial, año_publicacion):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.año_publicacion = año_publicacion

    def datos(self):
        return ("Título: " + self.titulo + " | Autores: " + self.autores +
                " | Editorial: " + self.editorial + " | Año: " + str(self.año_publicacion))

    # Copia dato a dato en otro objeto
    def copiar(self):
        return Libro(self.titulo, self.autores, self.editorial, self.año_publicacion)


# Revistas en papel: mismas características que los libros + volumen, número y mes de salida
class Revista(Libro):
    def __init__(self, titulo, autores, editorial, año_publicacion, volumen, numero, mes_salida):
        super().__init__(titulo, autores, editorial, año_publicacion)
        self.volumen = volumen
        self.numero = numero
        self.mes_salida = mes_salida

    def datos(self):
        return (super().datos() + " | Volumen: " + str(self.volumen) +
                " | Número: " + str(self.numero) + " | Mes: " + self.mes_salida)

    def copiar(self):
        return Revista(self.titulo, self.autores, self.editorial, self.año_publicacion,
                       self.volumen, self.numero, self.mes_salida)


# Documentos en formato CD (libros, software): formato del CD y tipo de licencia
class DocumentoCD(Libro):
    def __init__(self, titulo, autores, editorial, año_publicacion, formato_cd, tipo_licencia):
        super().__init__(titulo, autores, editorial, año_publicacion)
        self.formato_cd = formato_cd
        self.tipo_licencia = tipo_licencia

    def datos(self):
        return (super().datos() + " | Formato CD: " + self.formato_cd +
                " | Licencia: " + self.tipo_licencia)

    def copiar(self):
        return DocumentoCD(self.titulo, self.autores, self.editorial, self.año_publicacion,
                           self.formato_cd, self.tipo_licencia)


# Revistas de investigación: son revistas con un campo de investigación
# (el año de publicación lo hereda de Libro)
class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autores, editorial, año_publicacion, volumen, numero,
                 mes_salida, campo_investigacion):
        super().__init__(titulo, autores, editorial, año_publicacion, volumen, numero, mes_salida)
        self.campo_investigacion = campo_investigacion

    def datos(self):
        return super().datos() + " | Campo de investigación: " + self.campo_investigacion

    def copiar(self):
        return RevistaInvestigacion(self.titulo, self.autores, self.editorial,
                                    self.año_publicacion, self.volumen, self.numero,
                                    self.mes_salida, self.campo_investigacion)


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = []

    def agregar(self, documento):
        self.documentos.append(documento)

    def contar_revistas(self):
        total = 0
        for documento in self.documentos:
            if isinstance(documento, Revista):
                total = total + 1
        return total

    def mostrar(self):
        print(self.nombre + " (" + str(len(self.documentos)) + " documentos):")
        for documento in self.documentos:
            print("  -", type(documento).__name__, "|", documento.datos())

    # b. Muestra quién tiene más revistas y quién tiene más documentos
    def mostrar_quien_tiene_mas(self, otra):
        if self.contar_revistas() > otra.contar_revistas():
            print("Más revistas:", self.nombre)
        elif otra.contar_revistas() > self.contar_revistas():
            print("Más revistas:", otra.nombre)
        else:
            print("Más revistas: empate")

        if len(self.documentos) > len(otra.documentos):
            print("Más documentos:", self.nombre)
        elif len(otra.documentos) > len(self.documentos):
            print("Más documentos:", otra.nombre)
        else:
            print("Más documentos: empate")

    # c. Todas las revistas a esta biblioteca (la primera) y todos los libros a la otra (la segunda)
    def trasladar(self, otra):
        for documento in list(otra.documentos):
            if isinstance(documento, Revista):
                otra.documentos.remove(documento)
                self.documentos.append(documento)

        for documento in list(self.documentos):
            if type(documento) == Libro:
                self.documentos.remove(documento)
                otra.documentos.append(documento)

    # d. Copia de seguridad: copiar dato a dato en otro objeto
    def copia_seguridad(self):
        copia = Biblioteca(self.nombre + " (copia)")
        for documento in self.documentos:
            copia.agregar(documento.copiar())
        return copia


def main():
    # b. Instanciar 2 bibliotecas
    biblioteca1 = Biblioteca("Biblioteca Central")
    biblioteca1.agregar(Libro("Don Quijote", "Miguel de Cervantes", "Cátedra", 1605))
    biblioteca1.agregar(Libro("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 1967))
    biblioteca1.agregar(Revista("National Geographic", "Equipo editorial", "RBA", 2023, 45, 3, "Marzo"))
    biblioteca1.agregar(DocumentoCD("Office 2019", "Microsoft", "Microsoft", 2019, "DVD", "Comercial"))

    biblioteca2 = Biblioteca("Biblioteca de Ciencias")
    biblioteca2.agregar(Libro("Física Universitaria", "Hugh Young y Roger Freedman", "Pearson", 2013))
    biblioteca2.agregar(Revista("Muy Interesante", "Equipo editorial", "Zinet Media", 2022, 12, 7, "Julio"))
    biblioteca2.agregar(RevistaInvestigacion("Revista de Biología Marina", "Ana Torres",
                                             "Universidad Nacional", 2021, 8, 2, "Febrero", "Biología"))

    print("=== Bibliotecas iniciales ===")
    biblioteca1.mostrar()
    biblioteca2.mostrar()

    print("\n=== Quién tiene más ===")
    biblioteca1.mostrar_quien_tiene_mas(biblioteca2)

    # c. Trasladar
    biblioteca1.trasladar(biblioteca2)
    print("\n=== Después de trasladar ===")
    biblioteca1.mostrar()
    biblioteca2.mostrar()

    # d. Copia de seguridad de las dos bibliotecas
    copia1 = biblioteca1.copia_seguridad()
    copia2 = biblioteca2.copia_seguridad()
    print("\n=== Copias de seguridad ===")
    copia1.mostrar()
    copia2.mostrar()


if __name__ == "__main__":
    main()