# M1992 Programming in the Scientific Environment
# Simple image with Python 3.11 and main scientific libraries

FROM python:3.11-bullseye

LABEL author="jorge.duarte.campderros@cern.ch" \
      version="1.1" \
      description="Docker image for M1992-Python with main scientific libraries"

# 🔧 Actualitza i instal·la dependències de sistema bàsiques
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
    && rm -rf /var/lib/apt/lists/*

# 📦 Instal·la llibreries científiques amb pip
RUN pip install --no-cache-dir numpy scipy matplotlib pandas

# ⚙️ Instal·la tini (per evitar problemes amb PID 1)
ENV TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# 👤 Crear un usuari estàndard
ARG username=pythoner
RUN useradd --create-home --home-dir /home/${username} ${username}
ENV HOME=/home/${username}

# 📂 Directori de treball compartit amb el host
WORKDIR /gate
RUN chown -R ${username}:${username} /gate

# 👥 Canvia a l’usuari estàndard
USER ${username}

# 🚀 Usa tini com a entrypoint per evitar problemes amb processos zombies
ENTRYPOINT ["/tini", "--"]

# 🔍 Comanda per defecte: obrir una shell de Python
CMD ["python3"]
