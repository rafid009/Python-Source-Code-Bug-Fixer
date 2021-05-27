import numpy as np 

def function(x):

	t3 = 8
	o6 = 0
	paths = []
	try:
		if t3 > 3:
			o6 = o6*o6
			o6 = 5*o6
			o6 = x+o6
			paths.append(1)
		else:
			o6 = 9+1
			x = 6+x
			t3 = t3/t3
			paths.append(2)
		if x > 7:
			o6 = o6+9
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))