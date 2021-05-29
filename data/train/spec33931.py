import numpy as np 

def function(x):

	l0 = 1
	v6 = x
	x = x
	paths = []
	try:
		if x >= 4:
			l0 = l0*4
			l0 = l0-l0
			x = 6*x
			paths.append(1)
		else:
			l0 = v6/l0
			x = x+0
			v6 = v6*l0
			paths.append(2)
		if l0 <= 5:
			v6 = l0*v6
			l0 = l0-6
			l0 = l0+l0
			paths.append(3)
		else:
			v6 = v6-8
			l0 = 8-l0
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		l0 = v6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))