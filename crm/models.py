from django.db import models


class Company(models.Model):
    name = models.CharField("Nome", max_length=255)
    trade_name = models.CharField("Nome fantasia", max_length=255, blank=True)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True)
    segment = models.CharField("Segmento", max_length=100, blank=True)
    phone = models.CharField("Telefone", max_length=20, blank=True)
    email = models.EmailField("E-mail", blank=True)
    city = models.CharField("Cidade", max_length=100, blank=True)
    state = models.CharField("UF", max_length=2, blank=True)
    notes = models.TextField("Observações", blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Deal(models.Model):
    STAGE_CHOICES = [
        ('lead', 'Lead'),
        ('diagnostico', 'Diagnóstico'),
        ('proposta', 'Proposta'),
        ('negociacao', 'Negociação'),
        ('fechado', 'Fechado'),
    ]

    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('ganha', 'Ganha'),
        ('perdida', 'Perdida'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='lead')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    expected_close_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Activity(models.Model):
    TYPE_CHOICES = [
        ('ligacao', 'Ligação'),
        ('reuniao', 'Reunião'),
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('nota', 'Nota'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True)
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, blank=True, null=True)
    activity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    activity_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_activity_type_display()} - {self.company.name}"
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True)
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title