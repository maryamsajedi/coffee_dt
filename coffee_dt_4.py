# NOTE: version v0.3.0, we are adding another constraint to the model. The model is now considering the capacity of the food service.       
from dt_model import UniformCategoricalContextVariable, PresenceVariable, Constraint, Ensemble, Model, Index
import numpy as np
from sympy import Symbol


# Context Variables
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
CV_weekday = UniformCategoricalContextVariable('weekday', [Symbol(v) for v in days])

# Presence Variables
drink_customers = PresenceVariable(
    name='drink_customers', 
    cvs=[], 
)       
food_customers = PresenceVariable(
    'food_customers',
    cvs= [],
) 

# Capacity Index can be defined as a 
seat_capacity = Index('seat_capacity', 50) # There are 50 seats available in the bar        
service_capacity = Index('service_capacity', 100) # 100 customers can be served in the bar during the day

U_drink_seat = Index('drink customers seat usage factor', 0.2) # Usage of drink customers from the seats available in the bar
U_food_seat = Index('food customers seat usage factor', 0.8) # Usage of food customers from the seats available in the bar

U_service_drink = Index('drink customers service usage factor', 0.4) # Usage of drink customers from the service
U_service_food = Index('food customers service usage factor', 0.9) # Usage of food customers from the service


# Constraints
seat_constraint = Constraint(
    usage=drink_customers * U_drink_seat + food_customers * U_food_seat,
    capacity=seat_capacity
)

service_constraint = Constraint(
    usage=food_customers*U_service_food  + drink_customers*U_service_drink,
    capacity=service_capacity
)

# Define the model
model = Model(
    'coffee_shop',
    cvs=[CV_weekday],
    pvs=[drink_customers, food_customers],
    indexes=[seat_capacity, U_drink_seat, U_food_seat, U_service_drink, U_service_food, service_capacity],
    constraints=[seat_constraint, service_constraint],
    capacities=[seat_capacity, service_capacity]
)   

ensemble = Ensemble(model, {CV_weekday: days}, cv_ensemble_size=7)

grid = {
    drink_customers: np.linspace(0, 100, 10),
    food_customers: np.linspace(0, 100, 10)
}

print("Now we can evaluate our model")
print(model.evaluate(grid, ensemble))
