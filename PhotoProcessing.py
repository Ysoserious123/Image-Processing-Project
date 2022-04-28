import numpy as np
import DifferentialUtility as diff

def heatEquation(currentState, h, dt):
    prev = np.copy(currentState)

    uxx, uyy = diff.heatEquationPartials(prev, h, h)

    prev[1:-1, 1:-1] = prev[1:-1, 1:-1] + (dt)*(uxx + uyy)[1:-1, 1:-1]

    # We only want to add up everything except the edges, so we do that
    # prev[1:-1, 1:-1] = prev[1:-1, 1:-1] + (dt/(h**2))*(secondPartialDerivativeX(prev, h) + secondPartialDerivativeY(prev, h))[1:-1, 1:-1]

    # Then we set the next equal to the previous with the updated interior
    next = prev

    return next

def levelSet(currentState, h, dt, epsilon):
    prev = np.copy(currentState)

    ux, uy, uxy, uxx, uyy = diff.levelSetPartials(prev, h, h)
    prev[1:-1, 1:-1] = prev[1:-1, 1:-1] + (dt)*((((ux**2)*uyy) - (2*ux*uy*uxy) + ((uy**2)*uxx)) / (ux**2 + uy**2 + epsilon))[1:-1, 1:-1]

    # prev[1:-1, 1:-1] = prev[1:-1, 1:-1] + (dt/(h**2))*((((partialDerivativeX(prev, h)**2)*secondPartialDerivativeY(prev, h)) - (2*partialDerivativeX(prev, h)*partialDerivativeY(prev, h)*mixedPartial(prev, h, h)) + ((partialDerivativeY(prev, h)**2)*secondPartialDerivativeX(prev, h))) / (partialDerivativeX(prev, h)**2 + partialDerivativeY(prev, h)**2 + epsilon))[1:-1, 1:-1]

    next = prev

    return next

def shockFilter(currentState, h, dt):
    prev = np.copy(currentState)

    ux, uy, uxx, uyy = diff.shockFilterPartials(prev, h, h)
    prev[1:-1, 1:-1] = prev[1:-1, 1:-1] - (dt)*(np.sqrt(ux**2 + uy**2)*(uxx + uyy))[1:-1, 1:-1]

    next = prev

    return next

def modifiedLevelSet(currentState, original, h, dt, epsilon, alpha):
    prev = np.copy(currentState)
    ux, uy, uxy, uxx, uyy = diff.levelSetPartials(prev, h, h)
    prev[1:-1, 1:-1] = prev[1:-1, 1:-1] + (dt)*((((ux**2)*uyy) - (2*ux*uy*uxy) + ((uy**2)*uxx)) / (ux**2 + uy**2 + epsilon))[1:-1, 1:-1]

    prev[1:-1, 1:-1] = prev[1:-1, 1:-1] - alpha*(prev[1:-1, 1:-1] - original[1:-1, 1:-1])

    next = prev

    return next

def runHeatEquation(image, total_time, dt):
    time = 0.0
    initial_image = np.copy(image)
    while time < total_time:
        image = heatEquation(image, 1, dt)
        time += dt
    return (initial_image, image)

def runLevelSet(image, total_time, dt, epsilon):
    time = 0.0
    initial_image = np.copy(image)
    while time < total_time:
        image = levelSet(image, 1, dt, epsilon)
        time += dt
    return (initial_image, image)

def runModifiedLevelSet(image, total_time, dt, epsilon, alpha):
    # print("running modified level set", epsilon, alpha)
    time = 0.0
    initial_image = np.copy(image)
    while time < total_time:
        image = modifiedLevelSet(image, initial_image, 1, dt, epsilon, alpha)
        time += dt
    return (initial_image, image)

def runShockFilter(image, total_time, dt):
    # print("running modified level set", epsilon, alpha)
    time = 0.0
    initial_image = np.copy(image)
    while time < total_time:
        image = shockFilter(image, 1, dt)
        time += dt
    return (initial_image, image)

def processImage(image, method, total_time, dt, **kwargs):

    # threadsperblock = (16, 16)
    # blockspergrid_x = int(np.ceil(image.shape[0] / threadsperblock[0]))
    # blockspergrid_y = int(np.ceil(image.shape[1] / threadsperblock[1]))
    # blockspergrid = (blockspergrid_x, blockspergrid_y)

    method_dict = {'heat': lambda : runHeatEquation(image, total_time, dt), 
               'level-set': lambda : runLevelSet(image, total_time, dt, kwargs["epsilon"]), 
               'modified-level-set': lambda : runModifiedLevelSet(image, total_time, dt, kwargs['epsilon'], kwargs['alpha']),
               'shock-filter': lambda : runShockFilter(image, total_time, dt)
               }

    return method_dict[method]()
    