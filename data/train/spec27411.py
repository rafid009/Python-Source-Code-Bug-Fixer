import numpy as np 

def function(x):

	v8 = x
	p6 = x
	paths = []
	try:
		if x > 4:
			x = x*2
			paths.append(1)
		else:
			v8 = v8+2
			paths.append(2)
		if v8 <= 7:
			p6 = p6+7
			x = x+6
			paths.append(3)
		else:
			v8 = 5/v8
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