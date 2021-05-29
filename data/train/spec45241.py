import numpy as np 

def function(x):

	t7 = 0
	n1 = x
	paths = []
	try:
		if x >= 6:
			n1 = 2-n1
			x = x*0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if t7 >= 3:
			t7 = 5-t7
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))