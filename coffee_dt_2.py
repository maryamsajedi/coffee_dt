
# NOTE: In version v0.1.0, the model is defined using dt_model library. 
from dt_model import UniformCategoricalContextVariable, PresenceVariable, Constraint, Model, Index
import numpy as np
from sympy import Symbol


# Context Variables
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
CV_weekday = UniformCategoricalContextVariable('weekday', [Symbol(v) for v in days])

# Presence Variables
drink_customers = PresenceVariable(
    name='drink_customers', 
    cvs=[], )
food_customers = PresenceVariable(
    'food_customers',
    cvs= [],
)

# Capacity Index
capacity = Index('capacity', 50)

# Usage Index
U_drink_customers = Index('drink service usage factor', 1)
U_food_customers = Index('food service usage factor', 1)

# Constraints
C_drink_customers = Constraint(usage=drink_customers * U_drink_customers + food_customers*U_food_customers, capacity=capacity)

# Define the model
model = Model(
    'coffee_shop',
    cvs=[],
    pvs=[drink_customers, food_customers],
    indexes=[capacity, U_drink_customers, U_food_customers],
    constraints=[C_drink_customers],
    capacities=[capacity]
)

# We define a scenario where we have a fake ensemble of only one weekday.
fake_ensemble = [
(1, {"weekday": "monday"}),
]

grid = {
    drink_customers: np.linspace(0, 100, 10),
    food_customers: np.linspace(0, 100, 10)
}

print("Now we can evaluate our model")
print(model.evaluate(grid, fake_ensemble))

