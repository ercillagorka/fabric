fabric
======
<p>Egilea:         gorka ercilla, ercillagorka@gmail.com</p>
<p>server:         Ubuntu 12.04</p>
##Zer egiten du:
            * 1) Linux eta python pakete guztiak instalatzen ditu django projectua martzan jartzeko ubuntu serbidore batetan.
            * 2) Edo zure ordenagailu lokalean dituzun aldaketak edo githubean dituzun aldaketak serbidorean eguneratzen ditu.

##Zer egiten du:
Script honek fabric instalatuta eukitzea eskatzen dotzu. => (http://docs.fabfile.org/en/1.7/)
              fabric tresna aukera ematen deu script berean, tokiko eta urruneko komandoak ejekutatzeko eta hedapena gidoiak sortzeko
              Script honek (fabfile.py) projektuaren karpetan egon behar da:
            *  1) Urruneko zerbitzari batera konektatuko da eta zure Django proiektua hedatzeko behar diren paketeak instalatuko ditu Ubuntu sistema batetan.
                 ==> Python paketeak PIP bidez instalatuko dira (http://www.pip-installer.org/) virtualenv ingurunean eta virtualenvwrapper erabiliz (tualenvwrapper.readthedocs.org).
                        PIP badaki zer instalatu behar duen proiektuaren karpetan requirements.txt fitxeroan jarrita dagoelako. (fabfile.py dagoen karpetan)
                 ==> Python paketeak ez dira, ohi bezala instalatutako Ubuntu zerbitzarian.
            *  2) Zip zure git proiektua eta kopiatu urruneko zerbitzaria, sortu "bertsioa" karpeta eta deskonprimitu kodea han.
                  Urruneko karpeta jada existitzen bada huts egingo du.
            *  3) Instalatu zure aplikazioa nginx eta gunicorn zerbitzarian