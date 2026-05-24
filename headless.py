from __future__ import annotations
import time

from utils.tray_common import (
    bootstrap,
    load_config,
    start_proxy,
    stop_proxy,
)


def _show_error(text: str, title: str = "TG WS Proxy — Ошибка") -> None:
    print(f"{title}: {text}")


def main() -> None:
    global _tray_icon, _config

    _config = load_config()
    bootstrap(_config)

    start_proxy(_config, _show_error)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_proxy()


if __name__ == "__main__":
    main()
