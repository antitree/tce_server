"""
Django settings for tce_server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4ox49@&w$e4x25ces9mvh3fc$9=k04l!0!!5+9fb)7od=0h=ou'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG_PROPAGATE_EXCEPTIONS = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',

    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tce_server.urls'

WSGI_APPLICATION = 'tce_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


GPG_PUBLIC_KEY = u'-----BEGIN PGP PUBLIC KEY BLOCK-----\n\n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\n=oMPC\n-----END PGP PUBLIC KEY BLOCK-----\n'
GPG_PRIVATE_KEY = u'-----BEGIN PGP PRIVATE KEY BLOCK-----\n\n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\n5EPGV0yLYWCaN77IMUVBtl9s\n=Fykn\n-----END PGP PRIVATE KEY BLOCK-----\n'
GPG_FINGERPRINT = u'4BAEFBEDFFAB7CBC20C6E320E63F53384E8A76A6'

P_VALUE = 921355984572641311672343424898410239406765173564481049529310998437412969038866770004018133863821119723063474210217706973316313378613043770818780115988652746380714841456142639704626352778746695851788302212813071729066781855064705915608677688092341542568424482925462180633889723579377448564293509252435087477281161286147259728549498972138533165527662691306617571151999644107722686129055657829181973528055808318168063541650472028439642172128232391355303186171522887793994216888734434516097403106470551045418225907760866937899119453358993949368302899196593348587781289829114461181435009345801458736138423284445935647778071510107564961338155282235194713303681529865383261800265733083885319259454542964149249843475773904339566680218460878240048849309064731923166303421897726591880342754670170435647389065546266133258192653962148274540863521430747245658342533592543361748499215018089153994702237916350245910933537662925365405565771274120172582583500547352310022433066022690275959677696743489993411404619219133001998952984404232404962367594198986426803887303895347014868878166590277345633941382072502883955197749732581385414098128645307956625290745193548601504669931868639779915942610143766629826114677053173092959998726060927521195420788443
G_VALUE = 663967539726681103144465862624023347327698702596964472546454820612078529024826511081834885051391640561027926017836691699314236534541923660174228237481359399239083180745492344196240271583191901030943363158476402690866816165544413727642448467281613902744460740068022342814226536910981053149313200570584734433264322026211121298776746854224456594445267601706025601843269197307467696022013820314999017250076524215045953776140607347805724914635970896016787967508383404799474484032431598064588430204717282130624030236791313438685820994454800688074168393190968240421774957367364475227967115216643497513476439355774507681852727818225180294894690159121962082595832983558603527661891598029737473340045490056765931576922756721299050664825278351270156746074608877854067592917025359654086073944428436312956493450184334004168961635631284623451494433780460973694438069529748624269922713354688628667211254835640052369781611093104976907294716270650398203701503416097526621503515524050090620184511166507246300606992283420185768295268028274863932225993620378369739945955786054094149373142999987843559918951091147136538232655389152381266513956594698580925978254637104203194517867999160375927926123576218934330517623079023322032849247628255803444186962170
RECOVERY_THRESHOLD = 2

CREATE_KEY_FILE_JAR = os.path.join(os.path.dirname(BASE_DIR), 'java/out/artifacts/tce_server_jar/tce_server.jar')