FROM python:3.9
RUN useradd -m -u 1000 user
USER user
WORKDIR /app
COPY . /app
EXPOSE 7860
CMD ["sh", "hfcryptdecrypt.sh"]