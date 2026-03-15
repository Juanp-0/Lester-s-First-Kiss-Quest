class Ligue(Personaje):
    def __init__(self,nombre,nv_carisma,estado_relacion_xp):
        super().__init__( nv_carisma)
        self.nombre = nombre
        self.estado_relacion = ["Nulo", "Interesada", "Amigos", "Quedantes", "Novios"]
        self.estado_relacion_xp = estado_relacion_xp
    
    # Getters y Setters
    def get_nombre(self):
        return self.nombre
    
    def get_estado_relacion(self):
        return self.estado_relacion
    
    def get_estado_relacion_xp(self):
        return self.estado_relacion_xp
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_estado_relacion(self, estado_relacion):
        self.estado_relacion = estado_relacion
    
    def set_estado_relacion_xp(self, estado_relacion_xp):
        self.estado_relacion_xp = estado_relacion_xp
    
    # Métodos de utilidad
    def mostrar_estado_relacion(self):
        if self.estado_relacion_xp == 0:
            return self.estado_relacion[0]
        elif 1 <= self.estado_relacion_xp < 10:
            return self.estado_relacion[1]
        elif 10 <= self.estado_relacion_xp < 15:
            return self.estado_relacion[2]
        elif 15 <= self.estado_relacion_xp < 20:
            return self.estado_relacion[3]
        else:
            return self.estado_relacion[4]
    
    def sum_estado_relacion_xp(self, num):
        self.estado_relacion_xp += num
        if self.estado_relacion_xp > 20:
            self.estado_relacion_xp = 20
    
    def res_estado_relacion_xp(self, num):
        self.estado_relacion_xp -= num
        if self.estado_relacion_xp < 0:
            self.estado_relacion_xp = 0