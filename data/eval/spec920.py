import numpy as np 

def function(x):

	l3 = 6
	o1 = x
	x = 9
	paths = []
	try:
		if l3 < 4:
			l3 = 9+5
			x = 6/x
			paths.append(1)
		else:
			o1 = x/o1
			paths.append(2)
		if o1 < 7:
			x = x/o1
			l3 = 6*0
			paths.append(3)
		else:
			l3 = 1/l3
			l3 = l3+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))