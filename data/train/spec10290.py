import numpy as np 

def function(x):

	d2 = x
	t8 = x
	paths = []
	try:
		if t8 >= 5:
			d2 = d2+d2
			d2 = d2/4
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x <= 1:
			x = x/d2
			paths.append(3)
		else:
			t8 = t8+d2
			t8 = 4-d2
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))