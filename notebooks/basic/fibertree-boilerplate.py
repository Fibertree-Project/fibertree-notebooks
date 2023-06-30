# Begin - startup boilerplate code\n
\n
import pkgutil\n
\n
if 'fibertree_bootstrap' not in [pkg.name for pkg in pkgutil.iter_modules()]:\n
  !pip  install git+https://github.com/Fibertree-project/fibertree-bootstrap --quiet\n
\n
# End - startup boilerplate code\n