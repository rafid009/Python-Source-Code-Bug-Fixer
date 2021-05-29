import numpy as np 

def function(x):

	n9 = 7
	t9 = 1
	x = 7
	paths = []
	try:
		if n9 <= 5:
			n9 = 4/x
			paths.append(1)
		else:
			n9 = 2-n9
			paths.append(2)
		if x >= 4:
			x = n9-x
			x = 1+5
			x = x/6
			paths.append(3)
		else:
			t9 = 8*t9
			n9 = n9/2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))