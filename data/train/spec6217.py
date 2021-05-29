import numpy as np 

def function(x):

	t8 = 2
	d6 = x
	paths = []
	try:
		if x < 6:
			t8 = t8*d6
			d6 = d6/7
			t8 = 4+t8
			paths.append(1)
		else:
			t8 = 8+t8
			x = x*4
			paths.append(2)
		if t8 < 3:
			d6 = 5*d6
			x = 9+d6
			paths.append(3)
		else:
			d6 = 5*x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		d6 = t8**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))