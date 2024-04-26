

odd_examples = {
    "odd": {
        "summary": "Odd number",
        "value": {
            "value": 1111
        }
    },
    "even": {
        "summary": "Even number",
        "value": {
            "value": 322
        }
    },
    "alphabet": {
        "summary": "Example using alphabet",
        "description": "Using invalid, non-number input. Will raise `Error: Unprocessable Entity` message.",
        "value": {
            "value": "abc"
        }
    },
}

odd_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "odd": {
                        "summary": "Odd Number",
                        "value": {"code": 0, "message": "Success", "result": True}
                    },
                    "even": {
                        "summary": "Even Number",
                        "value": {"code": 0, "message": "Success", "result": False}
                    },
                }
            }
        }
    },
}