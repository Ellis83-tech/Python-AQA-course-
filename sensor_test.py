import time


def test_sanity(get_sensor_info, get_sensor_reading):
    sensor_info = get_sensor_info()

    sensor_name = sensor_info.get("name")
    assert isinstance(sensor_name, str), "Sensor name is not a string"

    sensor_hid = sensor_info.get("hid")
    assert isinstance(sensor_hid, str), "Sensor hid is not a string"

    sensor_model = sensor_info.get("model")
    assert isinstance(sensor_model, str), "Sensor model is not a string"

    sensor_firmware_version = sensor_info.get("firmware_version")
    assert isinstance(
        sensor_firmware_version, int
    ), "Sensor firmware version is not a int"

    sensor_reading_interval = sensor_info.get("reading_interval")
    assert isinstance(
        sensor_reading_interval, int
    ), "Sensor reading interval is not a string"

    sensor_reading = get_sensor_reading()
    assert isinstance(
        sensor_reading, float
    ), "Sensor doesn't seem to register temperature"

    print("Sanity test passed")


def test_reboot(get_sensor_info, reboot_sensor):
    """
    Steps:
        1. Get original sensor info.
        2. Reboot sensor.
        3. Wait for sensor to come back online.
        4. Get current sensor info.
        5. Validate that info from Step 1 is equal to info from Step 4.
    """
    """
    Test to reboot a sensor and validate its information before and after the reboot.
    """
    # Step 1: Get original sensor info
    original_info = get_sensor_info()

    # Step 2: Reboot sensor
    reboot_sensor()

    # Step 3: Wait for sensor to come back online
    time.sleep(10)  

    # Step 4: Get current sensor info
    current_info = get_sensor_info()

    # Step 5: Validate that info from Step 1 is equal to info from Step 4
    assert original_info == current_info, "Sensor info mismatch after reboot"

# Example usage of the test function
# Assuming we have defined the `get_sensor_info` and `reboot_sensor` functions
# test_reboot(get_sensor_info, reboot_sensor)


def test_set_sensor_name(get_sensor_info, set_sensor_name):
    """
    1. Set sensor name to "new_name".
    2. Get sensor_info.
    3. Validate that current sensor name matches the name set in Step 1.
    """

    # Step 1: Set sensor name to "new_name"
    set_sensor_name("new_name")
    
    # Step 2: Get sensor_info
    sensor_info = get_sensor_info()
    
    # Step 3: Validate that current sensor name matches the name set in Step 1
    assert sensor_info['name'] == "new_name", f"Sensor name should be 'new_name', but got '{sensor_info['name']}'"


def test_set_sensor_reading_interval(
    get_sensor_info, set_sensor_reading_interval, get_sensor_reading
):
    """
    1. Set sensor reading interval to 1.
    2. Get sensor info.
    3. Validate that sensor reading interval is set to interval from Step 1.
    4. Get sensor reading.
    5. Wait for interval specified in Step 1.
    6. Get sensor reading.
    7. Validate that reading from Step 4 doesn't equal reading from Step 6.
    """

    """
    Test to set sensor reading interval to 1, get sensor info, validate that the sensor reading interval is set,
    get sensor reading, wait for the interval, get sensor reading again, and validate that the readings are different.
    """
    # Step 1: Set sensor reading interval to 1
    set_sensor_reading_interval(1)
    
    # Step 2: Get sensor info
    sensor_info = get_sensor_info()
    
    # Step 3: Validate that sensor reading interval is set to interval from Step 1
    assert sensor_info['reading_interval'] == 1, f"Sensor reading interval should be 1, but got {sensor_info['reading_interval']}"
    
    # Step 4: Get sensor reading
    initial_reading = get_sensor_reading()
    
    # Step 5: Wait for interval specified in Step 1
    # (Note: This step is simulated with a sleep of 1 second)
    time.sleep(1)
    
    # Step 6: Get sensor reading
    new_reading = get_sensor_reading()
    
    # Step 7: Validate that reading from Step 4 doesn't equal reading from Step 6
    assert initial_reading != new_reading, "Sensor readings should be different after the interval"



# Максимальна версія прошивки сенсора -- 15
def test_update_sensor_firmware(get_sensor_info, update_sensor_firmware):
    """
    1. Get original sensor firmware version.
    2. Request firmware update.
    3. Get current sensor firmware version.
    4. Validate that current firmware version is +1 to original firmware version.
    5. Repeat steps 1-4 until sensor is at max_firmware_version - 1.
    6. Update sensor to max firmware version.
    7. Validate that sensor is at max firmware version.
    8. Request another firmware update.
    9. Validate that sensor doesn't update and responds appropriately.
    10. Validate that sensor firmware version doesn't change if it's at maximum value.
<<<<<<< HEAD
    """
import time

# Максимальна версія прошивки сенсора -- 15
max_firmware_version = 15

def test_update_sensor_firmware(get_sensor_info, update_sensor_firmware):
    """
    Test to update sensor firmware, validate firmware version increments, and ensure it doesn't update past the maximum version.
    """
    # Step 1: Get original sensor firmware version
    original_version = get_sensor_info()['firmware_version']
    
    # Steps 2-5: Update firmware and validate version increment until max_firmware_version - 1
    while original_version < max_firmware_version - 1:
        # Step 2: Request firmware update
        update_sensor_firmware()
        
        # Simulate time delay for firmware update
        time.sleep(1)
        
        # Step 3: Get current sensor firmware version
        current_version = get_sensor_info()['firmware_version']
        
        # Step 4: Validate that current firmware version is +1 to original firmware version
        assert current_version == original_version + 1, f"Firmware version did not increment correctly. Expected {original_version + 1}, got {current_version}"
        
        # Update original_version for the next iteration
        original_version = current_version
    
    # Step 6: Update sensor to max firmware version
    update_sensor_firmware()
    
    # Simulate time delay for firmware update
    time.sleep(1)
    
    # Step 7: Validate that sensor is at max firmware version
    current_version = get_sensor_info()['firmware_version']
    assert current_version == max_firmware_version, f"Sensor did not update to max firmware version. Expected {max_firmware_version}, got {current_version}"
    
    # Step 8: Request another firmware update
    update_sensor_firmware()
    
    # Simulate time delay for firmware update
    time.sleep(1)
    
    # Step 9-10: Validate that sensor doesn't update and responds appropriately
    new_version = get_sensor_info()['firmware_version']
    assert new_version == max_firmware_version, f"Sensor firmware version should not change if it's at maximum value. Expected {max_firmware_version}, got {new_version}"
