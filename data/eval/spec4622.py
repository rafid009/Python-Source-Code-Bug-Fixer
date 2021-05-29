import numpy as np 

def function(x):

	l9 = 5
	o2 = x
	x = 9
	paths = []
	try:
		if l9 >= 4:
			l9 = 4/x
			o2 = o2*7
			l9 = l9+9
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x <= 9:
			l9 = x*x
			x = 2-2
			paths.append(3)
		else:
			o2 = o2+8
			o2 = 8/8
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