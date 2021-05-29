import numpy as np 

def function(x):

	v2 = 1
	l7 = 5
	paths = []
	try:
		if v2 >= 5:
			l7 = x+l7
			l7 = l7-2
			v2 = v2*x
			paths.append(1)
		else:
			x = x+1
			v2 = 1*v2
			x = 3+x
			paths.append(2)
		if x <= 7:
			x = x/8
			paths.append(3)
		else:
			l7 = l7-7
			v2 = v2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))