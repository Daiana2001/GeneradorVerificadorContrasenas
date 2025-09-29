"""
Conversor de Unidades (POO)
Soporta: Longitud (m, km, mi) | Peso (kg, lb) | Temperatura (C, F)
"""

class ConversorLongitud:
    """Convierte entre m, km, mi usando 'm' como unidad base interna."""
    _to_m = {"m": 1.0, "km": 1000.0, "mi": 1609.34}

    def convertir(self, valor: float, origen: str, destino: str) -> float:
        origen = origen.lower()
        destino = destino.lower()
        if origen not in self._to_m or destino not in self._to_m:
            raise ValueError("Unidades de longitud válidas: m, km, mi.")
        if origen == destino:
            return valor
        metros = valor * self._to_m[origen]       # paso a metros
        return metros / self._to_m[destino]       # de metros a destino


class ConversorPeso:
    """Convierte entre kg y lb usando 'kg' como base interna."""
    _to_kg = {"kg": 1.0, "lb": 0.45359237}

    def convertir(self, valor: float, origen: str, destino: str) -> float:
        origen = origen.lower()
        destino = destino.lower()
        if origen not in self._to_kg or destino not in self._to_kg:
            raise ValueError("Unidades de peso válidas: kg, lb.")
        if origen == destino:
            return valor
        kg = valor * self._to_kg[origen]
        return kg / self._to_kg[destino]


class ConversorTemperatura:
    """Convierte entre Celsius (c) y Fahrenheit (f)."""

    def convertir(self, valor: float, origen: str, destino: str) -> float:
        o = origen.lower()
        d = destino.lower()
        if o == d:
            return valor
        if o == "c" and d == "f":
            return (valor * 9/5) + 32
        if o == "f" and d == "c":
            return (valor - 32) * 5/9
        raise ValueError("Unidades de temperatura válidas: C, F.")


# ---------------- Utilidades de entrada ---------------- #

def _leer_numero(prompt: str) -> float:
    """Lee float robusto: acepta coma y punto decimal y reintenta si hay error."""
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print(" Entrada inválida. Escribí un número (ej: 12.5 o 12,5).")

def _leer_opcion(prompt: str, opciones: tuple[str, ...]) -> str:
    """Lee una opción válida de la tupla opciones (no sensible a mayúsculas)."""
    opciones_lower = tuple(x.lower() for x in opciones)
    while True:
        s = input(prompt).strip().lower()
        if s in opciones_lower:
            return s
        print(f" Opción inválida. Elegí entre: {', '.join(opciones)}")


# ---------------- Interfaz de consola ---------------- #

class MenuConsola:
    def __init__(self) -> None:
        self.longitud = ConversorLongitud()
        self.peso = ConversorPeso()
        self.temperatura = ConversorTemperatura()

    def _menu(self) -> None:
        print("\n=== Conversor de Unidades (POO) ===")
        print("1) Longitud (m, km, mi)")
        print("2) Peso (kg, lb)")
        print("3) Temperatura (C, F)")
        print("0) Salir")

    def ejecutar(self) -> None:
        try:
            while True:
                self._menu()
                opcion = input("Seleccioná una opción: ").strip()

                if opcion == "0":
                    print(" Saliendo... ¡Hasta luego!")
                    break

                elif opcion == "1":
                    print("\n--- Longitud ---")
                    valor = _leer_numero("Valor: ")
                    origen = _leer_opcion("Unidad origen (m/km/mi): ", ("m", "km", "mi"))
                    destino = _leer_opcion("Unidad destino (m/km/mi): ", ("m", "km", "mi"))
                    resultado = self.longitud.convertir(valor, origen, destino)
                    print(f" {valor} {origen} = {resultado:.6f} {destino}")

                elif opcion == "2":
                    print("\n--- Peso ---")
                    valor = _leer_numero("Valor: ")
                    origen = _leer_opcion("Unidad origen (kg/lb): ", ("kg", "lb"))
                    destino = _leer_opcion("Unidad destino (kg/lb): ", ("kg", "lb"))
                    resultado = self.peso.convertir(valor, origen, destino)
                    print(f" {valor} {origen} = {resultado:.6f} {destino}")

                elif opcion == "3":
                    print("\n--- Temperatura ---")
                    valor = _leer_numero("Valor: ")
                    origen = _leer_opcion("Unidad origen (C/F): ", ("c", "f"))
                    destino = _leer_opcion("Unidad destino (C/F): ", ("c", "f"))
                    resultado = self.temperatura.convertir(valor, origen, destino)
                    print(f" {valor}°{origen.upper()} = {resultado:.2f}°{destino.upper()}")

                else:
                    print(" Opción no válida, probá de nuevo.")
        except KeyboardInterrupt:
            print("\n Interrumpido por el usuario.")


# ---------------- Punto de entrada ---------------- #

def main() -> None:
    app = MenuConsola()
    app.ejecutar()

if __name__ == "__main__":
    main()