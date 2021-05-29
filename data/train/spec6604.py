import numpy as np 

def function(x):

	u1 = x
	v5 = x
	paths = []
	try:
		if u1 < 5:
			v5 = v5/9
			paths.append(1)
		else:
			x = 0-x
			v5 = v5*0
			paths.append(2)
		if v5 < 7:
			v5 = v5*7
			paths.append(3)
		else:
			v5 = v5-6
			v5 = 6+v5
			v5 = 3*v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))