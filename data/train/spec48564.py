import numpy as np 

def function(x):

	e1 = 2
	v3 = x
	paths = []
	try:
		if v3 < 7:
			v3 = v3+x
			e1 = x+e1
			v3 = e1*8
			paths.append(1)
		else:
			e1 = x-2
			x = 3*7
			paths.append(2)
		if x >= 5:
			x = 7*v3
			paths.append(3)
		else:
			v3 = 4*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))