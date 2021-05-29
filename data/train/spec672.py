import numpy as np 

def function(x):

	n7 = x
	o2 = x
	paths = []
	try:
		if x > 6:
			n7 = n7-o2
			n7 = o2+3
			n7 = o2-o2
			paths.append(1)
		else:
			x = x+8
			x = x*x
			paths.append(2)
		if n7 >= 4:
			x = 4-x
			paths.append(3)
		else:
			x = 3/x
			n7 = 8*0
			o2 = 3*o2
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