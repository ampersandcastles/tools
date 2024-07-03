# This is not a direct clone of lsblk.c, this is a minimal reinterpretation for use on FreeBSD.

import subprocess

def get_geom_info():
    result = subprocess.run(['geom', 'disk', 'list'], stdout=subprocess.PIPE)
    return result.stdout.decode()

def parse_geom_output(output):
    devices = []
    device = {}
    for line in output.splitlines():
        if line.startswith('Geom name:'):
            if device:
                devices.append(device)
                device = {}
            device['name'] = line.split(': ')[1]
        elif 'Mediasize' in line:
            device['size'] = format_size(int(line.split(': ')[1].split(' ')[0]))
        elif 'descr' in line:
            device['description'] = line.split(': ')[1]
    if device:
        devices.append(device)
    return devices

def format_size(size):
    # Convert size in bytes to human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024

def get_mount_points():
    result = subprocess.run(['mount'], stdout=subprocess.PIPE)
    mount_output = result.stdout.decode()
    mount_points = {}
    for line in mount_output.splitlines():
        parts = line.split(' ')
        device = parts[0]
        mount_point = parts[2]
        mount_points[device] = mount_point
    return mount_points

def print_lsblk_format(devices, mount_points):
    print(f"{'NAME':<10} {'SIZE':<10} {'DESCRIPTION':<20} {'MOUNTPOINT':<20}")
    for device in devices:
        mount_point = mount_points.get(f"/dev/{device['name']}", '-')
        print(f"{device['name']:<10} {device['size']:<10} {device['description']:<20} {mount_point:<20}")

if __name__ == "__main__":
    geom_output = get_geom_info()
    devices = parse_geom_output(geom_output)
    mount_points = get_mount_points()
    print_lsblk_format(devices, mount_points)
