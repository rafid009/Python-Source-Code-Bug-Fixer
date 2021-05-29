import numpy as np 

def function(x):

	d6 = 9
	t7 = 3
	x = x
	paths = []
	try:
		if t7 < 9:
			d6 = d6-x
			paths.append(1)
		else:
			x = 3/8
			d6 = d6+5
			x = x/8
			paths.append(2)
		if d6 < 3:
			x = x+x
			t7 = t7/8
			paths.append(3)
		else:
			t7 = t7-3
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		t7 = d6**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))