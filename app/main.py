from fastapi import FastAPI, Request
from fastapi.responses import Response  # ADD THIS
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import logging
import time

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Logging setup
logging.basicConfig(
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
    level=logging.INFO
)

# Tracing setup
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

# Metrics
REQUEST_COUNT = Counter("request_count", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds", ["endpoint"])

app = FastAPI()
FastAPIInstrumentor().instrument_app(app, tracer_provider=trace.get_tracer_provider())

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    resp_time = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(resp_time)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    logging.info(f'{{"method": "{request.method}", "path": "{request.url.path}", "status": {response.status_code}}}')
    return response

# ADD THIS ENDPOINT (NEW)
@app.get("/")
def root():
    return {"message": "DevOps API", "version": "1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

# FIX THIS ENDPOINT (CHANGED)
@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)