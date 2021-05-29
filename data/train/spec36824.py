import numpy as np 

def function(x):

	v6 = 2
	i2 = 7
	paths = []
	try:
		if x >= 4:
			i2 = 3+6
			v6 = x-5
			paths.append(1)
		else:
			v6 = v6+5
			paths.append(2)
		if x >= 2:
			v6 = 7*v6
			x = i2/x
			paths.append(3)
		else:
			v6 = 7*v6
			i2 = i2*2
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		i2 = v6**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))