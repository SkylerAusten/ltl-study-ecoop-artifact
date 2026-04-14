FROM mambaorg/micromamba:1.4.0

# copy requirements first for layer caching
COPY requirements.txt /tmp/requirements.txt

# create env and install conda + pip packages in one layer, then clean caches
RUN micromamba create -y -n myenv python=3.11 -c conda-forge spot pip && \
    micromamba run -n myenv pip install --no-cache-dir -r /tmp/requirements.txt && \
    micromamba clean --all --yes && \
    rm -f /tmp/requirements.txt || true

# default to SQLite in-memory backend
ENV DB_BACKEND=sqlite

# app code
COPY . /src
WORKDIR /src
EXPOSE 8080

# run directly inside the micromamba environment (no activate/conda init)
ENTRYPOINT ["micromamba", "run", "-n", "myenv", "python", "./src/app.py"]
