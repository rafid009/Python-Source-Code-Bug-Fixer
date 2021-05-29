import numpy as np 

def function(x):

	r3 = x
	v6 = 3
	paths = []
	try:
		if r3 <= 6:
			r3 = r3*x
			v6 = v6*v6
			r3 = x-r3
			paths.append(1)
		else:
			v6 = v6-6
			x = x+v6
			v6 = v6-9
			paths.append(2)
		if v6 <= 9:
			x = x/r3
			r3 = 0*r3
			paths.append(3)
		else:
			v6 = v6+6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		r3 = v6**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))