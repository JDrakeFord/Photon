from supabase import create_client, Client

url: str = "https://tlffgfsjbhdveweghjuc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
           ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRsZmZnZnNqYmhkdmV3ZWdoan" \
           "VjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3MTYyNDQsImV4cCI6MTk5M" \
           "TI5MjI0NH0.TIp6h3hPT9mVW6kSeWgI21fHFVc_kVSUZmSdEP5APrY"
supabase: Client = create_client(url, key)


def getCodename(first_name, last_name) -> str:
    r = supabase.from_('player').select("codename").eq('first_name', first_name).eq('last_name', last_name).execute()
    return r.data[0]['codename']


def newPlayer(first_name, last_name, codename):
    r = supabase.from_('player').insert({
        'first_name': first_name,
        'last_name': last_name,
        'codename': codename
    }).execute()
    return r.data

def checkIfPlayerExists(first_name, last_name):
    r = supabase.from_('player').select('*').eq('first_name', first_name).eq('last_name', last_name).execute()
    return bool(r.data)
