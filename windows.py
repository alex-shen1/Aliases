import os

if os.name != 'nt':
    raise Exception('This should only be run on Windows')

with open('.aliases', 'r') as f:
    aliases = f.read().split('\n')

profile = os.path.expanduser('~') + '\\Documents\\WindowsPowerShell\\Microsoft.PowerShell_profile.ps1'
os.makedirs(os.path.dirname(profile), exist_ok=True)
with open(profile, 'w+') as f:
    # These are already Windows aliases but I don't care what they're supposed to be
    f.write(f'del alias:gc -Force\n')
    f.write(f'del alias:gcm -Force\n')
    f.write(f'del alias:gp -Force\n')
    for alias in aliases:
        if alias[0:5] == 'alias' and '<' not in alias:
            # The alias name will always start at index 6
            name = alias[6:alias.index('=')]
            value = alias[alias.index('=') + 2:-1]

            f.write(f'Function {name}_ {{{value}}}\n')
            f.write(f'Set-Alias -Name {name} -Value {name}_\n\n')
