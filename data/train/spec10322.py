import numpy as np 

def function(x):

	o9 = x
	x2 = 3
	paths = []
	try:
		if x2 >= 5:
			o9 = o9-0
			o9 = o9/3
			paths.append(1)
		else:
			o9 = o9-3
			x = x+9
			x = x*0
			paths.append(2)
		if x >= 3:
			x2 = 6+x2
			paths.append(3)
		else:
			x2 = 6*7
			x2 = x*3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))