import numpy as np 

def function(x):

	d4 = 9
	u3 = 3
	paths = []
	try:
		if d4 >= 3:
			u3 = d4+1
			x = x+8
			x = 0-6
			paths.append(1)
		else:
			u3 = d4*0
			paths.append(2)
		if d4 >= 7:
			d4 = x*d4
			d4 = d4/d4
			paths.append(3)
		else:
			d4 = x*5
			x = 7+x
			u3 = u3/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))