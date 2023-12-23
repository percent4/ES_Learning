# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: server.py.py
# @time: 2023/12/23 19:17
import time
import random
from flask import Flask, Response
import logging

logging.basicConfig(filename='../logstash/data/flask.log',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s-%(funcName)s-%(levelname)s-%(message)s')
logger = logging.getLogger()

app = Flask("elk_test")


@app.route('/')
def index():
    t1 = time.time()
    logger.info(f"api_endpoint: /, status: 200, cost_time: {(time.time() - t1) * 1000}")
    return "Hello index", 200


@app.route("/io_task")
def io_task():
    t1 = time.time()
    time.sleep(2)
    logger.info(f"api_endpoint: /io_task, status: 200, cost_time: {(time.time() - t1) * 1000}")
    return "IO bound task finish!", 200


@app.route("/cpu_task")
def cpu_task():
    t1 = time.time()
    for i in range(10000):
        n = i*i*i
    logger.info(f"api_endpoint: /cpu_task, status: 200, cost_time: {(time.time() - t1) * 1000}")
    return "CPU bound task finish!", 200


@app.route("/random_sleep")
def random_sleep():
    t1 = time.time()
    time.sleep(random.randint(0, 5))
    logger.info(f"api_endpoint: /random_sleep, status: 200, cost_time: {(time.time() - t1) * 1000}")
    return "random sleep", 200


@app.route("/random_status")
def random_status():
    t1 = time.time()
    status_code = random.choice([200] * 6 + [300, 400, 400, 500])
    logger.info(f"api_endpoint: /random_status, status: {status_code}, cost_time: {(time.time() - t1) * 1000}")
    return Response("random status", status=status_code)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
