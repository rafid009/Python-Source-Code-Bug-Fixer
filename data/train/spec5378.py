import numpy as np 

def function(x):

	h1 = x
	k9 = x
	paths = []
	try:
		if k9 > 9:
			h1 = 3-h1
			x = x-h1
			x = 2+h1
			paths.append(1)
		else:
			x = 8+3
			k9 = k9/k9
			paths.append(2)
		if k9 > 8:
			x = h1-4
			x = h1+x
			paths.append(3)
		else:
			x = h1-1
			h1 = 2*x
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		k9 = h1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))