# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import accounting_pb2 as accounting__pb2
import backend_pb2 as backend__pb2
import comptracker_pb2 as comptracker__pb2
import discovery_pb2 as discovery__pb2
import services_pb2 as services__pb2


class JustVpnStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class JustVpnServicer(object):
  # missing associated documentation comment in .proto file
  pass


def add_JustVpnServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.JustVpn', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TrackerInfoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOriginalIP = channel.unary_unary(
        '/api.TrackerInfo/GetOriginalIP',
        request_serializer=services__pb2.IPmessage.SerializeToString,
        response_deserializer=services__pb2.IPmessage.FromString,
        )
    self.GetBlockLists = channel.unary_unary(
        '/api.TrackerInfo/GetBlockLists',
        request_serializer=services__pb2.IPmessage.SerializeToString,
        response_deserializer=services__pb2.AuthResponse.FromString,
        )


class TrackerInfoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOriginalIP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockLists(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrackerInfoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOriginalIP': grpc.unary_unary_rpc_method_handler(
          servicer.GetOriginalIP,
          request_deserializer=services__pb2.IPmessage.FromString,
          response_serializer=services__pb2.IPmessage.SerializeToString,
      ),
      'GetBlockLists': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockLists,
          request_deserializer=services__pb2.IPmessage.FromString,
          response_serializer=services__pb2.AuthResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.TrackerInfo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CompTrackerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.stream_stream(
        '/api.CompTracker/Connect',
        request_serializer=comptracker__pb2.AgentEvent.SerializeToString,
        response_deserializer=comptracker__pb2.CompTrackerEvent.FromString,
        )
    self.CheckLimits = channel.unary_unary(
        '/api.CompTracker/CheckLimits',
        request_serializer=comptracker__pb2.CheckLimitsRequest.SerializeToString,
        response_deserializer=comptracker__pb2.CheckLimitsResponse.FromString,
        )
    self.UserSessionList = channel.unary_unary(
        '/api.CompTracker/UserSessionList',
        request_serializer=comptracker__pb2.UserSessionListRequest.SerializeToString,
        response_deserializer=comptracker__pb2.UserSessionListResponse.FromString,
        )
    self.UserCounters = channel.unary_unary(
        '/api.CompTracker/UserCounters',
        request_serializer=comptracker__pb2.UserCountersRequest.SerializeToString,
        response_deserializer=comptracker__pb2.UserCountersResponse.FromString,
        )
    self.UserSessionCounters = channel.unary_unary(
        '/api.CompTracker/UserSessionCounters',
        request_serializer=comptracker__pb2.UserSessionCountersRequest.SerializeToString,
        response_deserializer=comptracker__pb2.UserSessionCountersResponse.FromString,
        )
    self.ProjectSessionList = channel.unary_stream(
        '/api.CompTracker/ProjectSessionList',
        request_serializer=services__pb2.ProjectSessionListRequest.SerializeToString,
        response_deserializer=comptracker__pb2.UserSession.FromString,
        )
    self.ServerList = channel.unary_unary(
        '/api.CompTracker/ServerList',
        request_serializer=comptracker__pb2.ServerListRequest.SerializeToString,
        response_deserializer=comptracker__pb2.ServerListResponse.FromString,
        )


class CompTrackerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Connect(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckLimits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserSessionList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserCounters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserSessionCounters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProjectSessionList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CompTrackerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Connect': grpc.stream_stream_rpc_method_handler(
          servicer.Connect,
          request_deserializer=comptracker__pb2.AgentEvent.FromString,
          response_serializer=comptracker__pb2.CompTrackerEvent.SerializeToString,
      ),
      'CheckLimits': grpc.unary_unary_rpc_method_handler(
          servicer.CheckLimits,
          request_deserializer=comptracker__pb2.CheckLimitsRequest.FromString,
          response_serializer=comptracker__pb2.CheckLimitsResponse.SerializeToString,
      ),
      'UserSessionList': grpc.unary_unary_rpc_method_handler(
          servicer.UserSessionList,
          request_deserializer=comptracker__pb2.UserSessionListRequest.FromString,
          response_serializer=comptracker__pb2.UserSessionListResponse.SerializeToString,
      ),
      'UserCounters': grpc.unary_unary_rpc_method_handler(
          servicer.UserCounters,
          request_deserializer=comptracker__pb2.UserCountersRequest.FromString,
          response_serializer=comptracker__pb2.UserCountersResponse.SerializeToString,
      ),
      'UserSessionCounters': grpc.unary_unary_rpc_method_handler(
          servicer.UserSessionCounters,
          request_deserializer=comptracker__pb2.UserSessionCountersRequest.FromString,
          response_serializer=comptracker__pb2.UserSessionCountersResponse.SerializeToString,
      ),
      'ProjectSessionList': grpc.unary_stream_rpc_method_handler(
          servicer.ProjectSessionList,
          request_deserializer=services__pb2.ProjectSessionListRequest.FromString,
          response_serializer=comptracker__pb2.UserSession.SerializeToString,
      ),
      'ServerList': grpc.unary_unary_rpc_method_handler(
          servicer.ServerList,
          request_deserializer=comptracker__pb2.ServerListRequest.FromString,
          response_serializer=comptracker__pb2.ServerListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.CompTracker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CompMasterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SlaveConnect = channel.unary_stream(
        '/api.CompMaster/SlaveConnect',
        request_serializer=comptracker__pb2.CompTrackerSlave.SerializeToString,
        response_deserializer=comptracker__pb2.CompTrackerMasterEvent.FromString,
        )


class CompMasterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SlaveConnect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CompMasterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SlaveConnect': grpc.unary_stream_rpc_method_handler(
          servicer.SlaveConnect,
          request_deserializer=comptracker__pb2.CompTrackerSlave.FromString,
          response_serializer=comptracker__pb2.CompTrackerMasterEvent.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.CompMaster', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class LimitsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/api.Limits/Get',
        request_serializer=backend__pb2.LimitsGetRequest.SerializeToString,
        response_deserializer=backend__pb2.TrafficLimits.FromString,
        )
    self.GetFull = channel.unary_unary(
        '/api.Limits/GetFull',
        request_serializer=backend__pb2.LimitsGetFullRequest.SerializeToString,
        response_deserializer=backend__pb2.FullTrafficLimits.FromString,
        )
    self.Set = channel.unary_unary(
        '/api.Limits/Set',
        request_serializer=backend__pb2.LimitsSetRequest.SerializeToString,
        response_deserializer=backend__pb2.LimitsSetResponse.FromString,
        )
    self.CountUsage = channel.unary_unary(
        '/api.Limits/CountUsage',
        request_serializer=backend__pb2.LimitsCountUsageRequest.SerializeToString,
        response_deserializer=backend__pb2.LimitsCountUsageResponse.FromString,
        )


class LimitsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFull(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CountUsage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LimitsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=backend__pb2.LimitsGetRequest.FromString,
          response_serializer=backend__pb2.TrafficLimits.SerializeToString,
      ),
      'GetFull': grpc.unary_unary_rpc_method_handler(
          servicer.GetFull,
          request_deserializer=backend__pb2.LimitsGetFullRequest.FromString,
          response_serializer=backend__pb2.FullTrafficLimits.SerializeToString,
      ),
      'Set': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=backend__pb2.LimitsSetRequest.FromString,
          response_serializer=backend__pb2.LimitsSetResponse.SerializeToString,
      ),
      'CountUsage': grpc.unary_unary_rpc_method_handler(
          servicer.CountUsage,
          request_deserializer=backend__pb2.LimitsCountUsageRequest.FromString,
          response_serializer=backend__pb2.LimitsCountUsageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Limits', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ConnectionSourceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Subscribe = channel.unary_stream(
        '/api.ConnectionSource/Subscribe',
        request_serializer=accounting__pb2.ConnectionSubscribeRequest.SerializeToString,
        response_deserializer=accounting__pb2.ConnectionEvent.FromString,
        )


class ConnectionSourceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Subscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConnectionSourceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Subscribe': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe,
          request_deserializer=accounting__pb2.ConnectionSubscribeRequest.FromString,
          response_serializer=accounting__pb2.ConnectionEvent.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.ConnectionSource', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NodeStorageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PutVpnSession = channel.unary_unary(
        '/api.NodeStorage/PutVpnSession',
        request_serializer=accounting__pb2.VpnSessionPutRequest.SerializeToString,
        response_deserializer=accounting__pb2.VpnSessionPutResponse.FromString,
        )
    self.DeleteVpnSession = channel.unary_unary(
        '/api.NodeStorage/DeleteVpnSession',
        request_serializer=accounting__pb2.VpnSessionDeleteRequest.SerializeToString,
        response_deserializer=accounting__pb2.VpnSessionDeleteResponse.FromString,
        )
    self.UpdateVpnSession = channel.unary_unary(
        '/api.NodeStorage/UpdateVpnSession',
        request_serializer=accounting__pb2.VpnSessionUpdateRequest.SerializeToString,
        response_deserializer=accounting__pb2.VpnSessionUpdateResponse.FromString,
        )
    self.ListVpnSession = channel.unary_unary(
        '/api.NodeStorage/ListVpnSession',
        request_serializer=accounting__pb2.VpnSessionListRequest.SerializeToString,
        response_deserializer=accounting__pb2.VpnSessionListResponse.FromString,
        )
    self.WatchVpnSession = channel.unary_stream(
        '/api.NodeStorage/WatchVpnSession',
        request_serializer=accounting__pb2.VpnSessionWatchRequest.SerializeToString,
        response_deserializer=accounting__pb2.VpnSessionWatchEvent.FromString,
        )


class NodeStorageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PutVpnSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteVpnSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateVpnSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListVpnSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchVpnSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodeStorageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PutVpnSession': grpc.unary_unary_rpc_method_handler(
          servicer.PutVpnSession,
          request_deserializer=accounting__pb2.VpnSessionPutRequest.FromString,
          response_serializer=accounting__pb2.VpnSessionPutResponse.SerializeToString,
      ),
      'DeleteVpnSession': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteVpnSession,
          request_deserializer=accounting__pb2.VpnSessionDeleteRequest.FromString,
          response_serializer=accounting__pb2.VpnSessionDeleteResponse.SerializeToString,
      ),
      'UpdateVpnSession': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateVpnSession,
          request_deserializer=accounting__pb2.VpnSessionUpdateRequest.FromString,
          response_serializer=accounting__pb2.VpnSessionUpdateResponse.SerializeToString,
      ),
      'ListVpnSession': grpc.unary_unary_rpc_method_handler(
          servicer.ListVpnSession,
          request_deserializer=accounting__pb2.VpnSessionListRequest.FromString,
          response_serializer=accounting__pb2.VpnSessionListResponse.SerializeToString,
      ),
      'WatchVpnSession': grpc.unary_stream_rpc_method_handler(
          servicer.WatchVpnSession,
          request_deserializer=accounting__pb2.VpnSessionWatchRequest.FromString,
          response_serializer=accounting__pb2.VpnSessionWatchEvent.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.NodeStorage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NodeAuthenticatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Auth = channel.unary_unary(
        '/api.NodeAuthenticator/Auth',
        request_serializer=services__pb2.AuthRequest.SerializeToString,
        response_deserializer=services__pb2.AuthResponse.FromString,
        )
    self.ReportClientIP = channel.unary_unary(
        '/api.NodeAuthenticator/ReportClientIP',
        request_serializer=services__pb2.ReportClientIPRequest.SerializeToString,
        response_deserializer=services__pb2.ReportClientIPResponse.FromString,
        )
    self.GetPassByName = channel.unary_unary(
        '/api.NodeAuthenticator/GetPassByName',
        request_serializer=services__pb2.GetPassByNameRequest.SerializeToString,
        response_deserializer=services__pb2.GetPassByNameResponse.FromString,
        )
    self.RegisterAuthenticated = channel.unary_unary(
        '/api.NodeAuthenticator/RegisterAuthenticated',
        request_serializer=services__pb2.RegisterAuthenticatedRequest.SerializeToString,
        response_deserializer=services__pb2.RegisterAuthenticatedResponse.FromString,
        )


class NodeAuthenticatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Auth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReportClientIP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPassByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterAuthenticated(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodeAuthenticatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Auth': grpc.unary_unary_rpc_method_handler(
          servicer.Auth,
          request_deserializer=services__pb2.AuthRequest.FromString,
          response_serializer=services__pb2.AuthResponse.SerializeToString,
      ),
      'ReportClientIP': grpc.unary_unary_rpc_method_handler(
          servicer.ReportClientIP,
          request_deserializer=services__pb2.ReportClientIPRequest.FromString,
          response_serializer=services__pb2.ReportClientIPResponse.SerializeToString,
      ),
      'GetPassByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetPassByName,
          request_deserializer=services__pb2.GetPassByNameRequest.FromString,
          response_serializer=services__pb2.GetPassByNameResponse.SerializeToString,
      ),
      'RegisterAuthenticated': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterAuthenticated,
          request_deserializer=services__pb2.RegisterAuthenticatedRequest.FromString,
          response_serializer=services__pb2.RegisterAuthenticatedResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.NodeAuthenticator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NodeResolverStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Resolve = channel.unary_unary(
        '/api.NodeResolver/Resolve',
        request_serializer=services__pb2.ResolveRequest.SerializeToString,
        response_deserializer=services__pb2.ResolveResponse.FromString,
        )


class NodeResolverServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Resolve(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodeResolverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Resolve': grpc.unary_unary_rpc_method_handler(
          servicer.Resolve,
          request_deserializer=services__pb2.ResolveRequest.FromString,
          response_serializer=services__pb2.ResolveResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.NodeResolver', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class UnifiedVpnServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SessionSubscribe = channel.unary_stream(
        '/api.UnifiedVpnService/SessionSubscribe',
        request_serializer=services__pb2.SessionSubscribeRequest.SerializeToString,
        response_deserializer=services__pb2.SessionSubscribeEvent.FromString,
        )
    self.SessionList = channel.unary_unary(
        '/api.UnifiedVpnService/SessionList',
        request_serializer=services__pb2.SessionListRequest.SerializeToString,
        response_deserializer=services__pb2.SessionListResponse.FromString,
        )
    self.SessionKill = channel.unary_unary(
        '/api.UnifiedVpnService/SessionKill',
        request_serializer=services__pb2.SessionKillRequest.SerializeToString,
        response_deserializer=services__pb2.SessionKillResponse.FromString,
        )


class UnifiedVpnServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SessionSubscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SessionList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SessionKill(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UnifiedVpnServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SessionSubscribe': grpc.unary_stream_rpc_method_handler(
          servicer.SessionSubscribe,
          request_deserializer=services__pb2.SessionSubscribeRequest.FromString,
          response_serializer=services__pb2.SessionSubscribeEvent.SerializeToString,
      ),
      'SessionList': grpc.unary_unary_rpc_method_handler(
          servicer.SessionList,
          request_deserializer=services__pb2.SessionListRequest.FromString,
          response_serializer=services__pb2.SessionListResponse.SerializeToString,
      ),
      'SessionKill': grpc.unary_unary_rpc_method_handler(
          servicer.SessionKill,
          request_deserializer=services__pb2.SessionKillRequest.FromString,
          response_serializer=services__pb2.SessionKillResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.UnifiedVpnService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class DiscoveryServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ServerList = channel.unary_unary(
        '/api.DiscoveryService/ServerList',
        request_serializer=discovery__pb2.DiscoveryServerListRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryServerListResponse.FromString,
        )
    self.Request = channel.unary_unary(
        '/api.DiscoveryService/Request',
        request_serializer=discovery__pb2.DiscoveryRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryResponse.FromString,
        )
    self.LocationList = channel.unary_unary(
        '/api.DiscoveryService/LocationList',
        request_serializer=discovery__pb2.DiscoveryLocationListRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryLocationListResponse.FromString,
        )
    self.PrivateServerGroup = channel.unary_unary(
        '/api.DiscoveryService/PrivateServerGroup',
        request_serializer=discovery__pb2.DiscoveryPrivateServerGroupRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryPrivateServerGroupResponse.FromString,
        )
    self.GetPool = channel.unary_unary(
        '/api.DiscoveryService/GetPool',
        request_serializer=discovery__pb2.DiscoveryGetPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryGetPoolResponse.FromString,
        )
    self.PutPool = channel.unary_unary(
        '/api.DiscoveryService/PutPool',
        request_serializer=discovery__pb2.DiscoveryPutPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryPutPoolResponse.FromString,
        )
    self.PatchPool = channel.unary_unary(
        '/api.DiscoveryService/PatchPool',
        request_serializer=discovery__pb2.DiscoveryPatchPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryPatchPoolResponse.FromString,
        )
    self.ListPool = channel.unary_unary(
        '/api.DiscoveryService/ListPool',
        request_serializer=discovery__pb2.DiscoveryListPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryListPoolResponse.FromString,
        )
    self.ListServersPool = channel.unary_unary(
        '/api.DiscoveryService/ListServersPool',
        request_serializer=discovery__pb2.DiscoveryListServersPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryListServersPoolResponse.FromString,
        )
    self.CopyPool = channel.unary_unary(
        '/api.DiscoveryService/CopyPool',
        request_serializer=discovery__pb2.DiscoveryCopyPoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryCopyPoolResponse.FromString,
        )
    self.DeletePool = channel.unary_unary(
        '/api.DiscoveryService/DeletePool',
        request_serializer=discovery__pb2.DiscoveryDeletePoolRequest.SerializeToString,
        response_deserializer=discovery__pb2.DiscoveryDeletePoolResponse.FromString,
        )


class DiscoveryServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ServerList(self, request, context):
    """server list by specific requirements, not used
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Request(self, request, context):
    """request servers from pool
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LocationList(self, request, context):
    """list of avalable locations for the pool
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PrivateServerGroup(self, request, context):
    """get list of private groups in pool - not used
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPool(self, request, context):
    """get complete pool description
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutPool(self, request, context):
    """create or replace pool entirely
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PatchPool(self, request, context):
    """make some changes to existing pool
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPool(self, request, context):
    """list of pools
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListServersPool(self, request, context):
    """list servers in pool, for dashboard mapping edit purposes
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CopyPool(self, request, context):
    """copy pool, required read permissions on original pool, but copy will have full access
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePool(self, request, context):
    """delete pool
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiscoveryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ServerList': grpc.unary_unary_rpc_method_handler(
          servicer.ServerList,
          request_deserializer=discovery__pb2.DiscoveryServerListRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryServerListResponse.SerializeToString,
      ),
      'Request': grpc.unary_unary_rpc_method_handler(
          servicer.Request,
          request_deserializer=discovery__pb2.DiscoveryRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryResponse.SerializeToString,
      ),
      'LocationList': grpc.unary_unary_rpc_method_handler(
          servicer.LocationList,
          request_deserializer=discovery__pb2.DiscoveryLocationListRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryLocationListResponse.SerializeToString,
      ),
      'PrivateServerGroup': grpc.unary_unary_rpc_method_handler(
          servicer.PrivateServerGroup,
          request_deserializer=discovery__pb2.DiscoveryPrivateServerGroupRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryPrivateServerGroupResponse.SerializeToString,
      ),
      'GetPool': grpc.unary_unary_rpc_method_handler(
          servicer.GetPool,
          request_deserializer=discovery__pb2.DiscoveryGetPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryGetPoolResponse.SerializeToString,
      ),
      'PutPool': grpc.unary_unary_rpc_method_handler(
          servicer.PutPool,
          request_deserializer=discovery__pb2.DiscoveryPutPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryPutPoolResponse.SerializeToString,
      ),
      'PatchPool': grpc.unary_unary_rpc_method_handler(
          servicer.PatchPool,
          request_deserializer=discovery__pb2.DiscoveryPatchPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryPatchPoolResponse.SerializeToString,
      ),
      'ListPool': grpc.unary_unary_rpc_method_handler(
          servicer.ListPool,
          request_deserializer=discovery__pb2.DiscoveryListPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryListPoolResponse.SerializeToString,
      ),
      'ListServersPool': grpc.unary_unary_rpc_method_handler(
          servicer.ListServersPool,
          request_deserializer=discovery__pb2.DiscoveryListServersPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryListServersPoolResponse.SerializeToString,
      ),
      'CopyPool': grpc.unary_unary_rpc_method_handler(
          servicer.CopyPool,
          request_deserializer=discovery__pb2.DiscoveryCopyPoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryCopyPoolResponse.SerializeToString,
      ),
      'DeletePool': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePool,
          request_deserializer=discovery__pb2.DiscoveryDeletePoolRequest.FromString,
          response_serializer=discovery__pb2.DiscoveryDeletePoolResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.DiscoveryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
