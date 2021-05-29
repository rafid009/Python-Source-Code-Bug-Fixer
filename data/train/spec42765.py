import numpy as np 

def function(x):

	l3 = 3
	o5 = 6
	paths = []
	try:
		if o5 > 4:
			o5 = o5+x
			l3 = l3-8
			o5 = o5+6
			paths.append(1)
		else:
			x = x/l3
			l3 = l3+2
			o5 = 7/o5
			paths.append(2)
		if o5 >= 1:
			x = x+1
			paths.append(3)
		else:
			l3 = 6*l3
			l3 = 4*8
			o5 = 1-l3
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