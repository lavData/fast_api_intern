def pattern_ex(des, ex):
    return {
        "description": des,
        "content": {
            "application/json": {
                "example": ex
            }
        }
    }
