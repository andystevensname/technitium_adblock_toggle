from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, DEFAULT_NAME

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    async_add_entities([
        TechnitiumBlockPauseAdBlockSensor(coordinator)
    ])

class TechnitiumBlockPauseAdBlockSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = f"{DEFAULT_NAME} Ad Blocking"
        self._attr_unique_id = "technitium_block_pause_ad_blocking"

    @property
    def state(self):
        return self.coordinator.data.get("ad_blocking_status")
