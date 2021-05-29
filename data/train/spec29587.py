import numpy as np 

def function(x):

	v5 = x
	o1 = x
	paths = []
	try:
		if v5 < 5:
			x = o1/x
			o1 = 0-o1
			o1 = v5/o1
			paths.append(1)
		else:
			x = 4+x
			v5 = v5/1
			x = 9*x
			paths.append(2)
		if v5 <= 0:
			x = x/o1
			paths.append(3)
		else:
			o1 = o1-o1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		o1 = v5**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))