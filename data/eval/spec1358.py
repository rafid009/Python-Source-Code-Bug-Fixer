import numpy as np 

def function(x):

	i2 = 3
	d6 = 2
	paths = []
	try:
		if i2 >= 7:
			x = x-x
			d6 = i2/9
			paths.append(1)
		else:
			x = i2*x
			i2 = 9*6
			paths.append(2)
		if d6 > 6:
			i2 = x*0
			d6 = d6*1
			d6 = 8/d6
			paths.append(3)
		else:
			i2 = i2-i2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))