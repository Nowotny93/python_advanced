class NameTooShortError(Exception):
    """Raised when the input value is too small"""

class MustContainAtSymbolError(Exception):
    """Raised when symbol '@' is not in the input"""

class InvalidDomainError(Exception):
    """Raised when domail of input does not contain 'bg' or 'com' or 'net' or 'org'"""

email = input()

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    email_domain_splt = email.split('.')
    if email_domain_splt[-1] != 'com' and email_domain_splt[-1] != 'bg' and email_domain_splt[-1] != 'net' and email_domain_splt[-1] != 'org':
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    email_splt = email.split('@')
    email_name = email_splt[0]
    if len(email_name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    else:
        print('Email is valid')
    email = input()