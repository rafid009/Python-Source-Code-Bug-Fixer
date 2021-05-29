import numpy as np 

def function(x):

	b9 = 1
	k6 = 3
	paths = []
	try:
		if k6 >= 7:
			b9 = b9-5
			x = x*x
			k6 = k6/8
			paths.append(1)
		else:
			k6 = 3*b9
			k6 = k6+6
			paths.append(2)
		if b9 > 9:
			x = x+x
			k6 = x-k6
			paths.append(3)
		else:
			k6 = 0*9
			k6 = k6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))