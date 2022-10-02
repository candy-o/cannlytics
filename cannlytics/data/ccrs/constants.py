"""
CCRS Constants | Cannlytics
Copyright (c) 2022 Cannlytics

Authors: Keegan Skeate <https://github.com/keeganskeate>
Created: 4/12/2022
Updated: 9/22/2022
License: <https://github.com/cannlytics/cannlytics/blob/main/LICENSE>

Description: Helpful CCRS constants.

Data Sources:

    - WAC 314-55-102 Quality assurance and quality control
    https://app.leg.wa.gov/wac/default.aspx?cite=314-55-102&pdf=true

    - WAC 314-55-108 Pesticide action levels
    https://apps.leg.wa.gov/WAC/default.aspx?cite=314-55-108

    - WAC 246-70-050 Quality assurance testing
    https://app.leg.wa.gov/WAC/default.aspx?cite=246-70-050&pdf=true
"""

analyses = {
    'Foreign Matter': 'foreign_matter',
    'Heavy Metal': 'heavy_metal',
    'Microbiological': 'microbe',
    'Moisture Analysis': 'moisture',
    'Moistures Analysis': 'moisture',
    'Mycotoxin': 'mycotoxin',
    'Pesticide': 'pesticide',
    'Potency': 'cannabinoid',
    'Residual Solvent': 'residual_solvent',
    'Terpene': 'terpene',
    'Water Activity': 'water_activity',
}

