import numpy as np 

def function(x):

	h1 = x
	v5 = 7
	paths = []
	try:
		if h1 >= 5:
			h1 = v5-h1
			paths.append(1)
		else:
			v5 = 6-8
			h1 = h1+9
			paths.append(2)
		if x > 4:
			x = x*2
			v5 = v5/h1
			x = 1*x
			paths.append(3)
		else:
			h1 = x*h1
			x = x*0
			v5 = v5-8
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		h1 = v5**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))