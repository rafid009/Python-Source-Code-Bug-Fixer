import numpy as np 

def function(x):

	v5 = 3
	l8 = 1
	paths = []
	try:
		if l8 < 5:
			v5 = v5/4
			l8 = l8+6
			x = x+1
			paths.append(1)
		else:
			x = x+6
			l8 = v5*l8
			paths.append(2)
		if x < 7:
			v5 = v5/3
			l8 = 0*2
			paths.append(3)
		else:
			l8 = 0/1
			l8 = 9*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))