import LicenseNumberDetect as lnd

# def get_car_license_number(image_path):

license_number = lnd.detect_license_number("Plate_examples/dacia_duster_5.jpg")
print(license_number)