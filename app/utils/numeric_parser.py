from fastapi import HTTPException

def parser(value:None):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:  
            raise HTTPException(status_code=400, detail="Invalid temperature value")