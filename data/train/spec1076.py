import numpy as np 

def function(x):

	e6 = 7
	i0 = 4
	paths = []
	try:
		if i0 <= 2:
			e6 = 3-e6
			i0 = 7-5
			i0 = 5*i0
			paths.append(1)
		else:
			e6 = 6*e6
			e6 = 7-e6
			paths.append(2)
		if e6 <= 7:
			e6 = x*e6
			x = e6+9
			paths.append(3)
		else:
			i0 = 5+i0
			x = x*2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))