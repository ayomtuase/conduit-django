from conduit.apps.core.renderers import ConduitJSONRenderer

class  UserJSONRenderer(ConduitJSONRenderer):
	object_label = 'user'

	def render(self, data, media_type=None, renderer_context=None):				
		
		token = data.get('token', None)
		if token is not None and isinstance(token, bytes):
			data['token'] = token.decode(charset)

		return super(UserJSONRenderer, self).render(data)

			

		

		
