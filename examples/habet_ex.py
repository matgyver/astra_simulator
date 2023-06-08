#42.027681, -93.653945
"""
example_forecast.py
ASTRA High Altitude Balloon Flight Planner

DESCRIPTION
--------------

Example: Forecast based Simulation

University of Southampton
Niccolo' Zapponi, nz1g10@soton.ac.uk, 22/04/2013
"""
import logging
import numpy as np
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    from datetime import datetime, timedelta
    from astra.simulator import *

    np.random.seed(62)

    # Environment parameters
    # Launch site: Ames, IA
    #        time: tomorrow, this time
    launch_datetime = datetime.now() + timedelta(days=1)
    simEnvironment = forecastEnvironment(launchSiteLat=42.027681,      # deg
                                         launchSiteLon=--93.653945,     # deg
                                         launchSiteElev=304,           # m
                                         dateAndTime=launch_datetime,
                                         forceNonHD=True,
                                         debugging=True)

    # Launch setup
    simFlight = flight(environment=simEnvironment,
                       balloonGasType='Helium',
                       balloonModel='TA3000',
                       nozzleLift=2.0,                                # kg
                       payloadTrainWeight=0.433,                    # kg
                       parachuteModel='SPH36',
                       numberOfSimRuns=10,
                       trainEquivSphereDiam=0.1,                    # m
                       floatingFlight=False,
                       excessPressureCoeff=1,
                       outputFile=os.path.join('.', 'astra_output'),
                       debugging=True,
                       log_to_file=True)

    # simFlight.maxFlightTime = 5*60*60

    # Run the simulation
    simFlight.run()
