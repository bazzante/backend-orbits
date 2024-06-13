from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import plotly.express as px
import plotly.io as pio

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Generate a Plotly figure
    fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 2, 3],
                  title="Interactive Plotly Plot")

    # Convert the Plotly figure to HTML
    graph_html = pio.to_html(fig, full_html=False)

    # HTML template
    html_content = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Interactive Plotly Plot in FastAPI</title>
      </head>
      <body>
        <h1>Interactive Plotly Plot in FastAPI</h1>
        <div>{graph_html}</div>
      </body>
    </html>
    """

    return HTMLResponse(content=html_content)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
