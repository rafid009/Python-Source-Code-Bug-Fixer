import numpy as np 

def function(x):

	d5 = 9
	h3 = x
	paths = []
	try:
		if d5 >= 4:
			x = x*0
			d5 = d5+1
			d5 = 7+d5
			paths.append(1)
		else:
			d5 = d5-0
			d5 = 5+d5
			paths.append(2)
		if x >= 7:
			h3 = d5-h3
			h3 = 5-5
			h3 = x-h3
			paths.append(3)
		else:
			x = d5/d5
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))