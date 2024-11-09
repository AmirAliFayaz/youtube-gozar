import platform
import subprocess

import log

logger = log.Logger("logs.txt")
logger.clear()


def set_proxy(proxy_address, proxy_port):
    system_platform = platform.system()

    # if system_platform == 'Windows':
    # Run the command to set the proxy in the registry on Windows
    firstResult = subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                  '/v', 'ProxyServer', '/t', 'REG_SZ', '/d', f'{proxy_address}:{proxy_port}', '/f'],
                                 check=True)
    secondResult = subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   '/v', 'ProxyEnable', '/t', 'REG_DWORD', '/d', '1', '/f'],
                                  check=True)
    if firstResult.returncode == 0 and secondResult.returncode == 0:
        logger.log('Proxy set successfully on Windows.')
        return True
    else:
        logger.log('Failed to set proxy on Windows.')
        return False

    # elif system_platform == 'Linux' or system_platform == 'Darwin':
    #     # Run the command to set the environment variables for proxy on Linux or macOS
    #     env_var = f'http_proxy=http://{proxy_address}:{proxy_port}'
    #     subprocess.run(['export', env_var], shell=True)
    #     logger.log(f'Proxy set successfully on {system_platform}.')
    #     return True
    # else:
    #     logger.log(f'Proxy settings not supported on {system_platform}.')
    #     return False


def unset_proxy():
    system_platform = platform.system()

    # if system_platform == 'Windows':
    # Remove the registry values on Windows
    firstResult = subprocess.run(
        ['reg', 'delete', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings',
         '/v', 'ProxyServer', '/f'],
        check=True)

    secondResult = subprocess.run(
        ['reg', 'delete', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings',
         '/v', 'ProxyEnable', '/f'],
        check=True)

    if firstResult.returncode == 0 and secondResult.returncode == 0:
        logger.log('Proxy unset successfully on Windows.')
        return True
    else:
        logger.log('Failed to unset proxy on Windows.')
        return False
    # elif system_platform == 'Linux' or system_platform == 'Darwin':
    #     # Unset the environment variables for proxy on Linux or macOS
    #     subprocess.run(['unset', 'http_proxy'], shell=True)
    #     logger.log(f'Proxy unset successfully on {system_platform}.')
    #     return False
    # else:
    #     logger.log(f'Proxy settings not supported on {system_platform}.')
    #     return False
