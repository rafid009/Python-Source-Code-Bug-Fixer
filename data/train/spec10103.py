import numpy as np 

def function(x):

	i2 = x
	t4 = 7
	x = x
	paths = []
	try:
		if t4 > 8:
			x = i2/x
			x = i2*i2
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if i2 < 8:
			i2 = i2+1
			paths.append(3)
		else:
			i2 = 8-t4
			x = 0*t4
			x = 7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))