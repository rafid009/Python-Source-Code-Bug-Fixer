import numpy as np 

def function(x):

	o1 = 5
	l3 = x
	paths = []
	try:
		if l3 > 8:
			x = o1+x
			o1 = o1+l3
			l3 = 4-o1
			paths.append(1)
		else:
			o1 = o1-x
			paths.append(2)
		if x <= 7:
			l3 = l3/o1
			o1 = 3/o1
			paths.append(3)
		else:
			o1 = o1-0
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		o1 = l3**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))