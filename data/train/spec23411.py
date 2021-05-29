import numpy as np 

def function(x):

	w7 = x
	n2 = x
	paths = []
	try:
		if x <= 3:
			n2 = n2*2
			n2 = x-0
			x = 8*0
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if w7 > 3:
			x = 3*9
			n2 = 5/w7
			paths.append(3)
		else:
			x = x+3
			x = x+5
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		n2 = w7**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))