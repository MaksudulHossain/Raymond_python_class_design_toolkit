"""Advanced Circle Analytics - A comprehensive circle computation toolkit."""

class Circle(object):
    """Represents a circle with radius-based calculations.
    
    This class provides methods for computing area, perimeter, and other
    circle-related properties with support for subclassing and extension.

    Circle class with full Python toolkit support.
    """
    VERSION = "1.2.3" #class variable - shared across all instances
    PI = 3.141592654 #but better to import from math 

    def __init__(self, radius):
        """Initialize a circle with a given radius"""
        self.radius = radius #instance var -  unique per instance


