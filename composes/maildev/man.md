Github: https://github.com/maildev/maildev

```sh
curl --url 'smtp://localhost:25' \
  --mail-from 'seu_email@gmail.com' \
  --mail-rcpt 'destinatario@example.com' \
  --upload-file - <<END
From: seu_email@gmail.com
To: destinatario@example.com
Subject: Assunto do e-mail
Corpo do e-mail.
END
```