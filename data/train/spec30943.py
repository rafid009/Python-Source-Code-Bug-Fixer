import numpy as np 

def function(x):

	w6 = x
	i2 = 1
	x = 6
	paths = []
	try:
		if i2 >= 9:
			x = x/8
			paths.append(1)
		else:
			w6 = w6+w6
			paths.append(2)
		if i2 < 0:
			i2 = 6+i2
			w6 = i2*x
			paths.append(3)
		else:
			x = x/i2
			i2 = i2/8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		i2 = w6**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))