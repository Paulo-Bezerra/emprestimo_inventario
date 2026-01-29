from django.db import models

# Create your models here.

class Usuario(models.Model):
    TIPO_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('SERVIDOR', 'Servidor')
    ]
    PERFIL_CHOICES = [
        ('COMUM', 'Comum'),
        ('OPERADOR', 'Operador'),
        ('GESTOR', 'Gestor'),
        ('ADMINISTRADOR', 'Administrador')
    ]
    matricula = models.CharField(max_length=14, unique=True, blank=False, null=False)
    nome = models.CharField(max_length=75, blank=False, null=False)
    tipo = models.CharField(max_length=8, blank=False, null=False, choices=TIPO_CHOICES)
    perfil = models.CharField(max_length=13, blank=False, null=False,choices=PERFIL_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Material(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False,)
    patrimonio = models.CharField(max_length=10, blank=True, null=False, default='')
    quantidade_total = models.PositiveIntegerField(default=0, blank=False, null=False)
    descricao = models.TextField(blank=True, null=False, default='')

    def __str__(self):
        return f"Cod. {self.pk} | {self.nome} ({self.descricao})"

    @property
    def quantidade_disponivel(self):
        emprestimos_ativos = self.emprestimos.filter(data_devolucao__isnull=True).count()
        return self.quantidade_total - emprestimos_ativos


class Emprestimo(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name='emprestimos'
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='emprestimos'
    )
    data_saida = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    observacao = models.TextField(null=False, blank=True, default='')

    def __str__(self):
        return f"{self.material.nome} - {self.usuario.nome}"

    def save(self, *args, **kwargs):
        if self.pk is None and self.material.quantidade_disponivel <= 0:
            raise ValueError(f"Não há estoque disponível para {self.material.nome}")
        super().save(*args, **kwargs)

    @property
    def data_devolucao_display(self):
        return self.data_devolucao or "Não devolvido"