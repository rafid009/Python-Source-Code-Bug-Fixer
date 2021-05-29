import numpy as np 

def function(x):

	h1 = x
	f6 = 0
	x = x
	paths = []
	try:
		if f6 <= 1:
			h1 = h1+6
			x = 2+h1
			paths.append(1)
		else:
			x = x+h1
			paths.append(2)
		if f6 < 4:
			f6 = 3+f6
			f6 = f6+3
			paths.append(3)
		else:
			x = 1*f6
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))