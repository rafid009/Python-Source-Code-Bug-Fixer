import numpy as np 

def function(x):

	u6 = x
	j1 = 5
	paths = []
	try:
		if j1 > 6:
			u6 = u6+9
			j1 = 6-2
			paths.append(1)
		else:
			u6 = u6+9
			x = x/u6
			paths.append(2)
		if u6 >= 8:
			j1 = j1*8
			u6 = 1*2
			u6 = u6*7
			paths.append(3)
		else:
			x = 4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))