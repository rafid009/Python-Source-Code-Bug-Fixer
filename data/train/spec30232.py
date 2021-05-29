import numpy as np 

def function(x):

	t0 = x
	i2 = x
	paths = []
	try:
		if x < 6:
			i2 = 6/i2
			paths.append(1)
		else:
			i2 = 7*i2
			paths.append(2)
		if i2 <= 9:
			i2 = 1*i2
			i2 = 8*i2
			i2 = 6+9
			paths.append(3)
		else:
			t0 = t0-9
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))