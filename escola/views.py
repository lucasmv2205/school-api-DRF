from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
  """Exibindo todos as matriculas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
  """Listando as matriculas de um aluno"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
  """ Listando alunos matriculados em um curso """
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosSerializer