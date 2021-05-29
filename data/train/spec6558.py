import numpy as np 

def function(x):

	n8 = x
	t8 = 5
	paths = []
	try:
		if x > 3:
			t8 = 8-t8
			t8 = t8*5
			paths.append(1)
		else:
			n8 = n8+8
			paths.append(2)
		if n8 >= 9:
			n8 = 3*t8
			paths.append(3)
		else:
			x = n8-4
			t8 = t8-8
			x = n8*2
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		n8 = t8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))