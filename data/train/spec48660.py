import numpy as np 

def function(x):

	j2 = x
	h1 = 5
	paths = []
	try:
		if x <= 1:
			j2 = j2-8
			h1 = h1/6
			x = 2-x
			paths.append(1)
		else:
			h1 = 5*h1
			h1 = h1+9
			paths.append(2)
		if j2 <= 0:
			h1 = h1*j2
			h1 = 1+h1
			paths.append(3)
		else:
			j2 = 2*j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))