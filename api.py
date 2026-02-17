class TechnitiumApi:
    def __init__(self, host, api_key, session, timeout=10):
        self._host = host
        self._api_key = api_key
        self._timeout = timeout
        self._session = session

    async def get_status(self):
        url = f"{self._host}/api/status"
        headers = {"Authorization": f"Bearer {self._api_key}"}
        import logging
        logger = logging.getLogger(__name__)
        try:
            logger.debug(f"Requesting Technitium status from {url} with headers {headers}")
            async with self._session.get(url, headers=headers, timeout=self._timeout) as resp:
                logger.debug(f"Technitium status response code: {resp.status}")
                resp.raise_for_status()
                data = await resp.json()
                logger.debug(f"Technitium status response data: {data}")
                return {"ad_blocking_status": data.get("adBlockingEnabled")}
        except Exception as e:
            logger.error(f"Error fetching Technitium status from {url} with key {self._api_key}: {e}")
            return {"ad_blocking_status": None}

    async def pause_ad_blocking(self, seconds):
        url = f"{self._host}/api/pause"
        headers = {"Authorization": f"Bearer {self._api_key}"}
        payload = {"duration": seconds}
        import logging
        logger = logging.getLogger(__name__)
        try:
            logger.debug(f"Sending pause request to {url} with headers {headers} and payload {payload}")
            async with self._session.post(url, headers=headers, json=payload, timeout=self._timeout) as resp:
                logger.debug(f"Technitium pause response code: {resp.status}")
                resp.raise_for_status()
                data = await resp.json()
                logger.debug(f"Technitium pause response data: {data}")
                return data
        except Exception as e:
            logger.error(f"Error pausing ad blocking at {url} with key {self._api_key} and payload {payload}: {e}")
            return None

    async def close(self):
        # No need to close Home Assistant's managed session
        pass
