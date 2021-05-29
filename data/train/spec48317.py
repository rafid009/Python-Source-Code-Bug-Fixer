import numpy as np 

def function(x):

	n1 = 2
	t2 = x
	paths = []
	try:
		if t2 <= 7:
			n1 = n1-1
			paths.append(1)
		else:
			x = x*3
			t2 = 5/3
			t2 = t2*t2
			paths.append(2)
		if x < 4:
			n1 = x*n1
			paths.append(3)
		else:
			t2 = t2/t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		n1 = t2**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))