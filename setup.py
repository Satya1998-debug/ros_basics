from setuptools import find_packages, setup

package_name = 'ros_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='satya_ubuntu',
    maintainer_email='spradhan143as@gmail.com',
    description='Beginner client libraries tutorials practice package. Like Publisher-Subscriber, etc.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros_basics.publisher_member_function:main',
            'listener = ros_basics.subscriber_member_function:main',
        ],
    },
)
