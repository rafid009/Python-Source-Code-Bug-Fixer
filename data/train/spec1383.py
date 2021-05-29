import numpy as np 

def function(x):

	o2 = 3
	n2 = 9
	paths = []
	try:
		if o2 >= 4:
			x = o2-x
			x = x-o2
			x = 4*x
			paths.append(1)
		else:
			x = x/7
			n2 = n2*2
			paths.append(2)
		if x > 5:
			o2 = o2+o2
			paths.append(3)
		else:
			o2 = o2+9
			o2 = 8-9
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		n2 = o2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))