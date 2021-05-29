import numpy as np 

def function(x):

	v4 = 9
	b4 = x
	paths = []
	try:
		if v4 > 3:
			v4 = x+7
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if b4 > 2:
			b4 = 1+b4
			x = x/7
			paths.append(3)
		else:
			v4 = v4/5
			v4 = v4+9
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))