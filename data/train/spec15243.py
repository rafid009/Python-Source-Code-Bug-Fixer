import numpy as np 

def function(x):

	t7 = 0
	i2 = x
	paths = []
	try:
		if x >= 5:
			t7 = i2/4
			paths.append(1)
		else:
			x = 5+x
			t7 = t7/i2
			x = 2-i2
			paths.append(2)
		if t7 > 8:
			t7 = x*7
			i2 = i2/t7
			x = x/x
			paths.append(3)
		else:
			t7 = t7+8
			i2 = 6*7
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