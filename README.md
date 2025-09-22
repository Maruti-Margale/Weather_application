# Weather_application

LIVE DEMO ; https://marutimargale.pythonanywhere.com/

## 🔁 Application Flow

The following flowchart shows how the weather application works behind the scenes:

```mermaid
graph TD
    A[User visits app] --> B[Flask app receives request]
    B --> C[Call OpenWeatherMap API]
    C --> D[Parse API response (JSON)]
    D --> E[Send data to HTML template]
    E --> F[Render template using Jinja2]
    F --> G[Apply CSS for styling]
    G --> H[User sees weather information]
    H --> I[End]
```
