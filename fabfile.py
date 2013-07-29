"""
Egilea:         gorka ercilla, ercillagorka@gmail.com
server:         Ubuntu 12.04
Zer egiten du:
             1) Linux eta python pakete guztiak instalatzen ditu django projectua martzan jartzeko ubuntu serbidore batetan.
             2) Edo zure ordenagailu lokalean dituzun aldaketak edo githubean dituzun aldaketak serbidorean eguneratzen ditu.

Zer egiten du: Script honek fabric instalatuta eukitzea eskatzen dotzu. => (http://docs.fabfile.org/en/1.7/)
              fabric tresna aukera ematen deu script berean, tokiko eta urruneko komandoak ejekutatzeko eta hedapena gidoiak sortzeko
              Script honek (fabfile.py) projektuaren karpetan egon behar da:
              1) Urruneko zerbitzari batera konektatuko da eta zure Django proiektua hedatzeko behar diren paketeak instalatuko ditu Ubuntu sistema batetan.
                 ==> Python paketeak PIP bidez instalatuko dira (http://www.pip-installer.org/) virtualenv ingurunean eta virtualenvwrapper erabiliz (tualenvwrapper.readthedocs.org).
                        PIP badaki zer instalatu behar duen proiektuaren karpetan requirements.txt fitxeroan jarrita dagoelako. (fabfile.py dagoen karpetan)
                 ==> Python paketeak ez dira, ohi bezala instalatutako Ubuntu zerbitzarian.
              2) Zip zure git proiektua eta kopiatu urruneko zerbitzaria, sortu "bertsioa" karpeta eta deskonprimitu kodea han.
                  Urruneko karpeta jada existitzen bada huts egingo du.
              3) Instalatu zure aplikazioa nginx eta gunicorn zerbitzarian
"""

from fabric.api import *
from fabric.operations import *

# globals
env.project_name = 'webme'


def environment():
    #     Erabiltzaile lokala, ta bardine serbidorean errazago izateko.
    env.user = 'gorka'
    #     Serbitzariaren ip-a, bat baino gehiago izen al da [192.168.14.1 , 192.168.14.2 , 192.168.14.3]
    env.hosts = ['184.106.152.183']
    env.deploy_user = 'gorka'
    #     virtualenv egongo dan lekua
    env.virtualenv = '$HOME/.virtualenvs'
    #     virtualenv proiektuaren izena
    env.virtualenvwrapper = env.project_name
    #     virtuallenvwrapper aktibetako
    env.activate = 'workon %s' % (env.virtualenvwrapper)
    #     This path is used to change permissions
    env.code_root_parent = "/var/www"
    #     whole_path looks like /var/www/releases/1/webme
    #     This is where the code really is
    env.whole_path = "%s/%s/" % (env.code_root_parent, env.project_name)
