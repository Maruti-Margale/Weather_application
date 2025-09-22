# Weather_application

LIVE DEMO ; https://marutimargale.pythonanywhere.com/

```mermaid
graph TD
    A[Start: User visits app] --> B[Flask (app.py) receives request]
    B --> C[Weather API call using OpenWeatherMap]
    C --> D[Parse API response (JSON)]
    D --> E[Send data to HTML template (index.html)]
    E --> F[Render with Jinja2: show weather info]
    F --> G[Display styled page using CSS (style.css)]
    G --> H[User sees result on browser]
    H --> I[End]

...diagram code here...
```
