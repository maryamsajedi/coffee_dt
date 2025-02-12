# NOTE: version v0.3.0, we are adding another context variable to the model.
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

# Capacity Index
capacity = Index('capacity', 50)

# NOTE: We are going to change the usage factors to 0.5 for both drink and food customers
U_drink_customers = Index('drink service usage factor', 0.5)
U_food_customers = Index('food service usage factor', 0.5)

# Constraints
C_drink_customers = Constraint(usage=drink_customers*U_drink_customers + food_customers*U_food_customers, capacity=capacity)

# Define the model
model = Model(
    'coffee_shop',
    cvs=[CV_weekday],
    pvs=[drink_customers, food_customers],
    indexes=[capacity, U_drink_customers, U_food_customers],
    constraints=[C_drink_customers],
    capacities=[capacity]
)

ensemble = Ensemble(model, {CV_weekday: days}, cv_ensemble_size=7)

grid = {
    drink_customers: np.linspace(0, 100, 10),
    food_customers: np.linspace(0, 100, 10)
}

print("Now we can evaluate our model")
print(model.evaluate(grid, ensemble))
