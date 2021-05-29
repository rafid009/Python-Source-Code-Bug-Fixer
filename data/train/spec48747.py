import numpy as np 

def function(x):

	h2 = x
	l6 = x
	paths = []
	try:
		if l6 < 2:
			x = x/9
			paths.append(1)
		else:
			x = 5+x
			x = 3/1
			h2 = h2*h2
			paths.append(2)
		if x > 4:
			x = x+1
			paths.append(3)
		else:
			h2 = h2-9
			h2 = h2+5
			x = x+9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		h2 = l6**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))