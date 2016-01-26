from rest_framework import viewsets
from rest_framework.response import Response
from django_apogee.models import InsAdmEtp, InsAdmEtpInitial, Individu
from django_apogee.serializers import (InsAdmEtpSerializer,
                                       InsAdmEtpInitialSerializer,
                                       IndividuSerializer,
                                      )

class InsAdmEtpViewSet(viewsets.ModelViewSet):
    queryset = InsAdmEtp.objects.all()
    serializer_class = InsAdmEtpSerializer
    paginate_by = 100

    def list(self, request):
        if request.GET.get('cod_anu', None):
            self.queryset = InsAdmEtp.objects.filter(cod_anu__in=request.GET.getlist('cod_anu'))

        return super(InsAdmEtpViewSet, self).list(request)

class InsAdmEtpInitialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsAdmEtpInitial.objects.using('oracle').all()
    serializer_class = InsAdmEtpInitialSerializer
    paginate_by = 100

    def list(self, request):
        if request.GET.get('cod_anu', None):
            self.queryset = InsAdmEtpInitial.objects.using('oracle').filter(cod_anu__in=request.GET.getlist('cod_anu'))

        return super(InsAdmEtpInitialViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        try:
            cod_anu, cod_ind, cod_etp, cod_vrs_vet, num_occ_iae = pk.split('|')
            inscription = InsAdmEtpInitial.objects.using('oracle').filter(cod_anu=cod_anu,
                                                        cod_ind=cod_ind,
                                                        cod_etp=cod_etp,
                                                        cod_vrs_vet=cod_vrs_vet,
                                                        num_occ_iae=num_occ_iae)[0]
            return Response(self.serializer_class(inscription).data)

        except:
            return super(InsAdmEtpInitialViewSet, self).retrieve(request, pk)


class IndividuViewSet(viewsets.ModelViewSet):
    queryset = Individu.objects.using('oracle').all()
    serializer_class = IndividuSerializer
    paginate_by = 100
