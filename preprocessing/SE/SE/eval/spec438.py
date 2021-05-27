import numpy as np 

def function(x):

	w6 = x
	t8 = 8
	paths = []
	try:
		if t8 > 5:
			t8 = t8*3
			w6 = 0-w6
			x = x/8
			paths.append(1)
		else:
			w6 = 2-4
			w6 = 0-5
			w6 = 7+4
			paths.append(2)
		if w6 < 4:
			w6 = w6-5
			t8 = w6-x
			paths.append(3)
		else:
			x = 0-x
			w6 = w6/9
			t8 = t8/4
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