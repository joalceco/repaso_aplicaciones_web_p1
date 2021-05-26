from app import app
from flask import render_template
from app.forms import HonorariosForm


def calculo_honorarios(honorarios):
    iva = (0.16)
    r_iva = (0.1066666666)
    r_isr = (0.10)
    subtotal = honorarios+honorarios*iva
    neto = subtotal-(honorarios*r_iva)-(honorarios*r_isr)
    return neto

@app.route("/", methods=["GET", "POST"])
# @app.route("/index")
def index():
    form = HonorariosForm()
    if form.validate_on_submit():
        honorarios = float(form.honorarios.data)
        neto = calculo_honorarios(honorarios)
        return render_template("resultado.html", honorarios=honorarios, neto=neto)
    return render_template("index.html", form=form)