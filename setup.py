nfrom setuptools import setup, find_packages

names = [
]

#entry_points = {
#    "console_scripts": [
#        f"{name}= xpdan.startup.{name}:run_main" for name in names
#    ]
#}

setup(
    name="Impedance Fitting",
    version='0.0.1',
    packages=find_packages(),
    description="python API for impedance fitting",
    zip_safe=False,
    package_data={"Impedance-Fitting": ["config/*"]},
    include_package_data=True,
    url="http:/github.com/aplymill7/Impedance-Fitting",
    entry_points=entry_points,
)
