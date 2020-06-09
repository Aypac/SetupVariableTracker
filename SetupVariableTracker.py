from tabulate import tabulate  # Library for formatting text tables
from types import ModuleType


class SetupVariableTracker:
    """
    Usage example:

    from VariableTracker import VariableTracker
    vtrack = VariableTracker(locals())

    ##################################################
    # Define parameters for this script
    setup_variable_1 = "Hello"
    setup_variable_2 = "World!"
    foo = 1
    bar = None
    ##################################################
    # Create a summary of all newly defined variables
    summary_content = vtrack.get_table(locals(), sort=True)
    print(summary_content)
    vtrack.save()
    """
    base_vars = None

    def __init__(self, locals_c, delete: bool = False, verbose: bool = False):
        self._verbose = verbose
        # Clean up previously defined vars
        self._print("> Determining variables defined prior...")
        self.base_vars = list(locals_c.keys())[:]
        if delete:
            for k in self.base_vars:
                if k not in ['base_vars', 'dict', 'locals', 'ModuleType'] and not isinstance(locals_c[k], ModuleType):
                    if k[0] != '_' and k in self.base_vars:
                        try:
                            del self.base_vars[k]
                            exec(f"del {k:s}")
                        except:
                            pass
                del k

    def _print(self, msg):
        if self._verbose:
            print(msg)

    def get_variables(self, locals_c, sort: bool = False):
        # Generate overview of defined variables (ignore this)
        self._print("> Determining newly defined variables...")
        new_vars = list(locals_c.keys())[:]
        new_vars = [k for k in new_vars if k not in self.base_vars]

        nv = dict(locals_c)

        if sort:
            new_vars.sort(key=str.lower)
        items = [[k, nv[k]] for k in new_vars if not isinstance(locals_c[k], type(self))]
        return items

    def get_table(self, locals_c, sort: bool = False):
        self._print("> Generate variable overview...")
        items = self.get_variables(locals_c, sort=sort)
        return tabulate(items, headers=['Parameter', 'Value'], tablefmt="rst")

    def save(self, filename=None):
        if not filename:
            import datetime
            filename = datetime.datetime().strftime("YYYY-MM-DD_HH-MM-SS") + "_SetupVariables.log"

        import codecs
        with codecs.open(filename, 'w', 'utf-8') as f:
            f.write(self.get_table())
            f.flush()