# FIXME: Reformat and add WSLCB limits.
# Ensure all analytes are included and not repeated.
analytes = {
    'Microbial- I502 panel (3)-E.coli': {
        'key': 'e_coli',
        'type': 'microbe',
        'units': 'CFU/G',
        'limit': -1,
    },
    'Microbial- I502 panel (3)-Bile Tolerant gram neg': {
        'key': 'btgn',
        'type': 'microbe',
        'units': 'CFU/G',
        'limit': -1,
    },
    'Microbial- I502 panel (3)-Salmonella': {'key': 'salmonella', 'type': 'microbe', 'units': 'CFU/G'},
    'Moisture & Water Activity-Moisture(%)': {'key': 'moisture', 'type': 'moisture', 'units': 'percent'},
    'Moisture & Water Activity-Water Activity (Aw)(%)': {'key': 'water_activity', 'type': 'water_activity', 'units': 'aw'},
    'Mycotoxins-Total Aflatoxins': {'key': 'aflatoxins', 'type': 'mycotoxin', 'units': 'CFU/G'},
    'Mycotoxins-Ochratoxin A': {'key': 'ochratoxin', 'type': 'mycotoxin', 'units': 'CFU/G'},
    'Terpineol': {'key': 'terpineol', 'type': 'terpene', 'units': 'percent'},
    'Microbiological - BTGN (CFU/g)': {'key': 'btgn', 'type': 'Microbiological', 'units': 'CFU/g'},
    'Residual Solvent - Butanes (ppm)': {'key': 'butanes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Propanes (ppm)': {'key': 'propanes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Benzene (ppm)': {'key': 'benzene', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Potency - D9THCA (%)': {'key': '9_thca', 'type': 'Potency', 'units': 'percent'},
    'Potency - Total THC (%)': {'key': 'total_thc', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBDA (%)': {'key': 'cbda', 'type': 'Potency', 'units': 'percent'},
    'Foreign Matter - Seeds or Other (%)': {'key': 'seeds_or_other', 'type': 'Foreign Matter', 'units': 'percent'},
    'Potency - Total CBD (%)': {'key': 'total_cbd', 'type': 'Potency', 'units': 'percent'},
    'Potency - D9THC (%)': {'key': '9_thc', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBD (%)': {'key': 'cbd', 'type': 'Potency', 'units': 'percent'},
    'Foreign Matter - Stems (%)': {'key': 'stems', 'type': 'Foreign Matter', 'units': 'percent'},
    'Residual Solvent - Toluene (ppm)': {'key': 'toluene', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Heptanes (ppm)': {'key': 'heptanes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Microbiological - Salmonella (CFU/g)': {'key': 'salmonella', 'type': 'Microbiological', 'units': 'CFU/g'},
    'Microbiological - Ste (CFU/g)': {'key': 'stec', 'type': 'Microbiological', 'units': 'CFU/g'},
    'Moisture Analysis - Water Activity (aw)': {'key': 'water_activity', 'type': 'Moisture Analysis', 'units': 'aw'},
    'Mycotoxin - Ochratoxin A (ppb)': {'key': 'ochratoxin', 'type': 'Mycotoxin', 'units': 'ppb'},
    'Moistures Analysis - Moisture Content (%)': {'key': 'moisture_content', 'type': 'Moistures Analysis', 'units': 'percent'},
    'Mycotoxin - Total Aflatoxins (ppb)': {'key': 'total_aflatoxins', 'type': 'Mycotoxin', 'units': 'ppb'},
    'Residual Solvent - Hexanes (ppm)': {'key': 'hexanes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Acetone (ppm)': {'key': 'acetone', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Xylenes (ppm)': {'key': 'xylenes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Methanol (ppm)': {'key': 'methanol', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Isopropanol (ppm)': {'key': 'isopropanol', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Chloroform (ppm)': {'key': 'chloroform', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Dichloromethane (ppm)': {'key': 'dichloromethane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Ethyl Acetate (ppm)': {'key': 'ethyl_acetate', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Cyclohexane (ppm)': {'key': 'cyclohexane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Potency - CBDV (%)': {'key': 'cbdv', 'type': 'Potency', 'units': 'percent'},
    'Potency - THCV (%)': {'key': 'thcv', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBG (%)': {'key': 'cbg', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBGA (%)': {'key': 'cbga', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBN (%)': {'key': 'cbn', 'type': 'Potency', 'units': 'percent'},
    'Potency - D8THC (%)': {'key': '8_thc', 'type': 'Potency', 'units': 'percent'},
    'Potency - CBC (%)': {'key': 'cbc', 'type': 'Potency', 'units': 'percent'},
    'Potency - THCA (%)': {'key': 'thca', 'type': 'Potency', 'units': 'percent'},
    'Mycotoxin - Total Aflatoxins (ug/kg)': {'key': 'total_aflatoxins', 'type': 'Mycotoxin', 'units': 'ug/kg'},
    'Mycotoxin - Ochratoxin A (ug/kg)': {'key': 'ochratoxin', 'type': 'Mycotoxin', 'units': 'ug/kg'},
    'Residual Solvent - Acetone (ug/g)': {'key': 'acetone', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Acetonitrile (ug/g)': {'key': 'acetonitrile', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Benzene (ug/g)': {'key': 'benzene', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Butanes (ug/g)': {'key': 'butanes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Chloroform (ug/g)': {'key': 'chloroform', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Cyclohexane (ug/g)': {'key': 'cyclohexane', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Dichloromethane (ug/g)': {'key': 'dichloromethane', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Ethanol (ug/g)': {'key': 'ethanol', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Ethyl Acetate (ug/g)': {'key': 'ethyl_acetate', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Ethyl Ether (ug/g)': {'key': 'ethyl_ether', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Heptanea (ug/g)': {'key': 'heptanea', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Hexanes (ug/g)': {'key': 'hexanes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Isobutane (ug/g)': {'key': 'isobutane', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Methanol (ug/g)': {'key': 'methanol', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Pentanes (ug/g)': {'key': 'pentanes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - 2-Propanol (IPA) (ug/g)': {'key': '2_propanol', 'type': 'Residual Solvent', 'units': 'IPA '},
    'Residual Solvent - Propanes (ug/g)': {'key': 'propanes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Toluene (ug/g)': {'key': 'toluene', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Xylenes (ug/g)': {'key': 'xylenes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Moisture Analysis - Moisture Content (%)': {'key': 'moisture_content', 'type': 'Moisture Analysis', 'units': 'percent'},
    'Residual Solvent - Heptanes (ug/g)': {'key': 'heptanes', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Residual Solvent - Isopropanol (ug/g)': {'key': 'isopropanol', 'type': 'Residual Solvent', 'units': 'ug/g'},
    'Potency - CBD (mg/g)': {'key': 'cbd', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - CBDA (mg/g)': {'key': 'cbda', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - D9THC (mg/g)': {'key': '9_thc', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - D9THCA (mg/g)': {'key': '9_thca', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - Total THC (mg/g)': {'key': 'total_thc', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - Total CBD (mg/g)': {'key': 'total_cbd', 'type': 'Potency', 'units': 'mg/g'},
    'Potency - CBD (mg/mL)': {'key': 'cbd', 'type': 'Potency', 'units': 'mg/mL'},
    'Potency - CBDA (mg/mL)': {'key': 'cbda', 'type': 'Potency', 'units': 'mg/mL'},
    'Potency - D9THC (mg/mL)': {'key': '9_thc', 'type': 'Potency', 'units': 'mg/mL'},
    'Potency - D9THCA (mg/mL)': {'key': '9_thca', 'type': 'Potency', 'units': 'mg/mL'},
    'Potency - Total THC (mg/mL)': {'key': 'total_thc', 'type': 'Potency', 'units': 'mg/mL'},
    'Potency - Total CBD (mg/mL)': {'key': 'total_cbd', 'type': 'Potency', 'units': 'mg/mL'},
    'Microbiological - BTGN (CFU/G)': {'key': 'btgn', 'type': 'Microbiological', 'units': 'CFU/G'},
    'Mycotoxin - Ochratoxin (CFU/G)': {'key': 'ochratoxin', 'type': 'Mycotoxin', 'units': 'CFU/G'},
    'Microbiological - STEC (CFU/G)': {'key': 'stec', 'type': 'Microbiological', 'units': 'CFU/G'},
    'Microbiological - STEC (CFU/g)': {'key': 'stec', 'type': 'Microbiological', 'units': 'CFU/G'},
    'Microbiological - Salmonella (CFU/G)': {'key': 'salmonella', 'type': 'Microbiological', 'units': 'CFU/G'},
    'Mycotoxin - Aflatoxins (CFU/G)': {'key': 'aflatoxins', 'type': 'Mycotoxin', 'units': 'CFU/G'},
    'Residual Solvent - Benzene (PPM)': {'key': 'benzene', 'type': 'Residual Solvent', 'units': 'PPM'},
    'Residual Solvent - Dichloro-Methane (ppm)': {'key': 'dichloro_methane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Heptane (ppm)': {'key': 'heptane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - n-Hexane (ppm)': {'key': 'n_hexane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Pentanes (ppm)': {'key': 'pentanes', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Residual Solvent - Propane (ppm)': {'key': 'propane', 'type': 'Residual Solvent', 'units': 'ppm'},
    'Potency - D9THC (mg/serving)': {'key': '9_thc', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - D9THCA (mg/serving)': {'key': '9_thca', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - CBD (mg/serving)': {'key': 'cbd', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - CBDA (mg/serving)': {'key': 'cbda', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - Total THC (mg/serving)': {'key': 'total_thc', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - Total CBD (mg/serving)': {'key': 'total_cbd', 'type': 'Potency', 'units': 'mg/serving'},
    'Potency - D9THC ()': {'key': '9_thc', 'type': 'Potency', 'units': ''},
    'Potency - D9THCA ()': {'key': '9_thca', 'type': 'Potency', 'units': ''},
    'Potency - CBD ()': {'key': 'cbd', 'type': 'Potency', 'units': ''},
    'Potency - CBDA ()': {'key': 'cbda', 'type': 'Potency', 'units': ''},
    'Potency - Total THC ()': {'key': 'total_thc', 'type': 'Potency', 'units': ''},
    'Potency - Total CBD ()': {'key': 'total_cbd', 'type': 'Potency', 'units': ''},
    'Potency - THCA (mg/serving)': {'key': 'thca', 'type': 'Potency', 'units': 'mg/serving'},
    'Heavy Metal - Arsenic (ppm)': {'key': 'arsenic', 'type': 'Heavy Metal', 'units': 'ppm'},
    'Heavy Metal - Cadmium (ppm)': {'key': 'cadmium', 'type': 'Heavy Metal', 'units': 'ppm'},
    'Heavy Metal - Lead (ppm)': {'key': 'lead', 'type': 'Heavy Metal', 'units': 'ppm'},
    'Heavy Metal - Mercury (ppm)': {'key': 'mercury', 'type': 'Heavy Metal', 'units': 'ppm'},
    'Pesticide - Abamectin (ppm)': {'key': 'abamectin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Acephate (ppm)': {'key': 'acephate', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Acequinocyl (ppm)': {'key': 'acequinocyl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Acetamiprid (ppm)': {'key': 'acetamiprid', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Aldicarb (ppm)': {'key': 'aldicarb', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Azoxystrobin (ppm)': {'key': 'azoxystrobin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Bifenazate (ppm)': {'key': 'bifenazate', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Bifenthrin (ppm)': {'key': 'bifenthrin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Boscalid (ppm)': {'key': 'boscalid', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Carbaryl (ppm)': {'key': 'carbaryl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Carbofuran (ppm)': {'key': 'carbofuran', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Chlorantraniliprole (ppm)': {'key': 'chlorantraniliprole', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Chlorfenapyr (ppm)': {'key': 'chlorfenapyr', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Chlorpyrifos (ppm)': {'key': 'chlorpyrifos', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Clofentizine (ppm)': {'key': 'clofentizine', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Cyfluthrin (ppm)': {'key': 'cyfluthrin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Cypermethrin (ppm)': {'key': 'cypermethrin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Daminozide (ppm)': {'key': 'daminozide', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - DDVP (dichlorvos) (ppm)': {'key': 'ddvp', 'type': 'Pesticide', 'units': 'dichlorvos '},
    'Pesticide - Diazinon (ppm)': {'key': 'diazinon', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Dimethoate (ppm)': {'key': 'dimethoate', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Ethoprophos (ppm)': {'key': 'ethoprophos', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Etofenprox (ppm)': {'key': 'etofenprox', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Etoxazole (ppm)': {'key': 'etoxazole', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Fenoxycarb (ppm)': {'key': 'fenoxycarb', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Fenpyroximate (ppm)': {'key': 'fenpyroximate', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Fipronil (ppm)': {'key': 'fipronil', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Flonicamid (ppm)': {'key': 'flonicamid', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Fludioxonil (ppm)': {'key': 'fludioxonil', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Hexythiazox (ppm)': {'key': 'hexythiazox', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Imazalil (ppm)': {'key': 'imazalil', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Imidacloprid (ppm)': {'key': 'imidacloprid', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Kresoxim-Methyl (ppm)': {'key': 'kresoxim_methyl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Malathion (ppm)': {'key': 'malathion', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Metalaxyl (ppm)': {'key': 'metalaxyl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Methiocarb (ppm)': {'key': 'methiocarb', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Methomyl (ppm)': {'key': 'methomyl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Methyl parathion (ppm)': {'key': 'methyl_parathion', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - MGK-264 (ppm)': {'key': 'mgk_264', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Myclobutanil (ppm)': {'key': 'myclobutanil', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Naled (ppm)': {'key': 'naled', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Oxamyl (ppm)': {'key': 'oxamyl', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Paclobutrazol (ppm)': {'key': 'paclobutrazol', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Permethrins (ppm)': {'key': 'permethrins', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Phosmet (ppm)': {'key': 'phosmet', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Piperonyl butoxide (ppm)': {'key': 'piperonyl_butoxide', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Prallethrin (ppm)': {'key': 'prallethrin', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Propiconazole (ppm)': {'key': 'propiconazole', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Propoxur (ppm)': {'key': 'propoxur', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Pyrethrins (ppm)': {'key': 'pyrethrins', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Pyridaben (ppm)': {'key': 'pyridaben', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Spinosad (ppm)': {'key': 'spinosad', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Spiromesifen (ppm)': {'key': 'spiromesifen', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Spirotetramat (ppm)': {'key': 'spirotetramat', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Spiroxamine (ppm)': {'key': 'spiroxamine', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Tebuconazole (ppm)': {'key': 'tebuconazole', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Thiacloprid (ppm)': {'key': 'thiacloprid', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Thiamethoxam (ppm)': {'key': 'thiamethoxam', 'type': 'Pesticide', 'units': 'ppm'},
    'Pesticide - Trifloxystrobin (ppm)': {'key': 'trifloxystrobin', 'type': 'Pesticide', 'units': 'ppm'},
}

datasets = {
    'areas': {
        'dataset': 'Areas_0',
        'singular': 'area',
        'fields': {
            'LicenseeId': 'string',
            'Name': 'string',
            'IsQuarantine': 'bool',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'contacts': {
        'dataset': 'Contacts_0',
        'singular': 'contact',
        'fields': {
            'LicenseeId': 'string',
            'IntegratorId': 'string',
            'FirstName': 'string',
            'MiddleInitial': 'string',
            'LastName': 'string',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
            'IsAdmin': 'bool',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'integrators': {
        'dataset': 'Integrator_0',
        'singular': 'integrator',
        'fields': {
            'Name': 'string',
            'IsActive': 'bool',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'inventory': {
        'dataset': 'Inventory_0',
        'singular': 'inventory_item',
        'fields': {
            'LicenseeId': 'string',
            'StrainId': 'string',
            'AreaId': 'string',
            'ProductId': 'string',
            'InventoryIdentifier': 'string',
            'InitialQuantity': 'float',
            'QuantityOnHand': 'float',
            'TotalCost': 'float',
            'IsMedical': 'bool',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'updatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'updatedDate',
        ],
    },
    'inventory_adjustments': {
        'dataset': 'Areas_0',
        'singular': 'inventory_adjustment',
        'fields': {
            'InventoryId': 'string',
            'InventoryAdjustmentReason': 'string',
            'AdjustmentDetail': 'string',
            'Quantity': 'float',
            'AdjustmentDate': 'datetime',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'AdjustmentDate',
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'lab_results': {
        'dataset': 'LabResult_0',
        'singular': 'lab_result',
        'fields': {
            'LabLicenseeId': 'string',
            'LicenseeId': 'string',
            'LabTestStatus': 'string',
            'InventoryId': 'string',
            'TestName': 'string',
            'TestDate': 'datetime',
            'TestValue': 'float',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'string',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'TestDate',
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'licensees': {
        'dataset': 'Licensee_0',
        'singular': 'licensee',
        'fields': {
            'LicenseStatus': 'string',
            'UBI': 'string',
            'LicenseNumber': 'string',
            'Name': 'string',
            'DBA': 'string',
            'LicenseIssueDate': 'datetime',
            'LicenseExpirationDate': 'datetime',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'Address1': 'string',
            'Address2': 'string',
            'City': 'string',
            'State': 'string',
            'ZipCode': 'string',
            'County': 'string',
            'EmailAddress': 'string',
            'PhoneNumber': 'string',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'LicenseIssueDate',
            'LicenseExpirationDate',
            'UpdatedDate',
        ],
    },
    'plants': {
        'dataset': 'Plant_0',
        'singular': 'plant',
        'fields': {
            'LicenseeId': 'string',
            'AreaId': 'string',
            'StrainId': 'string',
            'PlantSource': 'string',
            'PlantState': 'string',
            'GrowthStage': 'string',
            'HarvestCycle': 'string',
            'MotherPlantId': 'string',
            'PlantIdentifier': 'string',
            'HarvestDate': 'datetime',
            'IsMotherPlant': 'bool',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'string',
        },
        'date_fields': [
            'CreatedDate',
            'HarvestDate',
            'UpdatedDate',
        ],
    },
    'plant_destructions': {
        'dataset': 'PlantDestructions_0',
        'singular': 'plant_destruction',
        'fields': {
            'PlantId',
            'DestructionReason',
            'DestructionMethod',
            'DestructionDate',
            'ExternalIdentifier',
            'IsDeleted',
            'CreatedBy',
            'CreatedDate',
            'UpdatedBy',
            'UpdatedDate'
        },
        'date_fields': [
            'CreatedDate',
            'DestructionDate',
            'UpdatedDate',
        ],
    },
    'products': {
        'dataset': 'Product_0',
        'singular': 'product',
        'fields': {
            'LicenseeId': 'string',
            'InventoryTypeId': 'string',
            'Name': 'string',
            'Description': 'string',
            'UnitWeightGrams': 'float',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'sale_headers': {
        'dataset': 'SaleHeader_0',
        'singular': 'sale',
        'fields': {
            'SaleHeaderId': 'string',
            'LicenseeId': 'string',
            'SoldToLicenseeId': 'string',
            'SaleType': 'string',
            'SaleDate': 'datetime',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'SaleDate',
            'UpdatedDate',
        ],
    },
    'sale_details': {
        'dataset': 'SalesDetail_0',
        'singular': 'sale_item',
        'fields': {
            'SaleDetailId': 'string',
            'SaleHeaderId': 'string',
            'InventoryId': 'string',
            'PlantId': 'string',
            'Quantity': 'float',
            'UnitPrice': 'float',
            'Discount': 'float',
            'SalesTax': 'float',
            'OtherTax': 'float',
            'ExternalIdentifier': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'strains': {
        'dataset': 'Strains_0',
        'singular': 'strain',
        'fields': {
            'StrainType': 'string',
            'Name': 'string',
            'IsDeleted': 'bool',
            'CreatedBy': 'string',
            'CreatedDate': 'datetime',
            'UpdatedBy': 'string',
            'UpdatedDate': 'datetime',
        },
        'date_fields': [
            'CreatedDate',
            'UpdatedDate',
        ],
    },
    'transfers': {
        'dataset': 'Transfers_0',
        'singular': 'transfer',
        'fields': {
            'Serial': 'string',
            'SID': 'string',
            'Submitted Time': 'datetime',
            'Completed Time': 'datetime',
            'Modified Time': 'datetime',
            'Draft': 'int',
            'UID': 'string',
            'Username': 'string',
            'Transportation Type': 'string',
            'Scheduled Transportation Date': 'datetime',
            'UBI Number': 'string',
            'Origin License Number': 'string',
            'Origin Trade Name': 'string',
            'Origin License Address': 'string',
            'Origin License Phone': 'string',
            'Origin License E-mail Address': 'string',
            'Departure Date': 'datetime',
            'Estimated Departure Time': 'time',
            'Arrival Date': 'datetime',
            'Estimated Arrival Time': 'time',
            'Destination License Name': 'string',
            'Destination License Number': 'string',
            'Destination License Email': 'string',
            'Destination License Phone': 'string',
            'Destination License Address': 'string',
            'Items Shipped': 'string', # This is actually a complex CSV, TSV, etc.
        },
        'date_fields': [
            'Submitted Time',
            'Completed Time',
            'Modified Time',
            'Scheduled Transportation Date',
            'Departure Date',
            'Arrival Date',
        ],
    },
}

plant_growth_stages = ['Vegetative', 'Immature', 'Flowering']
plant_harvest_cycles = [ 3,  6,  9, 12]
plants_sources = ['Clone', 'Seed']
plant_states = [
    'Growing',
    'Inventory',
    'Drying',
    'Harvested',
    'Destroyed',
    'Sold',
]
