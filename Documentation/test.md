## The test of package location RIS

The first package of ````def position````presents the radius of users based on the highest of the base station.
in this package: 
```` amplitude=np.random.uniform```` generate the most random amplitude for each user.
```` theta=np.random.uniform````generate the most random angle (phase) for each user.
the output of the package will be present in the radius of users compared with the base station. Then, the RIS will be used to affect the area that users can't receive the signal. As result, RIS can help cover and signal propagation.

In the Test: 
A number of users can be tested with different amplitude and phases, and fix the radius of the base station.
``@pytest.mark.parametrize(
    'test_input, expected',`....)``
the input is the number of users with the quality of servers, the generation of amplitude and phase is random, where phase ( 0 to 2pi) and amplitude ( 0 to 20).
another test based on ValueError and  TypeError.
