FROM node:24-alpine

WORKDIR /app

# Copia só os arquivos de dependência primeiro para o Docker reaproveitar
# o cache do npm ci quando apenas o código mudar.
COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 5173

# --host faz o Vite aceitar conexões de fora do container.
CMD ["npm", "run", "dev", "--", "--host"]
