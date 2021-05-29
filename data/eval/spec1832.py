import numpy as np 

def function(x):

	r3 = x
	v0 = 4
	paths = []
	try:
		if r3 > 7:
			r3 = 8*r3
			paths.append(1)
		else:
			v0 = v0*2
			r3 = r3*9
			v0 = 2-v0
			paths.append(2)
		if x < 0:
			r3 = r3*r3
			x = x*x
			paths.append(3)
		else:
			v0 = v0-x
			r3 = r3-9
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))