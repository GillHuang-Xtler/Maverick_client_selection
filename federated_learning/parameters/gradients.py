import numpy

def calculate_model_gradient(logger, model_1, model_2):
    model_1_parameters = list(dict(model_1.state_dict()))
    model_2_parameters = list(dict(model_2.state_dict()))

    return calculate_parameter_gradients(logger, model_1_parameters, model_2_parameters)

def calculate_parameter_gradients(logger, params_1, params_2):
    logger.debug("Shape of model_1_parameters: {}".format(str(len(params_1))))
    logger.debug("Shape of model_2_parameters: {}".format(str(len(params_2))))

    return numpy.array([x for x in numpy.subtract(params_1, params_2)])
