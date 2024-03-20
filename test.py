import requests

url = "https://www.newslive.com/business/cnbc-live-free.html"

payload = "{\n  \"aps\": {\n\t\"alert\": {\n\t\t\"title\": \"Example Title\",\n\t\t\"body\": \"Example Body\"\n\t},\n\t\"badge\": 1,\n\t\"sound\": \"default\"\n\n  }\n  }"
headers = {
  'Content-Type': 'text/plain',
  'Authorization': 'Bearer RzBFAiAz_oms2E55XZ65aQfpK1vXrfMIysj2e7cu3D2YBbPWHAIhAOctdvucbpNoQV9VG9X0sd_DlRuQZxLbhsfdH2hrnE9keyJ1IjoxLCJlIjoiMjAyNC0wMS0yNVQyMzowMDowMC4wMDArMDA6MDAifQ'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
