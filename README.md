# Telegram Bot

## Описание
Бот для автоматической генерации и публикации постов в Telegram-канале, посвященном криптовалютам. Использует OpenAI GPT для генерации текста и DALL·E для создания изображений.

## Основные функции
1. **Мониторинг референсных каналов**:
   - Чтение сообщений из каналов через Telegram аккаунт.
   - Передача данных боту для анализа и генерации постов.
   
2. **Генерация постов**:
   - Использование OpenAI GPT для создания контента.
   - Выбор между оригинальными изображениями и генерацией через DALL·E.

3. **Проверка вебхука**:
   - Установка и верификация вебхука для Telegram бота.

## Состав проекта
- `bot.py`: Основной файл для запуска бота.
- `webhook_helper.py`: Установка и проверка вебхука.
- `monitor_channels.py`: Мониторинг референсных каналов через Telegram аккаунт.
- `bot_content_processing.py`: Обработка контента, полученного от аккаунта.
- `openai_helper.py`: Функции для интеграции с OpenAI GPT и DALL·E.
- `.env`: Конфигурация токенов и настроек.
- `requirements.txt`: Список зависимостей.
- `telegram-bot.service`: Файл для автозапуска через systemd.

## Шаги для запуска

### 1. Установите виртуальную машину на Google Cloud
1. Перейдите в Google Cloud Console.
2. Выберите **Compute Engine** > **VM Instances**.
3. Создайте новую виртуальную машину (например, с Ubuntu 20.04).
4. Убедитесь, что для машины открыт порт 443 (HTTPS).

### 2. Подключитесь к серверу через SSH
1. В Google Cloud Console нажмите **SSH** для доступа к вашей виртуальной машине.

### 3. Установите необходимые пакеты
```bash
sudo apt update
sudo apt install python3 python3-pip nginx certbot python3-certbot-nginx git
```

### 4. Склонируйте проект
```bash
git clone https://github.com/MishaKhovrych/telegram-bot.git
cd telegram-bot
```

### 5. Установите зависимости
```bash
pip3 install -r requirements.txt
```

### 6. Настройте `.env` файл
1. Создайте файл `.env` в корневой директории проекта.
2. Добавьте ваши токены и настройки:
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   YOUR_CHANNEL_ID=your_telegram_channel_id
   API_ID=your_api_id
   API_HASH=your_api_hash
   ```

### 7. Настройте Nginx и HTTPS
1. Настройте Nginx для обработки вебхуков:
   ```bash
   sudo nano /etc/nginx/sites-available/default
   ```
   Замените содержимое файла:
   ```
   server {
       listen 443 ssl;
       server_name yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

       location /telegram-webhook {
           proxy_pass http://localhost:8000/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```
2. Получите HTTPS сертификаты:
   ```bash
   sudo certbot --nginx
   ```

### 8. Установите вебхук
1. Настройте вебхук:
   ```python
   from webhook_helper import set_webhook
   print(set_webhook("https://yourdomain.com/telegram-webhook"))
   ```

### 9. Запустите мониторинг референсных каналов
1. Запустите файл `monitor_channels.py`:
   ```bash
   python3 monitor_channels.py
   ```

### 10. Запустите бот
1. Запустите файл `bot_content_processing.py` для обработки контента:
   ```bash
   python3 bot_content_processing.py
   ```
2. Запустите основной файл `bot.py` для взаимодействия с Telegram:
   ```bash
   python3 bot.py
   ```

### 11. Настройте автозапуск
1. Настройте systemd-сервис:
   ```bash
   sudo nano /etc/systemd/system/telegram-bot.service
   ```
   Содержимое файла:
   ```
   [Unit]
   Description=Telegram Bot "Пока все ждут отката"
   After=network.target

   [Service]
   User=your_username
   WorkingDirectory=/path/to/telegram-bot
   ExecStart=/usr/bin/python3 bot.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
2. Активируйте сервис:
   ```bash
   sudo systemctl enable telegram-bot
   sudo systemctl start telegram-bot
   sudo systemctl status telegram-bot
   ```

## Команды бота
- `/start`: Запуск бота.
- `/test_connection`: Тест подключения.
- `/test_with_references`: Тест с референсными каналами.
- `/check_webhook`: Проверка вебхука.

## Примечания
- Убедитесь, что ваш сервер защищен (например, используйте файрвол Google Cloud).
- Используйте `tmux` или `screen` для тестирования в SSH-сессии.
