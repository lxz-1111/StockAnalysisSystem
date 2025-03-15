try:
    import requests
    import pandas as pd
    import numpy as np
    import matplotlib
    from dateutil import parser
    
    print('所有依赖库已正确安装:')
    print(f'requests版本: {requests.__version__}')
    print(f'pandas版本: {pd.__version__}')
    print(f'numpy版本: {np.__version__}')
    print(f'matplotlib版本: {matplotlib.__version__}')
except ImportError as e:
    print(f'依赖库缺失: {e}')
    print('请运行: pip install -r requirements.txt')