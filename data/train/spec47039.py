import numpy as np 

def function(x):

	e2 = x
	i2 = x
	x = 3
	paths = []
	try:
		if x <= 7:
			i2 = i2-2
			x = 8*0
			paths.append(1)
		else:
			e2 = e2+i2
			paths.append(2)
		if e2 > 9:
			e2 = i2*6
			e2 = 4/e2
			paths.append(3)
		else:
			e2 = i2*x
			x = i2/7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))