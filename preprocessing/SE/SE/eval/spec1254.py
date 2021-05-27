import numpy as np 

def function(x):

	v6 = x
	i7 = 5
	paths = []
	try:
		if i7 >= 9:
			v6 = 7/v6
			v6 = v6*v6
			paths.append(1)
		else:
			i7 = i7-i7
			v6 = v6*v6
			x = 2*x
			paths.append(2)
		if x > 7:
			x = x/v6
			i7 = i7+5
			paths.append(3)
		else:
			v6 = v6+v6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))