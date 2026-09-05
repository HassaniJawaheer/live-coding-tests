def filter_predictions(predictions, threshold):
    return [
        (filename, label)
        for filename, label, rate in predictions
        if rate >= threshold
    ]
