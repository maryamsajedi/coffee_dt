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
seat_capacity = Index('seat_capacity', 50)
food_capacity = Index('food_capacity', 100)

# NOTE: We are going to change the usage factors to 0.5 for both drink and food customers
U_drink_customers = Index('drink service usage factor', 0.3)
U_food_customers = Index('food service usage factor', 0.7)

# Constraints
seat_constraint = Constraint(usage=drink_customers*U_drink_customers + food_customers*U_food_customers, capacity=seat_capacity)
food_constraint = Constraint(usage=food_customers*U_food_customers, capacity=food_capacity)


# Define the model
model = Model(
    'coffee_shop',
    cvs=[CV_weekday],
    pvs=[drink_customers, food_customers],
    indexes=[seat_capacity, U_drink_customers, U_food_customers],
    constraints=[seat_constraint, food_constraint],
    capacities=[seat_capacity, food_capacity]
)   

ensemble = Ensemble(model, {CV_weekday: days}, cv_ensemble_size=7)

grid = {
    drink_customers: np.linspace(0, 100, 10),
    food_customers: np.linspace(0, 100, 10)
}

print("Now we can evaluate our model")
print(model.evaluate(grid, ensemble))
