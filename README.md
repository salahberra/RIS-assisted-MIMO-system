## User_Location_RIS

The reflecting intelligent surface (RIS) technology is a novel emergery of the beyond 5G, which has gotten a lot of interest research in the future.
A RIS is a planar array consisting of multiple low-cost reflecting elements. Each element can steer the incident signal through passive beamforming, and thus, RIS can reconfigure the wireless environment to facilitate information transmission.
In this work, a RIS can help a multi-input multi-output (MIMO) system to control the physical propagation environment and the direction of the no line of sight (NLOS) channel. As a result of this benefit, RIS can improve the broadcast of the base station vers users, which increases the data rate for each user.
in the first package,
```python
User_Location_RIS
```
 the location of users vers RIS are most important to control the signal, which select by the area. As the figure below, which explain the dimession of area depnded on the position of X and position of Y, and also the source of two-channel of the line of sight and no line of sight as represented.

In the test of the package, The two circle has been defined to select the inside and outside of the area. For example, the point red is defined by the users when they are inside the green circle then the test is passed when they are out of the green circle, the test is failed.
In the parameters test, a number of users, random value for amplitude and phase.

![System model.](https://github.com/salahberra/RIS-assited-MIMO-system/raw/master/figures/RIS.png)