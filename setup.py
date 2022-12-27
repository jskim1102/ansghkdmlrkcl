from setuptools import setup, find_packages

def imshow(img):
    cv2.imshow('image', img)
    cv2.waitKey() 
    cv2.destroyAllWindows()

setup(
    name                = 'ansghkdmlrkcl',
    version             = '0.1',
    description         = 'ansghkdmlrkcl',
    author              = 'jinsoo',
    author_email        = 'deepi.contact.us@gmail.com',
    url                 = 'https://github.com/jeakwon/ansghkdmlrkcl',
    download_url        = 'https://github.com/jeakwon/ansghkdmlrkcl/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['ansghkdmlrkcl'],
    python_requires     = '>=3.8',
    install_requires=[
        "opencv-python"
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3.8',
    ],
)
