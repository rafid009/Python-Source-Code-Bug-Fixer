import numpy as np 

def function(x):

	b4 = 5
	v6 = x
	paths = []
	try:
		if b4 >= 9:
			b4 = 8+x
			b4 = v6*x
			paths.append(1)
		else:
			v6 = v6*b4
			v6 = v6*v6
			x = 7-x
			paths.append(2)
		if v6 <= 1:
			b4 = 7*8
			x = 5*7
			paths.append(3)
		else:
			v6 = v6-5
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