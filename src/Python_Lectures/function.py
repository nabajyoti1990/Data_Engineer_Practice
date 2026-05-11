from loguru import logger

def details(**param):
    for i,j in param.items():
        logger.info(f"{i} has value {j}")
        
details(Name="Nabajyoti",age=36,city="Bhubaneswar")
