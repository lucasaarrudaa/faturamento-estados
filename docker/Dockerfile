FROM ubuntu:latest

# Instalar dependências do MySQL Workbench
RUN apt-get update && \
    apt-get install -y wget libzip4 libglu1-mesa libgtk-3-0 libpng16-16 libmysqlclient21 libpcre3 libssl1.1 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libfontconfig1 libfreetype6 libxrandr2 libglib2.0-0 libgtk2.0-0 libnotify4 libnss3 libxss1 libasound2 libxt6 libxkbcommon-x11-0 libxkbcommon0 libpulse0 libv4l-0 libxshmfence1 xdg-utils && \
    rm -rf /var/lib/apt/lists/*

# Download do MySQL Workbench
RUN wget -O /tmp/mysql-workbench.deb https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-community_8.0.27-1ubuntu20.04_amd64.deb && \
    dpkg -i /tmp/mysql-workbench.deb && \
    rm /tmp/mysql-workbench.deb

# Executar o MySQL Workbench quando o contêiner iniciar
CMD ["/usr/bin/mysql-workbench"]

# docker build -t my-mysql-workbench-image .
