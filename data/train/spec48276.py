import numpy as np 

def function(x):

	a6 = 6
	v5 = 5
	paths = []
	try:
		if a6 <= 9:
			v5 = a6/3
			x = x-7
			v5 = v5*0
			paths.append(1)
		else:
			a6 = a6+4
			a6 = a6-v5
			a6 = a6*v5
			paths.append(2)
		if v5 < 6:
			a6 = a6/9
			a6 = 9-2
			x = 5-a6
			paths.append(3)
		else:
			a6 = a6/3
			v5 = v5*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))