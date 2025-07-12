def apply_class_label_replacement(X, Y, replacement_method):
    return (X, replacement_method(Y, set(Y)))


