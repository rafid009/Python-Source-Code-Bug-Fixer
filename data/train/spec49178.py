import numpy as np 

def function(x):

	b8 = x
	h1 = 8
	paths = []
	try:
		if h1 <= 5:
			x = 3+x
			x = x/4
			paths.append(1)
		else:
			h1 = h1/2
			paths.append(2)
		if x <= 5:
			b8 = x*8
			b8 = b8*0
			b8 = 4/1
			paths.append(3)
		else:
			h1 = h1-9
			x = 5-h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))