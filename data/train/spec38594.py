import numpy as np 

def function(x):

	l0 = 3
	v2 = x
	paths = []
	try:
		if l0 > 7:
			v2 = 5*v2
			v2 = 9+v2
			v2 = 5/v2
			paths.append(1)
		else:
			v2 = v2-6
			l0 = 2*l0
			l0 = 5-l0
			paths.append(2)
		if x <= 5:
			l0 = 0/l0
			v2 = v2*x
			paths.append(3)
		else:
			l0 = l0/5
			v2 = 7-v2
			l0 = x*1
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