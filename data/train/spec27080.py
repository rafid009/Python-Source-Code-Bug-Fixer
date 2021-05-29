import numpy as np 

def function(x):

	v9 = x
	v6 = 2
	x = x
	paths = []
	try:
		if v6 < 6:
			v6 = v6-6
			paths.append(1)
		else:
			x = 2-x
			v9 = v6+v6
			paths.append(2)
		if v6 >= 2:
			v6 = v6+3
			v9 = v9*3
			paths.append(3)
		else:
			v9 = v9*0
			v9 = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))