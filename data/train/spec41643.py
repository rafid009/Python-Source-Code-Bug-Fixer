import numpy as np 

def function(x):

	t7 = x
	d6 = x
	paths = []
	try:
		if t7 < 2:
			t7 = t7-9
			t7 = 0*t7
			paths.append(1)
		else:
			x = x/9
			x = x+4
			x = t7+x
			paths.append(2)
		if t7 >= 3:
			x = 9-x
			t7 = 0+9
			x = 7+x
			paths.append(3)
		else:
			d6 = d6+2
			t7 = 4*t7
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))