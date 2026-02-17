# Technitium Block Pause Home Assistant Integration

This custom integration allows Home Assistant to monitor and control ad blocking on a Technitium DNS server, with a focus on pausing ad blocking.

## Features
- Sensor for ad blocking status (on/off)
- Service to pause ad blocking for a specified duration

## Installation
1. Copy the `technitium-block-pause` folder to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Add the integration via the UI (search for "Technitium Block Pause").
4. Enter your Technitium DNS host URL and API key.

## Usage
- The sensor `sensor.technitium_block_pause_ad_blocking` shows the current ad blocking status.
- Call the `technitium_block_pause.pause_ad_blocking` service with a `duration` (seconds) to pause ad blocking.

## Configuration
- Host: URL to your Technitium DNS server (e.g., `http://192.168.1.2:5380`)
- API Key: Your Technitium DNS API key

## Notes
- Requires Technitium DNS API to be enabled.
- For more, see the official [Technitium DNS API docs](https://github.com/TechnitiumSoftware/DnsServer).
