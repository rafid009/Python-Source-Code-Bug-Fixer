import numpy as np 

def function(x):

	l1 = x
	o2 = x
	x = x
	paths = []
	try:
		if o2 < 6:
			l1 = l1/9
			x = x+o2
			paths.append(1)
		else:
			l1 = x+9
			x = x/l1
			paths.append(2)
		if l1 >= 7:
			o2 = o2*0
			paths.append(3)
		else:
			x = o2/x
			l1 = 4*l1
			x = 5/2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))