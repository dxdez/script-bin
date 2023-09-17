# Use the php:8.2-alpine image as the base image
FROM php:8.2-alpine

# Arguments defined in docker-compose.yml
ARG user
ARG uid

# Install system dependencies and necessary build tools
RUN apk update && apk add --no-cache \
    git \
    curl \
    libpng-dev \
    libjpeg-turbo-dev \
    libwebp-dev \
    libxpm-dev \
    libxml2-dev \
    zip \
    unzip \
    oniguruma-dev

# Clear cache
RUN rm -rf /var/cache/apk/*

# Set environment variables for oniguruma
ENV PKG_CONFIG_PATH=/usr/lib/pkgconfig
ENV ONIG_CFLAGS=-I/usr/include
ENV ONIG_LIBS=-lonig

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Create system user to run Composer and Artisan Commands
RUN adduser -D -u $uid -h /home/$user $user && \
    mkdir -p /home/$user/.composer && \
    chown -R $user:$user /home/$user

# Set working directory
WORKDIR /var/www

USER $user

