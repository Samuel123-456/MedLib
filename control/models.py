from uuid import uuid4

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

extra_fields = {"null": True, "blank": True}


class Reader(models.Model):
    """
    Model Reader (Leitor/User/Estudante)

    Contém informações sobre um leitor ou aluno, incluindo dados associados como:
    número de processo, turma (group), classe (grade), curso e um identificador único (UID) para chamadas
    de URL.

    Atributos:
    - user: Relacionamento de um-para-um com o modelo User
    - process_number: Número de processo único para cada aluno
    - grade: Classe do aluno, especificada com opções predefinidas (10, 11, 12).
    - course: Curso em que o aluno está matriculado, com as seguintes opções: Informática ou Eletrônica.
    - group: Turma do aluno, com as seguintes opções: A, B, C ou D.
    - uid: Identificador único (UUID) gerado automaticamente para facilitar chamadas de URL e outras referências únicas.
    """

    GRADE_CHOICES = [
        ("10", "Décima"),
        ("11", "Décima Primeira"),
        ("12", "Décima Segunda"),
        ("13", "Décima Terceira"),
    ]

    GROUP_CHOICES = [
        ("A", "Turma A"),
        ("B", "Turma B"),
        ("C", "Turma C"),
        ("D", "Turma D"),
    ]

    COURSE_CHOICES = [
        ("Informática", "Informática"),
        ("Eletrónica", "Eletrónica"),
    ]

    photo = models.ImageField(upload_to="profile-photos/", **extra_fields)
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name="reader", **extra_fields
    )
    process_number = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(1),
        ],
        verbose_name="Número de Processo",
        **extra_fields
    )
    grade = models.CharField(verbose_name="Classe", max_length=3, choices=GRADE_CHOICES, **extra_fields)
    course = models.CharField(
        verbose_name="Curso", max_length=30, choices=COURSE_CHOICES, **extra_fields
    )
    group = models.CharField(verbose_name="Turma", max_length=1, choices=GROUP_CHOICES, **extra_fields)
    uid = models.UUIDField(
        verbose_name="Identificador Universal",
        default=uuid4,
        unique=True,
        editable=False,
        **extra_fields
    )

    def __str__(self):
        return f"{self.user.username} ({self.grade}-{self.group})"
