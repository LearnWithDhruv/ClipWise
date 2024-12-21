from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Script
from .serializers import ScriptSerializer
from .openai_client import OpenAI
import os

class GenerateScriptAPIView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        language = request.data.get('language', 'English')

        api_key = os.getenv('XAI_API_KEY')
        if not api_key:
            return Response({'error': 'API key is not configured. Please set the XAI_API_KEY environment variable.'}, status=500)

        client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

        try:
            completion = client.chat.completions.create(
                model="grok-2-1212",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant responding in {language}."},
                    {"role": "user", "content": prompt}
                ]
            )
            content = completion.get("choices", [{}])[0].get("message", {}).get("content", "No response")

            script = Script.objects.create(content=content, language=language)
            return Response(ScriptSerializer(script).data)

        except Exception as e:
            return Response({'error': 'Failed to generate script', 'details': str(e)}, status=500)
