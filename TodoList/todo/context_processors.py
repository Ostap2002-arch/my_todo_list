from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'Russian')
def date_today(request):
    return {
        'date_today' : date.today().strftime('%d %b').title()
    }
