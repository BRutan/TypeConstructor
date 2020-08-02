################################
# TypeConstructor.py
################################
# Description:
# * Singleton class that generates
# new instances from type objects.

import re
import sys
import types

class TypeConstructor:
    """
    * Singleton class that generates
    new instances from type objects.
    """
    __replacements = re.compile('|'.join(['class', '<', '>',"'", ' +']))
    ################
    # Interface Methods:
    ################
    @classmethod
    def ConstructType(cls, typeObj):
        """
        * Generate instance of type without arguments
        Inputs:
        * typeObj: type object to construct.
        """
        errs = []
        if not isinstance(typeObj, type):
            errs.append('typeObj must be a type.')
        if errs:
            raise ValueError('\n'.join(errs))
        module, classname = TypeConstructor.SplitType(typeObj)
        return TypeConstructor.__CreateClassObj(module, classname)

    @classmethod
    def ConstructTypeArgs(cls, typeObj, *args):
        """
        * Generate instance of type using 
        *args style arguments.
        Inputs:
        * typeObj: type object to construct.
        * args: variadic list containing objects to be fed to constructor. 
        """
        errs = []
        if not isinstance(typeObj, type):
            errs.append('typeObj must be a type.')
        if errs:
            raise ValueError('\n'.join(errs))
        module, classname = TypeConstructor.SplitType(typeObj)
        return TypeConstructor.__CreateClassObj(module, classname, args)

    @classmethod
    def ConstructTypeKwargs(cls, typeObj, **kwargs):
        """
        * Generate instance of type using 
        **kwargs style arguments.
        Inputs:
        * typeObj: type object to construct.
        * kwargs: dictionary containing objects to be fed to constructor. 
        """
        errs = []
        if not isinstance(typeObj, type):
            errs.append('typeObj must be a type.')
        if errs:
            raise ValueError('\n'.join(errs))
        module, classname = TypeConstructor.SplitType(typeObj)
        return TypeConstructor.__CreateClassObj(module, classname, kwargs)
        
    @classmethod
    def SplitType(cls, typeObj):
        """
        * Get the entity name from the type.
        Returns (module, classname).
        Inputs:
        * typeObj: type object.
        """
        if not isinstance(typeObj, type):
            raise ValueError('typeObj must be a type.')
        name = str(typeObj)
        module = TypeConstructor.__StripChars(name[0:name.rfind('.')])
        classname = TypeConstructor.__StripChars(name[name.rfind('.') + 1:len(name)])
        return module, classname

    @classmethod
    def IsImported(cls, module):
        """
        * Check that module has been imported.
        Inputs:
        * module: string module name.
        """
        if not isinstance(module, str):
            raise ValueError('module must be a string.')
        return module in sys.modules

    ################
    # Private Helpers:
    ################
    @staticmethod
    def __FindModules(module):
        """
        * Search for all modules at all depths from
        which to perform class construction.
        """
        modules = []
        while module != '':
            if module in sys.modules:
                modules.append(module)
            if '.' not in module:
                break
            module = module[0:module.rfind('.')]
        return set(modules)

    @staticmethod
    def __CreateClassObj(module, classname, args = None):
        """
        * Create class object using one of the 
        modules at depth.
        """
        modules = TypeConstructor.__FindModules(module)
        # Attempt to construct class from one of the modules:
        for mod in modules:
            try:
                if isinstance(args, dict):
                    return getattr(sys.modules[mod], classname)(**args)
                elif isinstance(args, tuple):
                    return getattr(sys.modules[mod], classname)(*args)
                else:
                    return getattr(sys.modules[mod], classname)()
            except:
                pass
        raise Exception('Could not construct class %s at any module depth in %s.' % module)

    @staticmethod
    def __StripChars(val):
        """
        * Strip characters from module/class name.
        """
        return TypeConstructor.__replacements.sub('', val)
