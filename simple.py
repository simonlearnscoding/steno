from contextlib import suppress



from plover_vim.relative_number.builtins import RelativeNumberLookup as RelativeNumberLookup
from plover_vim.Josiah_modifier.builtins import Lookup as JosiahModifierLookup
Josiah_modifier_lookup = JosiahModifierLookup()
relative_number_lookup = RelativeNumberLookup()
LONGEST_KEY = 1
def lookup(key):
    for look in [
        relative_number_lookup,
        Josiah_modifier_lookup
    ]:
        with suppress(KeyError):
            return look(key)
    raise KeyError