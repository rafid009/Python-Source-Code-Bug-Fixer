import numpy as np 

def function(x):

	v4 = 4
	a0 = 5
	paths = []
	try:
		if v4 >= 4:
			v4 = v4+v4
			paths.append(1)
		else:
			v4 = 5-v4
			a0 = a0/1
			v4 = v4+v4
			paths.append(2)
		if x <= 6:
			v4 = 5-v4
			a0 = 0*a0
			v4 = v4/5
			paths.append(3)
		else:
			v4 = a0/2
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		a0 = v4**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))