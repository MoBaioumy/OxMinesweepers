import numpy as np

# Helper functions. This is usually in a separate file
def sim_dynamics(input_force, x, v):
     return (input_force - k1*x - k2*v)/m

def rk4_int(prior, time_step, derivative):
    """
        Implements RK4 integration for one time-step
    """
    h = time_step
    f_dot = derivative
    f_t_min = prior

    k1 = h*f_dot
    k2 = h*(f_dot + k1/2)
    k3 = h*(f_dot + k2/2)
    k4 = h*(f_dot + k3)

    f_t = f_t_min + (k1 + 2*k2 + 2*k3 +k4)/6
    return f_t
