import numpy as np 

def function(x):

	o2 = x
	t3 = 1
	paths = []
	try:
		if o2 <= 7:
			t3 = t3+t3
			paths.append(1)
		else:
			x = 5/o2
			paths.append(2)
		if t3 < 8:
			o2 = 3-o2
			o2 = 0-o2
			paths.append(3)
		else:
			x = 5-t3
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))