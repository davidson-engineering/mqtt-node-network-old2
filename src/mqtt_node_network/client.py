from collections import deque
import json
from typing import Union

from mqtt_node_network.node import MQTTNode
from mqtt_node_network.configure import MQTTBrokerConfig


class MQTTClient(MQTTNode):
    def __init__(
        self,
        broker_config: MQTTBrokerConfig,
        buffer: Union[list, deque] = None,
        name=None,
        node_id=None,
        node_type=None,
        logger=None,
    ):
        super().__init__(
            broker_config,
            name=name,
            node_id=node_id,
            node_type=node_type,
            logger=logger,
        )

        if buffer is None:
            buffer = []
        self.buffer = buffer

    def on_message(self, client, userdata, message):
        super().on_message(client, userdata, message)
        data = message.payload.decode()
        data = json.loads(data)
        self.buffer.append(data)
