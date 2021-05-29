import numpy as np 

def function(x):

	t3 = 6
	d2 = x
	paths = []
	try:
		if d2 < 4:
			d2 = d2+t3
			x = 3-x
			paths.append(1)
		else:
			d2 = 9+d2
			paths.append(2)
		if t3 <= 3:
			t3 = t3*t3
			x = 5/d2
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))