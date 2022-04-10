# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:11:25 2022

@author: ESunCe
"""
#simple arithmetic operations for fundamental units in SI system by bundling data with dimension
#importing module copy for creating independent copies of the object via deep copy
import copy


class FundUnit(object):
    # null values
    value = 0
    # initial dimensions
    length_unit = 'm'
    mass_unit = 'kg'
    time_unit = 's'
    electric_current_unit = 'A'
    temperature_unit = 'k'
    amount_of_substance_unit = 'mole'
    light_intensity_unit = 'cd'
    # null dimension power
    length_power = 0
    mass_power = 0
    time_power = 0
    electric_current_power = 0
    temperature_power = 0
    amount_of_substance_power = 0
    light_intensity_power = 0

    def __init__(self, value):
        self.value = value

    # value set
    def set_value(self, value):
        self.value = value

    # unit set
    def set_length_unit(self, length_unit: str):
        self.length_unit = length_unit

    def set_mass_unit(self, mass_unit: str):
        self.mass_unit = mass_unit

    def set_time_unit(self, time_unit: str):
        self.time_unit = time_unit

    def set_electric_current_unit(self, electric_current_unit: str):
        self.electric_current_unit = electric_current_unit

    def set_temperature_unit(self, temperature_unit: str):
        self.temperature_unit = temperature_unit

    def set_amount_of_substance_unit(self, amount_of_substance_unit: str):
        self.amount_of_substance_unit = amount_of_substance_unit

    def set_light_intensity_unit(self, light_intensity_unit: str):
        self.light_intensity_unit = light_intensity_unit

    # power set
    def set_length_power(self, length_power):
        self.length_power = length_power

    def set_mass_power(self, mass_power):
        self.mass_power = mass_power

    def set_time_power(self, time_power):
        self.time_power = time_power

    def set_electric_current_power(self, electric_current_power):
        self.electric_current_power = electric_current_power

    def set_temperature_power(self, temperature_power):
        self.temperature_power = temperature_power

    def set_amount_of_substance_power(self, amount_of_substance_power):
        self.amount_of_substance_power = amount_of_substance_power

    def set_light_intensity_power(self, light_intensity_power):
        self.light_intensity_power = light_intensity_power

    # getter values
    def get_value(self):
        return self.value

    # getter unit
    def get_length_unit(self):
        return self.length_unit

    def get_mass_unit(self):
        return self.mass_unit

    def get_time_unit(self):
        return self.time_unit

    def get_electric_current_unit(self):
        return self.electric_current_unit

    def get_temperature_unit(self):
        return self.temperature_unit

    def get_amount_of_substance_unit(self):
        return self.amount_of_substance_unit

    def get_light_intensity_unit(self):
        return self.light_intensity_unit

    # getter power
    def get_length_power(self):
        return self.length_power

    def get_mass_power(self):
        return self.mass_power

    def get_time_power(self):
        return self.time_power

    def get_electric_current_power(self):
        return self.electric_current_power

    def get_temperature_power(self):
        return self.temperature_power

    def get_amount_of_substance_power(self):
        return self.amount_of_substance_power

    def get_light_intensity_power(self):
        return self.light_intensity_power
    #overloading
    def __add__(self, other):
        #crating a checklist for comparison of object's attributes and the other object
        length_unit_checker = self.length_unit == other.length_unit
        mass_unit_checker = self.mass_unit == other.mass_unit
        time_unit_checker = self.time_unit == other.time_unit
        electric_current_unit_checker = self.electric_current_unit == other.electric_current_unit
        temperature_unit_checker = self.temperature_unit == other.temperature_unit
        amount_of_substance_unit_checker = self.amount_of_substance_unit == other.amount_of_substance_unit
        light_intensity_unit_checker = self.light_intensity_unit == other.light_intensity_unit

        uchecklist = [length_unit_checker, mass_unit_checker, time_unit_checker, electric_current_unit_checker,
                      temperature_unit_checker, amount_of_substance_unit_checker, light_intensity_unit_checker]

        length_checker = self.length_power == other.length_power
        mass_checker = self.mass_power == other.mass_power
        time_checker = self.time_power == other.time_power
        electric_current_checker = self.electric_current_power == other.electric_current_power
        temperature_checker = self.temperature_power == other.temperature_power
        amount_of_substance_checker = self.amount_of_substance_power == other.amount_of_substance_power
        light_intensity_checker = self.light_intensity_power == other.light_intensity_power

        pchecklist = [length_checker, mass_checker, time_checker, electric_current_checker, temperature_checker,
                      amount_of_substance_checker, light_intensity_checker]

        if False in uchecklist or False in pchecklist:
            raise ValueError("Units do not match")
        else:
            tempclass = copy.deepcopy(self)
            tempclass.set_value(self.value + other.value)
            return tempclass

    def __sub__(self, other):
        length_unit_checker = self.length_unit == other.length_unit
        mass_unit_checker = self.mass_unit == other.mass_unit
        time_unit_checker = self.time_unit == other.time_unit
        electric_current_unit_checker = self.electric_current_unit == other.electric_current_unit
        temperature_unit_checker = self.temperature_unit == other.temperature_unit
        amount_of_substance_unit_checker = self.amount_of_substance_unit == other.amount_of_substance_unit
        light_intensity_unit_checker = self.light_intensity_unit == other.light_intensity_unit

        uchecklist = [length_unit_checker, mass_unit_checker, time_unit_checker, electric_current_unit_checker,
                      temperature_unit_checker, amount_of_substance_unit_checker, light_intensity_unit_checker]

        length_checker = self.length_power == other.length_power
        mass_checker = self.mass_power == other.mass_power
        time_checker = self.time_power == other.time_power
        electric_current_checker = self.electric_current_power == other.electric_current_power
        temperature_checker = self.temperature_power == other.temperature_power
        amount_of_substance_checker = self.amount_of_substance_power == other.amount_of_substance_power
        light_intensity_checker = self.light_intensity_power == other.light_intensity_power

        pchecklist = [length_checker, mass_checker, time_checker, electric_current_checker, temperature_checker,
                      amount_of_substance_checker, light_intensity_checker]

        if False in uchecklist or False in pchecklist:
            raise ValueError("Units do not match")
        else:
            tempclass = copy.deepcopy(self)
            tempclass.set_value(self.value - other.value)
            return tempclass

    def __mul__(self, other):
        if type(other) == FundUnit:
            tempclass = copy.deepcopy(self)
            tempclass.set_value(self.value * other.value)

            #
            tempclass.length_power = self.length_power + other.length_power
            tempclass.mass_power = self.mass_power + other.mass_power
            tempclass.time_power = self.time_power + other.time_power
            tempclass.electric_current_power = self.electric_current_power + other.electric_current_power
            tempclass.temperature_power = self.temperature_power + other.temperature_power
            tempclass.amount_of_substance_power = self.amount_of_substance_power + other.amount_of_substance_power
            tempclass.light_intensity_power = self.light_intensity_power + other.light_intensity_power

            return tempclass
        #for multiplication of ints and floats that are dimensionless
        elif type(other) == int or type(other) == float:
            tempclass = copy.deepcopy(self)
            tempclass.value *= other
            return tempclass

    def __truediv__(self, other):
        if type(other) == FundUnit:
            tempclass = copy.deepcopy(self)
            tempclass.set_value(self.value / other.value)
            ##
            tempclass.length_power = self.length_power - other.length_power
            tempclass.mass_power = self.mass_power - other.mass_power
            tempclass.time_power = self.time_power - other.time_power
            tempclass.electric_current_power = self.electric_current_power - other.electric_current_power
            tempclass.temperature_power = self.temperature_power - other.temperature_power
            tempclass.amount_of_substance_power = self.amount_of_substance_power - other.amount_of_substance_power
            tempclass.light_intensity_power = self.light_intensity_power - other.light_intensity_power

            return tempclass

        elif type(other) == int or type(other) == float:
            tempclass = copy.deepcopy(self)
            tempclass.set_value(self.value / other)
            return tempclass

    def __str__(self):
        strresult = f"{self.value}"
        if self.length_power != 0:
            strresult += f" {self.length_unit}^{self.length_power}"
        if self.mass_power != 0:
            strresult += f" {self.mass_unit}^{self.mass_power}"
        if self.time_power != 0:
            strresult += f" {self.time_unit}^{self.time_power}"
        if self.electric_current_power != 0:
            strresult += f" {self.electric_current_unit}^{self.electric_current_power}"
        if self.temperature_power != 0:
            strresult += f" {self.temperature_unit}^{self.temperature_power}"
        if self.amount_of_substance_power != 0:
            strresult += f" {self.amount_of_substance_unit}^{self.amount_of_substance_power}"
        if self.light_intensity_power != 0:
            strresult += f" {self.light_intensity_unit}^{self.light_intensity_power}"
        return strresult
