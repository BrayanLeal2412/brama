from pasajes.model import Pasajero

# Create your tests here.
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Pasajero.objects.create(primer_nombre='Mario', primer_apellido='Arias'

    def test_primer_nombre_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label=pasajero._meta.get_field('primer_nombre').verbose_name
        self.assertEquals(field_label,'primer nombre')

    def test_nacionalidad_length(self):
        pasajero=Pasajero.objects.get(id=1)
        max_length=pasajero._meta.get_field('primer_nombre').max_length
        self.assertEquals(max_length,50)

    def test_fecha_de_nacimiento_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label=pasajero._meta.get_field('fecha_de_nacimiento').verbose_name
        self.assertEquals(field_label,'10/03/2000')

    def test_nombre_completo_is_primer_apellido_comma_primer_nombre(self):
        pasajero=Pasajero.objects.get(id=1)
        expected_object_name = '%s, %s' % (pasajero.primer_apellido, pasajero.primer_nombre)
        self.assertEquals(expected_object_name,str(pasajero))



