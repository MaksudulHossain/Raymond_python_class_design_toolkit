"""Advanced Circle Analytics - A comprehensive circle computation toolkit."""
import math 

class Circle(object):
    """Represents a circle with radius-based calculations.
    
    This class provides methods for computing area, perimeter, and other
    circle-related properties with support for subclassing and extension.

    Circle class with full Python toolkit support.
    """
    VERSION = "1.2.3" #class variable - shared across all instances

    def __init__(self, radius):
        """Initialize a circle with a given radius"""
        self.radius = radius #instance var -  unique per instance

    def area(self):
        return math.pi * self.radius**2


