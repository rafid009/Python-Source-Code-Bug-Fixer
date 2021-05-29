import numpy as np 

def function(x):

	t6 = 4
	n2 = 0
	paths = []
	try:
		if t6 >= 1:
			n2 = 3-7
			t6 = t6*4
			t6 = t6+3
			paths.append(1)
		else:
			n2 = 0-n2
			n2 = n2/t6
			x = x-4
			paths.append(2)
		if t6 < 6:
			x = 7-x
			t6 = t6-t6
			n2 = n2*1
			paths.append(3)
		else:
			n2 = n2*2
			x = x+t6
			t6 = t6+8
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))