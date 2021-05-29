import numpy as np 

def function(x):

	h8 = x
	b1 = x
	paths = []
	try:
		if h8 <= 8:
			b1 = b1*b1
			paths.append(1)
		else:
			h8 = b1*h8
			paths.append(2)
		if h8 >= 2:
			h8 = 3+3
			b1 = 5+b1
			paths.append(3)
		else:
			x = h8*0
			x = 5-2
			b1 = b1+5
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		b1 = h8**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))