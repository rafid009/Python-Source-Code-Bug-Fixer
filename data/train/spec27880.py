import numpy as np 

def function(x):

	b2 = x
	v3 = 7
	paths = []
	try:
		if v3 >= 2:
			v3 = 2*1
			b2 = b2+v3
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if v3 <= 3:
			b2 = b2/9
			v3 = v3*0
			x = x/9
			paths.append(3)
		else:
			b2 = x-b2
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