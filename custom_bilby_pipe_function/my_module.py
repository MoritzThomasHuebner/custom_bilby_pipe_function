from bilby.gw.source import lal_binary_black_hole


def my_function(frequency_array, mass_1, mass_2, luminosity_distance, a_1, tilt_1,
                phi_12, a_2, tilt_2, phi_jl, theta_jn, phase, **kwargs):
    return lal_binary_black_hole(frequency_array, mass_1, mass_2, luminosity_distance,
                                 a_1, tilt_1, phi_12, a_2, tilt_2, phi_jl, theta_jn, phase, **kwargs)