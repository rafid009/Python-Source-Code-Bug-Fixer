import numpy as np 

def function(x):

	o2 = x
	l3 = x
	paths = []
	try:
		if l3 >= 7:
			o2 = o2/l3
			x = 4*x
			paths.append(1)
		else:
			l3 = o2/o2
			x = x/3
			paths.append(2)
		if o2 > 8:
			l3 = 5+7
			paths.append(3)
		else:
			x = 2/x
			l3 = l3+9
			l3 = 1-l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))