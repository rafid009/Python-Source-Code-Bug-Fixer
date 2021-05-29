import numpy as np 

def function(x):

	v6 = x
	r0 = x
	paths = []
	try:
		if v6 > 4:
			r0 = x-r0
			x = x-x
			paths.append(1)
		else:
			v6 = v6+v6
			x = x*x
			x = v6*7
			paths.append(2)
		if x < 9:
			x = x*r0
			r0 = 1*r0
			x = 9*x
			paths.append(3)
		else:
			v6 = v6-5
			r0 = r0-x
			v6 = 6*5
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))