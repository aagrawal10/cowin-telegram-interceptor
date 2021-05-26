FROM akhmetov/python-telegram:latest

WORKDIR /code

ARG telegram_api_id
RUN test -n "${telegram_api_id}"

ARG telegram_api_hash
RUN test -n "${telegram_api_hash}"

ARG telegram_number
RUN test -n "${telegram_number}"

ARG db_encryption_key
RUN test -n "${db_encryption_key}"

ENV TELEGRAM_API_ID ${telegram_api_id}
ENV TELEGRAM_API_HASH ${telegram_api_hash}
ENV TELEGRAM_NUMBER ${telegram_number}
ENV DB_ENCRYPTION_KEY ${db_encryption_key}

COPY . ./

ENTRYPOINT [ "python", "telegram_interceptor.py" ]
