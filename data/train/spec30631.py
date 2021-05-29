import numpy as np 

def function(x):

	t0 = x
	i2 = x
	paths = []
	try:
		if t0 < 8:
			i2 = 5*8
			i2 = 6/t0
			i2 = i2-9
			paths.append(1)
		else:
			x = x+5
			t0 = i2+7
			x = x+x
			paths.append(2)
		if x <= 1:
			x = x-6
			i2 = i2*8
			paths.append(3)
		else:
			i2 = i2*i2
			i2 = 6/9
			t0 = i2-t0
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