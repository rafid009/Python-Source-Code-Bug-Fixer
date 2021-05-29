import numpy as np 

def function(x):

	v1 = x
	b3 = 0
	paths = []
	try:
		if b3 > 4:
			x = x*1
			b3 = b3-v1
			paths.append(1)
		else:
			v1 = v1+7
			x = x+v1
			paths.append(2)
		if b3 >= 7:
			x = 8+x
			x = 3+x
			x = x/6
			paths.append(3)
		else:
			b3 = b3*v1
			x = v1-9
			b3 = b3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))