import numpy as np 

def function(x):

	d9 = 7
	t8 = x
	x = x
	paths = []
	try:
		if t8 >= 4:
			t8 = 3+t8
			x = x-2
			x = x/5
			paths.append(1)
		else:
			x = x/7
			x = x+9
			paths.append(2)
		if d9 >= 7:
			d9 = d9*6
			x = x/t8
			x = x+x
			paths.append(3)
		else:
			d9 = t8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))