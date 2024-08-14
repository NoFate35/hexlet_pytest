class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)
    def __init__(self, **options):
        for opt in options:
            if opt not in self.OPTIONS:
                del options[opt]
        for opt in options:
            if opt == 'min_len':
                if not isinstance(options[opt], int):
                    del options[opt]
            if opt == 'contain_numbers':
                if not isinstance(options[opt], bool):
                    del options[opt]
        self.OPTIONS = options
        #print('options', options)
    def validate(self, password):
        char_len = len(password)
        errors = dict()
        if char_len < self.OPTIONS['min_len']:
            errors['min_len'] = 'too small'
        if self.OPTIONS['contain_numbers'] == True:
            rez = self._has_number(password)
            if rez is False:
                errors['contain_numbers'] = 'should contain at least one number'
        print('errors', errors)
        return errors
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)
