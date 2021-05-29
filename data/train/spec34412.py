import numpy as np 

def function(x):

	v6 = 8
	a0 = x
	paths = []
	try:
		if x >= 4:
			v6 = v6-9
			v6 = v6*3
			x = 5*7
			paths.append(1)
		else:
			v6 = v6/v6
			paths.append(2)
		if x <= 2:
			v6 = a0+1
			x = 4-v6
			x = x-x
			paths.append(3)
		else:
			x = x/3
			v6 = 6/7
			x = x-7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		a0 = v6**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))