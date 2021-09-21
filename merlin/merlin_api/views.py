from rest_framework import viewsets
from merlin.serializers import DevicesSerializer, LearnACLSerializer, LearnARPSerializer, LearnARPStatisticsSerializer, LearnBGPInstancesSerializer, LearnBGPRoutesPerPeerSerializer, LearnBGPTablesSerializer, LearnInterfaceSerializer, LearnVLANSerializer, LearnVRFSerializer, ParseShowInventorySerializer, ParseShowIPIntBriefSerializer, ParseShowVersionSerializer
from merlin.models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnInterface, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all().order_by('timestamp')
    serializer_class = DevicesSerializer

class LearnACLViewSet(viewsets.ModelViewSet):
    queryset = LearnACL.objects.all().order_by('timestamp')
    serializer_class = LearnACLSerializer

class LearnARPViewSet(viewsets.ModelViewSet):
    queryset = LearnARP.objects.all().order_by('timestamp')
    serializer_class = LearnARPSerializer

class LearnARPStatisticsViewSet(viewsets.ModelViewSet):
    queryset = LearnARPStatistics.objects.all().order_by('timestamp')
    serializer_class = LearnARPStatisticsSerializer    

class LearnBGPInstancesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPInstances.objects.all().order_by('timestamp')
    serializer_class = LearnBGPInstancesSerializer

class LearnBGPRoutesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPRoutesPerPeer.objects.all().order_by('timestamp')
    serializer_class = LearnBGPRoutesPerPeerSerializer    

class LearnBGPTablesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPTables.objects.all().order_by('timestamp')
    serializer_class = LearnBGPTablesSerializer

class LearnInterfaceViewSet(viewsets.ModelViewSet):
    queryset = LearnInterface.objects.all().order_by('timestamp')
    serializer_class = LearnInterfaceSerializer

class LearnVLANViewSet(viewsets.ModelViewSet):
    queryset = LearnVLAN.objects.all().order_by('timestamp')
    serializer_class = LearnVLANSerializer

class LearnVRFViewSet(viewsets.ModelViewSet):
    queryset = LearnVRF.objects.all().order_by('timestamp')
    serializer_class = LearnVRFSerializer

class ShowInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShowInventory.objects.all().order_by('timestamp')
    serializer_class = ParseShowInventorySerializer

class ShowIPIntBriefViewSet(viewsets.ModelViewSet):
    queryset = ShowIPIntBrief.objects.all().order_by('timestamp')
    serializer_class = ParseShowIPIntBriefSerializer 

class ShowVersionViewSet(viewsets.ModelViewSet):
    queryset = ShowVersion.objects.all().order_by('timestamp')
    serializer_class = ParseShowVersionSerializer    