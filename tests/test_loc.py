import pytest
from User_Location_RIS.loc import pos
import numpy as np 

x=200 # height of the base station BS
y=30  # width of the base station  BS
r=10  # optimal rang raduis to select the area
R=12  # maximal Radius
users=pos(x,y,r,R)
#K=5 #number of users
Qos=0.8 #quaility of test 

@pytest.mark.parametrize(
    'test_input, expected',
    [(1, Qos), (2, Qos), (3, Qos), (4, Qos), (5, Qos), (6, Qos), (7, Qos), (8, Qos)])
def test_location_values(test_input, expected):
    location = users.position(test_input) #based on num of users
    users.plot(location)
    coverage = 0
    for i in range(len(location)):
        if np.sqrt(np.power(location[i,0]-x,2)+np.power(location[i,1]-y,2)) <= r: " compare each users raduis Any of user out of r-coverage"
        coverage += 1
    assert coverage/test_input >= expected     
@pytest.mark.parametrize(
    'input, exception',
    [(-1, ValueError), (-5000, ValueError),
    (-1.4, TypeError), ('hello world', TypeError), ((1, 2, 3, 4), TypeError)])
def test_location_values_errors(input, exception):
    with pytest.raises(exception):     
        location = users.position(input) #based on num of users
    users.plot(location)
    coverage = 0
    for i in range(len(location)):
        if np.sqrt(np.power(location[i,0]-x,2)+np.power(location[i,1]-y,2)) <= r: "Any of user out of r-coverage"
        coverage += 1
    assert coverage/input >= exception 