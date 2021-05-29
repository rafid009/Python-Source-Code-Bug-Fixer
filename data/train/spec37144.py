import numpy as np 

def function(x):

	o2 = x
	r7 = 0
	paths = []
	try:
		if x < 2:
			o2 = 9*r7
			paths.append(1)
		else:
			o2 = 4-o2
			paths.append(2)
		if x <= 2:
			x = 6+x
			x = x/9
			paths.append(3)
		else:
			x = x-0
			o2 = o2-r7
			r7 = 7*6
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		r7 = o2**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))