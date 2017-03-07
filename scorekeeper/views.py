from accounts.api.serializers import UserDetailSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data

    }
