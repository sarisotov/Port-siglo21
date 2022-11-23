class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self,plato):
        id= str(plato.id_plato)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "plato_id": plato.id_plato,
                "nombre": plato.nom_plato,
                "acumulado": plato.valor_plato,
                "cantidad":1
            }
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] += plato.valor_plato
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self,plato):
        id = str(plato.id_plato)
        if id in self.carrito:
            del self.carrito[id]
            self. guardar_carrito()
    
    def restar (self, plato):
        id = str(plato.id_plato)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["acumulado"]-=plato.valor_plato
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(plato)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
