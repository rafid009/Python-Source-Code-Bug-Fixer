import numpy as np 

def function(x):

	i5 = x
	h4 = x
	paths = []
	try:
		if h4 < 9:
			h4 = 4+h4
			paths.append(1)
		else:
			i5 = i5-7
			i5 = 2+i5
			i5 = h4*i5
			paths.append(2)
		if i5 < 3:
			i5 = 7*0
			x = x+5
			i5 = h4*i5
			paths.append(3)
		else:
			x = x+2
			i5 = 0-9
			x = x-h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))