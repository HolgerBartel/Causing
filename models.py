# -*- coding: utf-8 -*-
"""Model Examples."""

from sympy import symbols


def example():
    """model example"""

    X1, X2, Y1, Y2, Y3 = symbols(["X1", "X2", "Y1", "Y2", "Y3"])

    def define_equations(X1, X2):

        eq_Y1 = X1
        eq_Y2 = X2 + 2 * Y1**2
        eq_Y3 = Y1 + Y2

        return eq_Y1, eq_Y2, eq_Y3

    model_dat = {
        "define_equations": define_equations,   # equations in topological order
        "xvars": [X1, X2],                      # exogenous variables in desired order
        "yvars": [Y1, Y2, Y3],                  # endogenous variables in topological order
        "ymvars": [Y3],                         # manifest endogenous variables
        "final_var": Y3,                        # final variable of interest, for mediation analysis
        "show_nr_indiv": 3,                     # show first individual effects
        "dir_path": "output/",                  # output directory path
        }

    # simulate data
    import utils
    simulation_dat = {
        "xmean_true": [3, 2],                   # mean of exogeneous data
        "sigx_theo": 1,                         # true scalar error variance of xvars
        "sigym_theo": 1,                        # true scalar error variance of ymvars
        "rho": 0.2,                             # true correlation within y and within x vars
        "tau": 200,                             # nr. of simulated observations
        }
    model_dat.update(simulation_dat)
    xdat, ymdat = utils.simulate(model_dat)

    # save data
# =============================================================================
#     from numpy import savetxt
#     savetxt("data/xdat.csv", xdat, delimiter=",")
#     savetxt("data/ymdat.csv", ymdat, delimiter=",")
# =============================================================================

    # load data
# =============================================================================
#     from numpy import loadtxt
#     xdat = loadtxt("data/xdat.csv", delimiter=",").reshape(len(model_dat["xvars"]), -1)
#     ymdat = loadtxt("data/ymdat.csv", delimiter=",").reshape(len(model_dat["ymvars"]), -1)
# =============================================================================

    model_dat["xdat"] = xdat                    # exogenous data
    model_dat["ymdat"] = ymdat                  # manifest endogenous data

    return model_dat

def example2():
    """model example 2, no regularization required, no latent variables"""

    X1, Y1 = symbols(["X1", "Y1",])

    def define_equations(X1):

        eq_Y1 = X1

        return [eq_Y1]

    model_dat = {
        "define_equations": define_equations,
        "xvars": [X1],
        "yvars": [Y1],
        "ymvars": [Y1],
        "final_var": Y1,
        "show_nr_indiv": 3,
        "dir_path": "output/",
        }

    # simulate data
    import utils
    simulation_dat = {
        "xmean_true": [3],
        "sigx_theo": 1,
        "sigym_theo": 1,
        "rho": 0.2,
        "tau": 200,
        }
    model_dat.update(simulation_dat)
    xdat, ymdat = utils.simulate(model_dat)

    model_dat["xdat"] = xdat
    model_dat["ymdat"] = ymdat

    return model_dat

def example3():
    """model example 3
    
    difficult to estimate:
    if just Y3 is manifest, huge regularization is required and direct effects are strongly biased,
    (if all yvars are manifest, just slight regularization is required and some standard errors are huge)
    """

    X1, Y1, Y2, Y3 = symbols(["X1", "Y1", "Y2", "Y3"])

    def define_equations(X1):

        eq_Y1 = 2 * X1
        eq_Y2 = -X1
        eq_Y3 = Y1 + Y2

        return eq_Y1, eq_Y2, eq_Y3

    model_dat = {
        "define_equations": define_equations,
        "xvars": [X1],
        "yvars": [Y1, Y2, Y3],
        "ymvars": [Y3],
        "final_var": Y3,
        "show_nr_indiv": 3,
        "dir_path": "output/",
        }

    # simulate data
    import utils
    simulation_dat = {
        "xmean_true": [3],
        "sigx_theo": 1,
        "sigym_theo": 1,
        "rho": 0.2,
        "tau": 200,
        }
    model_dat.update(simulation_dat)
    xdat, ymdat = utils.simulate(model_dat)

    model_dat["xdat"] = xdat
    model_dat["ymdat"] = ymdat

    return model_dat

def education():
    """model example"""

    (TIMETRND, X2, Y1, Y2, Y3
     ) = symbols(["TIMETRND", "X2", "Y1", "Y2", "Y3"])
    # EDUC, LOGWAGE, POTEXPER, TIMETRND, ABILITY, MOTHERED, FATHERED, BRKNHOME, SIBLINGS 

    def define_equations(X1, X2):

        eq_Y1 = X1
        eq_Y2 = X2 + 2 * Y1**2
        eq_Y3 = Y1 + Y2
        
        # time varying
        EDUC = 1 * TIMETRND
        LOGWAGE = 1 * TIMETRND
        POTEXPER = 1 * TIMETRND
        
        # time invariant
        ABILITY 
        MOTHERED 
        FATHERED 
        BRKNHOME 
        SIBLINGS 

        return eq_Y1, eq_Y2, eq_Y3

    model_dat = {
        "define_equations": define_equations,   # equations in topological order
        "xvars": [X1, X2],                      # exogenous variables in desired order
        "yvars": [Y1, Y2, Y3],                  # endogenous variables in topological order
        "ymvars": [Y3],                         # manifest endogenous variables
        "final_var": Y3,                        # final variable of interest, for mediation analysis
        "show_nr_indiv": 3,                     # show first individual effects
        "dir_path": "output/",                  # output directory path
        }


    # load data
    from numpy import loadtxt
    xymdat = loadtxt("data/education.csv", delimiter=",").reshape(-1, 10)
    xymdat = xymdat.T # observation in columns
    xymdat = xymdat[1:] # deleted PERSONID
    
    print(xymdat)
    print(xymdat.shape)
    1/0

    model_dat["xdat"] = xdat                    # exogenous data
    model_dat["ymdat"] = ymdat                  # manifest endogenous data

    return model_dat

