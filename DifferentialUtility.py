import numpy as np

def secondPartialDerivativeX(prev, dx):
    d2t = np.copy(prev)
    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            d2t[i, j] = (prev[i+1, j] - (2*prev[i, j]) + prev[i-1, j])/(dx**2)

    return d2t

def secondPartialDerivativeY(prev, dy):
    d2t = np.copy(prev)
    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            d2t[i, j] = (prev[i, j+1] - (2*prev[i, j]) + prev[i, j-1])/(dy**2)

    return d2t

def partialDerivativeX(prev, dx):
    dudx = np.copy(prev)
    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            dudx[i, j] = (prev[i+1, j] - prev[i-1, j])/(2*dx)
    
    return dudx

def partialDerivativeY(prev, dy):
    dudy = np.copy(prev)
    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            dudy[i, j] = (prev[i, j+1] - prev[i, j-1])/(2*dy)
    
    return dudy

def mixedPartial(prev, dx, dy):
    dudxdy = np.copy(prev)
    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            dudxdy[i, j] = (prev[i+1, j+1] - prev[i-1, j+1] - prev[i+1, j-1] - prev[i-1, j-1])/(4*dx*dy)
    
    return dudxdy

def heatEquationPartials(prev, dx, dy):
    uxx = np.copy(prev)
    uyy = np.copy(prev)

    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            uxx[i, j] = (prev[i+1, j] - (2*prev[i, j]) + prev[i-1, j])/(dx**2)
            uyy[i, j] = (prev[i, j+1] - (2*prev[i, j]) + prev[i, j-1])/(dy**2)

    return (uxx, uyy)


def levelSetPartials(prev, dx, dy):
    ux = np.copy(prev)
    uy = np.copy(prev)
    uxx = np.copy(prev)
    uyy = np.copy(prev)
    uxy = np.copy(prev)

    for i in range(1, len(prev) - 1):
        for j in range(1, len(prev[i]) - 1):
            uxy[i, j] = (prev[i+1, j+1] - prev[i-1, j+1] - prev[i+1, j-1] - prev[i-1, j-1])/(4*dx*dy)
            uy[i, j] = (prev[i, j+1] - prev[i, j-1])/(2*dy)
            ux[i, j] = (prev[i+1, j] - prev[i-1, j])/(2*dx)
            uyy[i, j] = (prev[i, j+1] - (2*prev[i, j]) + prev[i, j-1])/(dy**2)
            uxx[i, j] = (prev[i+1, j] - (2*prev[i, j]) + prev[i-1, j])/(dx**2)

    return [ux, uy, uxy, uxx, uyy]