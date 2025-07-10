FROM --platform=linux/amd64 tryton/tryton:7.6

# Cambiar a root para instalar módulos
USER root


RUN pip install --break-system-packages \
    trytond_sale trytond_stock \
    trytond_account trytond_account_invoice \
    trytond_account_invoice_stock trytond_company \
    trytond_country trytond_currency trytond_party \
    trytond_product

# Volver a usuario 'tryton'
COPY modules/ /opt/trytond/modules/


USER tryton