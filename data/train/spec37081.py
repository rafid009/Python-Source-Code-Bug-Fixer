import numpy as np 

def function(x):

	n2 = 4
	o2 = 1
	paths = []
	try:
		if n2 > 6:
			x = x+9
			x = x+9
			paths.append(1)
		else:
			x = x+6
			n2 = x/n2
			paths.append(2)
		if n2 <= 4:
			o2 = x*9
			o2 = 9*o2
			paths.append(3)
		else:
			n2 = n2-x
			o2 = n2*9
			x = x*x
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