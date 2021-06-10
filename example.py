from applauncher import Kernel
from apscheduler_bundle import APSchedulerBundle

with Kernel(bundles=[APSchedulerBundle()], environment="PROD") as kernel:
    kernel.container.apscheduler.background_scheduler().add_job(lambda: print("HOLA"), 'interval', seconds=2)
    kernel.container.apscheduler.background_scheduler_resource()
    kernel.wait()
