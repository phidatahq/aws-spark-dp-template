from phidata.app.group import AppGroup
from phidata.app.spark import SparkDriver, SparkWorker

from workspace.settings import ws_settings

# -*- Run a spark cluster on docker

dev_spark_driver = SparkDriver(
    name=f"spark-{ws_settings.ws_name}-driver",
    mount_workspace=True,
    # Connect to spark driver on port 9080
    container_host_port=9080,
    # Run the driver UI on spark.dp
    container_labels={
        "traefik.enable": "true",
        "traefik.http.routers.spark.entrypoints": "http",
        "traefik.http.routers.spark.rule": "Host(`spark.dp`)",
        "traefik.http.services.spark.loadbalancer.server.port": "8080",
    },
    use_cache=ws_settings.use_cache,
)

dev_spark_worker = SparkWorker(
    name=f"spark-{ws_settings.ws_name}-worker",
    driver_url=dev_spark_driver.driver_url,
    mount_workspace=True,
    # Connect to spark driver on port 9080
    container_host_port=9081,
    use_cache=ws_settings.use_cache,
)

dev_spark_apps = AppGroup(
    name="spark",
    enabled=True,
    apps=[dev_spark_driver, dev_spark_worker],
)
